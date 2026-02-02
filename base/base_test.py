"""
Base Test Class for Selenium Test Automation
Provides common utilities, dynamic waits, and error handling
"""

import logging
import os
import time
from datetime import datetime
from typing import Optional, Tuple, List, Callable
from functools import wraps

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException,
)
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_execution.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def retry_on_exception(max_retries: int = 3, delay: float = 0.5):
    """Decorator to retry operations on exception"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (
                    StaleElementReferenceException,
                    ElementNotInteractableException,
                ) as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(
                        f"Attempt {attempt + 1} failed: {e}. Retrying..."
                    )
                    time.sleep(delay * (attempt + 1))
            return None

        return wrapper

    return decorator


class BaseTest:
    """Base class for all test cases with dynamic waits and error handling"""

    # Default configuration
    DEFAULT_TIMEOUT = 20
    DEFAULT_POLL_FREQUENCY = 0.5
    BASE_URL = "https://testing.d1z4wu6myne6l0.amplifyapp.com"

    def setup_driver(
        self, headless: bool = False, timeout: int = DEFAULT_TIMEOUT
    ) -> webdriver.Chrome:
        """Setup and configure Chrome driver with options"""
        logger.info("Setting up Chrome driver...")

        # Initialize instance attributes
        self.driver: Optional[webdriver.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
        self.actions: Optional[ActionChains] = None
        self.timeout = timeout
        self.headless = headless
        self.test_start_time: Optional[datetime] = None

        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )

        if self.headless:
            options.add_argument("--headless")

        # Disable automation flags
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        options.add_experimental_option("useAutomationExtension", False)

        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', "
                "{get: () => undefined})"
            )
            self.wait = WebDriverWait(
                self.driver,
                self.timeout,
                poll_frequency=self.DEFAULT_POLL_FREQUENCY,
            )
            self.actions = ActionChains(self.driver)
            self.driver.maximize_window()
            logger.info("Chrome driver setup completed successfully")
            return self.driver
        except WebDriverException as e:
            logger.error(f"Failed to setup Chrome driver: {e}")
            raise

    def teardown(self):
        """Clean up and close browser"""
        if self.driver:
            try:
                logger.info("Closing browser...")
                self.driver.quit()
                logger.info("Browser closed successfully")
            except Exception as e:
                logger.error(f"Error closing browser: {e}")

    def navigate_to(self, path: str):
        """Navigate to a specific URL path"""
        url = f"{self.BASE_URL}{path}"
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        self.wait_for_page_load()

    def wait_for_page_load(self, timeout: int = 30):
        """Wait for page to fully load"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState")
                == "complete"
            )
            logger.debug("Page loaded successfully")
        except TimeoutException:
            logger.warning("Page load timeout - continuing anyway")

    def wait_for_element(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
        condition=EC.presence_of_element_located,
    ) -> WebElement:
        """
        Wait for an element with specified condition

        Args:
            locator: Tuple of (By, str) for element location
            timeout: Custom timeout (uses default if None)
            condition: Expected condition to wait for

        Returns:
            WebElement when condition is met
        """
        wait_time = timeout or self.timeout
        custom_wait = WebDriverWait(
            self.driver, wait_time, poll_frequency=self.DEFAULT_POLL_FREQUENCY
        )

        try:
            element = custom_wait.until(condition(locator))
            logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timeout waiting for element: {locator}")
            raise

    def wait_for_clickable(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
    ) -> WebElement:
        """Wait for element to be clickable"""
        return self.wait_for_element(
            locator, timeout, EC.element_to_be_clickable
        )

    def wait_for_visible(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
    ) -> WebElement:
        """Wait for element to be visible"""
        return self.wait_for_element(
            locator, timeout, EC.visibility_of_element_located
        )

    def wait_for_presence(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
    ) -> WebElement:
        """Wait for element to be present in DOM"""
        return self.wait_for_element(
            locator, timeout, EC.presence_of_element_located
        )

    def wait_for_all_elements(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
    ) -> List[WebElement]:
        """Wait for all elements matching locator"""
        wait_time = timeout or self.timeout
        custom_wait = WebDriverWait(self.driver, wait_time)

        try:
            elements = custom_wait.until(
                EC.presence_of_all_elements_located(locator)
            )
            logger.debug(f"Found {len(elements)} elements for: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"Timeout waiting for elements: {locator}")
            raise

    def wait_for_element_invisible(
        self,
        locator: Tuple[By, str],
        timeout: Optional[int] = None,
    ) -> bool:
        """Wait for element to become invisible"""
        wait_time = timeout or self.timeout
        custom_wait = WebDriverWait(self.driver, wait_time)

        try:
            return custom_wait.until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.warning(
                f"Element still visible after timeout: {locator}"
            )
            return False

    def wait_for_overlay_to_disappear(self, timeout: int = 10):
        """Wait for loading overlays/modals to disappear"""
        overlay_selectors = [
            (By.CSS_SELECTOR, ".modal"),
            (By.CSS_SELECTOR, ".modal-backdrop"),
            (By.CSS_SELECTOR, ".overlay"),
            (By.CSS_SELECTOR, ".spinner"),
            (By.CSS_SELECTOR, ".loading"),
            (By.CSS_SELECTOR, ".loader"),
            (By.CSS_SELECTOR, "[class*='loading']"),
            (By.CSS_SELECTOR, "[class*='spinner']"),
        ]

        for selector in overlay_selectors:
            try:
                self.wait_for_element_invisible(selector, timeout=2)
            except Exception:
                pass

    @retry_on_exception(max_retries=3)
    def click_element(
        self,
        locator: Tuple[By, str],
        use_js: bool = False,
        scroll: bool = True,
    ):
        """
        Click an element with retry logic

        Args:
            locator: Element locator tuple
            use_js: Use JavaScript click instead of native click
            scroll: Scroll element into view before clicking
        """
        element = self.wait_for_clickable(locator)

        if scroll:
            self.scroll_to_element(element)

        self.wait_for_overlay_to_disappear()

        try:
            if use_js:
                self.driver.execute_script("arguments[0].click();", element)
            else:
                element.click()
            logger.debug(f"Clicked element: {locator}")
        except ElementClickInterceptedException:
            logger.warning(
                f"Click intercepted, using JavaScript click for: {locator}"
            )
            self.driver.execute_script("arguments[0].click();", element)

    @retry_on_exception(max_retries=3)
    def send_keys_to_element(
        self,
        locator: Tuple[By, str],
        text: str,
        clear_first: bool = True,
    ):
        """Send keys to an element"""
        element = self.wait_for_visible(locator)

        if clear_first:
            element.clear()
            # Ensure clear worked
            if element.get_attribute("value"):
                element.send_keys(Keys.CONTROL + "a")
                element.send_keys(Keys.DELETE)

        element.send_keys(text)
        logger.debug(f"Sent keys to element: {locator}")

    def scroll_to_element(self, element: WebElement, block: str = "center"):
        """Scroll element into view"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: '%s', behavior: 'smooth'});"
            % block,
            element,
        )

    def scroll_by(self, x: int = 0, y: int = 500):
        """Scroll by specified amount"""
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_element_text(self, locator: Tuple[By, str]) -> str:
        """Get text from an element"""
        element = self.wait_for_visible(locator)
        return element.text.strip()

    def get_element_attribute(
        self, locator: Tuple[By, str], attribute: str
    ) -> str:
        """Get attribute value from an element"""
        element = self.wait_for_presence(locator)
        return element.get_attribute(attribute)

    def is_element_present(
        self, locator: Tuple[By, str], timeout: int = 3
    ) -> bool:
        """Check if element is present (without raising exception)"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_visible(
        self, locator: Tuple[By, str], timeout: int = 3
    ) -> bool:
        """Check if element is visible (without raising exception)"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name: Optional[str] = None) -> str:
        """Take a screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name or 'screenshot'}_{timestamp}.png"

        # Create screenshots directory if it doesn't exist
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        filepath = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        return filepath

    def login(
        self,
        email: str = "admin@gmail.com",
        password: str = "Bmr@1234",
    ):
        """Perform login operation"""
        logger.info("Performing login...")

        self.navigate_to("/admin/login")

        # Enter credentials
        self.send_keys_to_element(
            (By.XPATH, '//input[@name="email" or @type="email"]'),
            email,
        )
        self.send_keys_to_element(
            (By.XPATH, '//input[@type="password"]'),
            password,
        )

        # Click login
        self.click_element((By.XPATH, '//button[@type="submit"]'))

        # Wait for navigation after login - wait for dashboard to load
        try:
            self.wait_for_visible(
                (By.XPATH, '//*[contains(text(), "Dashboard")]'),
                timeout=15,
            )
            logger.info("Login completed successfully - Dashboard loaded")
        except TimeoutException:
            # Try alternative dashboard indicators
            try:
                self.wait_for_visible(
                    (By.XPATH, '//*[contains(text(), "Gamer PC")]'),
                    timeout=5,
                )
                logger.info(
                    "Login completed successfully - Gamer PC header found"
                )
            except TimeoutException:
                logger.warning(
                    "Could not verify dashboard loaded, continuing anyway"
                )

    def logout(self):
        """Perform logout operation"""
        logger.info("Performing logout...")
        # Add logout logic based on your application
        # This is a placeholder - modify according to your app's logout mechanism

    def assert_element_present(
        self, locator: Tuple[By, str], message: Optional[str] = None
    ):
        """Assert that element is present"""
        assert self.is_element_present(locator), (
            message or f"Element not found: {locator}"
        )

    def assert_element_visible(
        self, locator: Tuple[By, str], message: Optional[str] = None
    ):
        """Assert that element is visible"""
        assert self.is_element_visible(locator), (
            message or f"Element not visible: {locator}"
        )

    def assert_text_present(self, text: str, message: Optional[str] = None):
        """Assert that text is present on page"""
        assert text in self.driver.page_source, (
            message or f"Text not found: {text}"
        )

