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
    WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_execution.log'),
        logging.StreamHandler()
    ]
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
                except (StaleElementReferenceException, ElementNotInteractableException) as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (attempt + 1))
            return None
        return wrapper
    return decorator


class BaseTest:
    """Base class for all test cases with dynamic waits and error handling"""
    
    # Default configuration
    DEFAULT_TIMEOUT = 30  # Increased from 20 to handle slower page loads
    DEFAULT_POLL_FREQUENCY = 0.5
    BASE_URL = "https://testing.d1z4wu6myne6l0.amplifyapp.com"
        
    def setup_driver(self, headless: bool = False, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Chrome:
        """Setup and configure Chrome driver with options"""
        logger.info("Setting up Chrome driver...")
        
        # Determine effective headless mode:
        # - explicit argument takes precedence
        # - otherwise fall back to HEADLESS environment variable (set by run_tests.py)
        if headless:
            effective_headless = True
        else:
            env_headless = os.getenv("HEADLESS", "").strip().lower()
            effective_headless = env_headless in ("1", "true", "yes", "y")
        
        # Initialize instance attributes
        self.driver: Optional[webdriver.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
        self.actions: Optional[ActionChains] = None
        self.timeout = timeout
        self.headless = effective_headless
        self.test_start_time: Optional[datetime] = None
        
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--remote-allow-origins=*")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        if self.headless:
            options.add_argument("--headless=new")
            
        # Disable automation flags
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
        })
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )
            self.wait = WebDriverWait(self.driver, self.timeout, poll_frequency=self.DEFAULT_POLL_FREQUENCY)
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
        # Wait for any loading overlays to disappear
        self.wait_for_no_loading(timeout=10)
    
    def wait_for_page_load(self, timeout: int = 30):
        """Wait for page to fully load"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            logger.debug("Page loaded successfully")
        except TimeoutException:
            logger.warning("Page load timeout - continuing anyway")
    
    def wait_for_element(
        self, 
        locator: Tuple[By, str], 
        timeout: Optional[int] = None,
        condition = EC.presence_of_element_located
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
        custom_wait = WebDriverWait(self.driver, wait_time, poll_frequency=self.DEFAULT_POLL_FREQUENCY)
        
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
        timeout: Optional[int] = None
    ) -> WebElement:
        """Wait for element to be clickable"""
        return self.wait_for_element(locator, timeout, EC.element_to_be_clickable)
    
    def wait_for_visible(
        self, 
        locator: Tuple[By, str], 
        timeout: Optional[int] = None
    ) -> WebElement:
        """Wait for element to be visible"""
        return self.wait_for_element(locator, timeout, EC.visibility_of_element_located)
    
    def wait_for_presence(
        self, 
        locator: Tuple[By, str], 
        timeout: Optional[int] = None
    ) -> WebElement:
        """Wait for element to be present in DOM"""
        return self.wait_for_element(locator, timeout, EC.presence_of_element_located)
    
    def wait_for_all_elements(
        self, 
        locator: Tuple[By, str], 
        timeout: Optional[int] = None
    ) -> List[WebElement]:
        """Wait for all elements matching locator"""
        wait_time = timeout or self.timeout
        custom_wait = WebDriverWait(self.driver, wait_time)
        
        try:
            elements = custom_wait.until(EC.presence_of_all_elements_located(locator))
            logger.debug(f"Found {len(elements)} elements for: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"Timeout waiting for elements: {locator}")
            raise
    
    def wait_for_element_invisible(
        self, 
        locator: Tuple[By, str], 
        timeout: Optional[int] = None
    ) -> bool:
        """Wait for element to become invisible"""
        wait_time = timeout or self.timeout
        custom_wait = WebDriverWait(self.driver, wait_time)
        
        try:
            return custom_wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            logger.warning(f"Element still visible after timeout: {locator}")
            return False
    
    def wait_for_overlay_to_disappear(self, timeout: int = 10):
        """Wait for loading overlays to disappear (NOT modals - those are legitimate UI)"""
        overlay_selectors = [
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
            except:
                pass
    
    @retry_on_exception(max_retries=3)
    def click_element(
        self, 
        locator: Tuple[By, str], 
        use_js: bool = False,
        scroll: bool = True
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
            logger.warning(f"Click intercepted, using JavaScript click for: {locator}")
            self.driver.execute_script("arguments[0].click();", element)
    
    @retry_on_exception(max_retries=3)
    def send_keys_to_element(
        self, 
        locator: Tuple[By, str], 
        text: str,
        clear_first: bool = True
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
            f"arguments[0].scrollIntoView({{block: '{block}', behavior: 'smooth'}});", 
            element
        )
    
    def scroll_by(self, x: int = 0, y: int = 500):
        """Scroll by specified amount"""
        self.driver.execute_script(f"window.scrollBy({x}, {y});")
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    def get_element_text(self, locator: Tuple[By, str]) -> str:
        """Get text from an element"""
        element = self.wait_for_visible(locator)
        return element.text.strip()
    
    def get_element_attribute(self, locator: Tuple[By, str], attribute: str) -> str:
        """Get attribute value from an element"""
        element = self.wait_for_presence(locator)
        return element.get_attribute(attribute)
    
    def is_element_present(self, locator: Tuple[By, str], timeout: int = 3) -> bool:
        """Check if element is present (without raising exception)"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 3) -> bool:
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
    
    def login(self, email: str = "admin@gmail.com", password: str = "Bmr@1234"):
        """Perform login operation"""
        logger.info("Performing login...")
        
        self.navigate_to("/admin/login")
        
        # Enter credentials
        self.send_keys_to_element((By.XPATH, '//input[@name="email" or @type="email"]'), email)
        self.send_keys_to_element((By.XPATH, '//input[@type="password"]'), password)
        
        # Click login
        self.click_element((By.XPATH, '//button[@type="submit"]'))
        
        # Wait for navigation after login - wait for dashboard to load
        try:
            self.wait_for_visible((By.XPATH, '//*[contains(text(), "Dashboard")]'), timeout=15)
            logger.info("Login completed successfully - Dashboard loaded")
        except TimeoutException:
            # Try alternative dashboard indicators
            try:
                self.wait_for_visible((By.XPATH, '//*[contains(text(), "Gamer PC")]'), timeout=5)
                logger.info("Login completed successfully - Gamer PC header found")
            except TimeoutException:
                logger.warning("Could not verify dashboard loaded, continuing anyway")
    
    def logout(self):
        """Perform logout operation"""
        logger.info("Performing logout...")
        # Add logout logic based on your application
        # This is a placeholder - modify according to your app's logout mechanism
    
    def assert_element_present(self, locator: Tuple[By, str], message: Optional[str] = None):
        """Assert that element is present"""
        assert self.is_element_present(locator), message or f"Element not found: {locator}"
    
    def assert_element_visible(self, locator: Tuple[By, str], message: Optional[str] = None):
        """Assert that element is visible"""
        assert self.is_element_visible(locator), message or f"Element not visible: {locator}"
    
    def assert_text_present(self, text: str, message: Optional[str] = None):
        """Assert that text is present on page"""
        assert text in self.driver.page_source, message or f"Text not found: {text}"

    def wait_for_no_loading(self, timeout: int = 10):
        """Wait for all loading indicators to disappear"""
        loading_selectors = [
            (By.CSS_SELECTOR, ".spinner"),
            (By.CSS_SELECTOR, ".loading"),
            (By.CSS_SELECTOR, ".loader"),
            (By.CSS_SELECTOR, "[class*='loading']"),
            (By.CSS_SELECTOR, "[class*='spinner']"),
            (By.CSS_SELECTOR, "[class*='loader']"),
            (By.XPATH, "//*[contains(@class,'spin')]"),
        ]

        for selector in loading_selectors:
            try:
                self.wait_for_element_invisible(selector, timeout=timeout)
            except:
                pass

        logger.debug("All loading indicators cleared")

    def wait_for_dropdown_open(self, timeout: int = 5) -> bool:
        """Wait for react-select dropdown menu to open"""
        menu_selectors = [
            (By.CSS_SELECTOR, ".react-select__menu"),
            (By.CSS_SELECTOR, "[class*='react-select__menu']"),
            (By.XPATH, "//div[contains(@class,'react-select__menu')]"),
        ]

        for selector in menu_selectors:
            try:
                self.wait_for_visible(selector, timeout=timeout)
                logger.debug("Dropdown menu opened successfully")
                return True
            except:
                continue

        logger.warning("Could not verify dropdown menu opened")
        return False

    def wait_for_page_ready(self, expected_heading: Optional[str] = None, timeout: int = 30):
        """
        Comprehensive page load verification

        Args:
            expected_heading: Text to look for in h1-h6 tags
            timeout: Maximum wait time
        """
        # Wait for document ready state
        self.wait_for_page_load(timeout=timeout)

        # Wait for loading indicators to disappear
        self.wait_for_no_loading(timeout=10)

        # If expected heading provided, wait for it
        if expected_heading:
            heading_selectors = [
                (By.XPATH, f"//h1[contains(text(),'{expected_heading}')]"),
                (By.XPATH, f"//h2[contains(text(),'{expected_heading}')]"),
                (By.XPATH, f"//h3[contains(text(),'{expected_heading}')]"),
                (By.XPATH, f"//h4[contains(text(),'{expected_heading}')]"),
                (By.XPATH, f"//h5[contains(text(),'{expected_heading}')]"),
                (By.XPATH, f"//h6[contains(text(),'{expected_heading}')]"),
            ]

            for selector in heading_selectors:
                try:
                    self.wait_for_visible(selector, timeout=5)
                    logger.info(f"Found expected heading: {expected_heading}")
                    return
                except:
                    continue

            logger.warning(f"Expected heading '{expected_heading}' not found")

        logger.debug("Page ready")

    def find_element_with_fallbacks(
        self,
        selectors: List[Tuple[By, str]],
        timeout: int = 5
    ) -> Optional[WebElement]:
        """
        Try multiple selectors in sequence until one works

        Args:
            selectors: List of (By, selector) tuples to try
            timeout: Timeout for each selector attempt

        Returns:
            WebElement if found, None otherwise
        """
        for by, selector in selectors:
            try:
                element = self.wait_for_presence((by, selector), timeout=timeout)
                logger.debug(f"Element found using selector: {selector}")
                return element
            except TimeoutException:
                continue

        logger.warning(f"Element not found with any of {len(selectors)} selectors")
        return None

    @retry_on_exception(max_retries=3)
    def select_from_react_dropdown(
        self,
        dropdown_locator: Optional[Tuple[By, str]] = None,
        dropdown_index: Optional[int] = None,
        option_text: Optional[str] = None,
        option_index: int = 0,
        max_retries: int = 3
    ) -> bool:
        """
        Universal react-select dropdown handler with robust error handling

        Args:
            dropdown_locator: Tuple (By, selector) to find dropdown
            dropdown_index: 0-based index if multiple dropdowns (alternative to locator)
            option_text: Text to search for in options (partial match)
            option_index: If option_text not provided, select by index (default 0 = first)
            max_retries: Number of retry attempts

        Returns:
            True if successful, False otherwise

        Example:
            # Select by dropdown index and option text
            self.select_from_react_dropdown(dropdown_index=0, option_text="Electronics")

            # Select by locator and option index
            locator = (By.XPATH, "//div[@id='category-select']")
            self.select_from_react_dropdown(dropdown_locator=locator, option_index=1)
        """
        for attempt in range(max_retries):
            try:
                # Step 1: Find the dropdown control
                if dropdown_locator:
                    dropdown = self.wait_for_clickable(dropdown_locator, timeout=10)
                elif dropdown_index is not None:
                    # Find all enabled react-select controls
                    time.sleep(0.5)  # Brief wait for DOM to stabilize
                    dropdowns = self.driver.find_elements(
                        By.XPATH,
                        '//div[contains(@class,"react-select__control") and not(contains(@class,"--is-disabled"))]'
                    )

                    if len(dropdowns) <= dropdown_index:
                        logger.warning(f"Dropdown index {dropdown_index} not found, only {len(dropdowns)} enabled")
                        if attempt < max_retries - 1:
                            time.sleep(1)
                            continue
                        return False

                    dropdown = dropdowns[dropdown_index]
                else:
                    logger.error("Must provide either dropdown_locator or dropdown_index")
                    return False

                # Step 2: Scroll dropdown into view
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
                    dropdown
                )
                time.sleep(0.3)

                # Step 3: Wait for any overlays to clear
                self.wait_for_overlay_to_disappear(timeout=3)

                # Step 4: Click the dropdown (try both methods)
                try:
                    dropdown.click()
                except (ElementNotInteractableException, ElementClickInterceptedException):
                    logger.debug("Regular click failed, using JavaScript click")
                    self.driver.execute_script("arguments[0].click();", dropdown)

                # Step 5: Wait for dropdown menu to open
                time.sleep(0.8)  # Allow animation to complete

                if not self.wait_for_dropdown_open(timeout=5):
                    logger.warning("Dropdown menu did not open, retrying...")
                    if attempt < max_retries - 1:
                        continue
                    return False

                # Step 6: Find all options in the opened menu
                option_selectors = [
                    '//div[contains(@class,"react-select__menu")]//div[@role="option"]',
                    '//div[@role="listbox"]//div[@role="option"]',
                    '//div[contains(@class,"react-select__option")]',
                    '//div[@role="option" and not(contains(@class,"disabled"))]',
                ]

                all_options = []
                for selector in option_selectors:
                    all_options = self.driver.find_elements(By.XPATH, selector)
                    if all_options:
                        logger.debug(f"Found {len(all_options)} options using selector: {selector}")
                        break

                if not all_options:
                    logger.warning("No options found in dropdown menu")
                    # Close dropdown and retry
                    from selenium.webdriver.common.keys import Keys
                    body = self.driver.find_element(By.TAG_NAME, 'body')
                    body.send_keys(Keys.ESCAPE)
                    time.sleep(0.5)
                    if attempt < max_retries - 1:
                        continue
                    return False

                # Step 7: Select the option
                target_option = None

                if option_text and option_text.strip():
                    # Find option by text (partial match, case-insensitive)
                    for opt in all_options:
                        try:
                            opt_text = opt.text.strip()
                            if option_text.lower() in opt_text.lower():
                                target_option = opt
                                logger.debug(f"Found matching option: {opt_text}")
                                break
                        except StaleElementReferenceException:
                            continue

                # If no text match or text not provided, use index
                if not target_option:
                    if 0 <= option_index < len(all_options):
                        target_option = all_options[option_index]
                        try:
                            logger.debug(f"Selecting option by index {option_index}: {target_option.text.strip()}")
                        except:
                            logger.debug(f"Selecting option by index {option_index}")
                    else:
                        logger.warning(f"Option index {option_index} out of range (0-{len(all_options)-1})")
                        target_option = all_options[0] if all_options else None

                if not target_option:
                    logger.error("Could not determine target option")
                    return False

                # Step 8: Click the option
                try:
                    # Scroll option into view
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block: 'nearest', behavior: 'instant'});",
                        target_option
                    )
                    time.sleep(0.2)

                    # Try JavaScript click first (more reliable for react-select)
                    self.driver.execute_script("arguments[0].click();", target_option)
                except Exception as click_error:
                    logger.debug(f"JavaScript click failed, trying regular click: {click_error}")
                    target_option.click()

                # Step 9: Wait for dropdown to close
                time.sleep(0.5)

                # Step 10: Verify selection (optional but recommended)
                try:
                    selected_text = dropdown.text.strip()
                    logger.info(f"Successfully selected from dropdown: {selected_text}")
                except:
                    logger.info("Dropdown selection completed")

                return True

            except StaleElementReferenceException as e:
                logger.warning(f"Stale element on attempt {attempt + 1}/{max_retries}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                return False

            except Exception as e:
                logger.warning(f"Dropdown selection attempt {attempt + 1}/{max_retries} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                return False

        logger.error("All dropdown selection attempts failed")
        return False
