import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# -------------------------------
# Logging Setup
# -------------------------------
logging.basicConfig(
    filename="automation_log.txt",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.warning(message)

# -------------------------------
# Utility Functions
# -------------------------------
def safe_click(driver, locator, retries=2, timeout=15):
    """Click element safely with retry and scroll"""
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
            return True
        except Exception as e:
            log_and_print(f"⚠️ Attempt {attempt+1}: Could not click {locator} -> {e}", "warning")
            time.sleep(1)
    return False

def safe_type(driver, locator, text, retries=2, timeout=15):
    """Type text safely with retry"""
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            log_and_print(f"⚠️ Attempt {attempt+1}: Could not type {locator} -> {e}", "warning")
            time.sleep(1)
    return False

# -------------------------------
# Browser Setup
# -------------------------------
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    # -------------------------------
    # LOGIN
    # -------------------------------
    driver.get("https://bavit-dev.vercel.app/admin/login")
    safe_type(driver, (By.NAME, "email"), "admin@gmail.com")
    safe_type(driver, (By.XPATH, '//input[@type="password"]'), "Bmr@1234")
    safe_click(driver, (By.XPATH, '//button[@type="submit"]'))
    log_and_print("✅ Logged in successfully")

    # -------------------------------
    # NAVIGATION
    # -------------------------------
    safe_click(driver, (By.XPATH, "//span[contains(text(),'Inventory')]"))
    safe_click(driver, (By.XPATH, "//a[contains(text(),'View Stock')]"))
    safe_click(driver, (By.XPATH, "//i[contains(@class,'ri-add-line')]"))
    log_and_print("✅ Navigated to Add Product Page")

    # -------------------------------
    # PRODUCT FORM
    # -------------------------------
    safe_click(driver, (By.XPATH, '//label[@for="products-radio"]'))

    # Category
    safe_click(driver, (By.XPATH, "//div[@id='categorySelect']//div[contains(@class,'select__control')]"))
    safe_click(driver, (By.XPATH, "//div[contains(@id,'react-select') and @role='option'][1]"))

    # Product
    safe_click(driver, (By.XPATH, "//div[contains(@id,'layout-wrapper')]//form//div[contains(@class,'select__control')][2]"))
    safe_click(driver, (By.XPATH, "//div[contains(@id,'react-select') and @role='option'][1]"))

    # Supplier
    safe_click(driver, (By.XPATH, "//*[@id='supplier-select']//div[contains(@class,'select__control')]"))
    safe_click(driver, (By.XPATH, "//div[contains(@id,'react-select') and @role='option'][2]"))

    # Received By
    safe_click(driver, (By.XPATH, "//*[@id='user-select']//div[contains(@class,'select__control')]"))
    safe_click(driver, (By.XPATH, "//div[contains(@id,'react-select') and @role='option'][2]"))

    # Purchase & Received Dates
    safe_click(driver, (By.XPATH, "//button[@aria-label='Choose date']"))
    safe_click(driver, (By.XPATH, "(//div[@role='dialog']//button[contains(@class,'MuiPickersDay')])[5]"))
    safe_click(driver, (By.XPATH, "(//button[@aria-label='Choose date'])[2]"))
    safe_click(driver, (By.XPATH, "(//div[@role='dialog']//button[contains(@class,'MuiPickersDay')])[6]"))

    # Add Expense
    safe_click(driver, (By.XPATH, "//button[contains(.,'Add Expense')]"))
    safe_click(driver, (By.XPATH, "//*[@id='name-0']//div[contains(@class,'select__control')]"))
    safe_click(driver, (By.XPATH, "//div[contains(@id,'react-select') and @role='option'][1]"))
    safe_type(driver, (By.XPATH, '//*[@id="value-0"]'), "120")
    safe_click(driver, (By.XPATH, "//div[@role='dialog']//button[contains(.,'Add')]"))

    # Unit Fields
    safe_type(driver, (By.ID, "total-units-input"), "100")
    safe_type(driver, (By.ID, "usable-units-input"), "90")
    safe_type(driver, (By.ID, "purchase-price-input"), "120")

    # Next Step
    safe_click(driver, (By.XPATH, "//button[contains(.,'Next Step')]"))
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Final Step
    safe_click(driver, (By.XPATH, "//button[contains(.,'Available For Listing')]"))
    log_and_print("✅ Product added successfully!")

except Exception as e:
    log_and_print(f"❌ Error during automation: {e}", "error")

finally:
    driver.quit()
    log_and_print("🎯 Script completed & browser closed.")
