import html
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

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


                                  # --------------------------
                                     # Browser options
                                  # --------------------------
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

                                      # --------------------------
                                            # 3) Login 
                                      # --------------------------
driver.get("https://gamerpc-test.vercel.app/admin/login")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admin@gmail.com")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(2)


             # ----------------------------------------------------------------------------------------------

                         # 4) Navigate to inventory -> View product catalogue -> Add product catalogue

             # ----------------------------------------------------------------------------------------------

inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="3. Inventory"]')))
inventory_section .click()
time.sleep(1.0)   


View_stock = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="3.2 View Stock"]')))
View_stock .click()
time.sleep(1.0)    

Add_stock = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
Add_stock.click()
time.sleep(1.0)   

             # ----------------------------------------------------------------------------------------------

                                   # Open new page 

            # ----------------------------------------------------------------------------------------------
                       
product = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//label[@for="products-radio"]'))
)
product.click()
#select_category
select_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[2]/div/div/div/div[1]/div[2]')))
select_category.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
# select_category = wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[2]/div/div/div/div[1]/div[2]'))
# )
# select_category.send_keys("lap")

# # Wait for dropdown options to appear
# time.sleep(1.5)  
# # Move to first option and press Enter (react-select reliable method)
# select_category.send_keys(Keys.ARROW_DOWN)
# select_category.send_keys(Keys.ENTER)

select_product= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[3]/div[1]/div/div[1]/div[2]'))
)
select_product.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()

time.sleep(4)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1.0)
#  supplier_feild

supplier= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="supplier-select"]/div/div[1]/div[2]'))
)
supplier.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)
first_option_danger.click()
time.sleep(2)

#Received_By


Received_By= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="user-select"]/div/div[1]/div[2]'))
)
Received_By.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)
first_option_danger.click()
time.sleep(2)
#//button[@aria-label="Choose dat, selected  is Sep 2, 2025"]
#select Dat

purchase_date= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[6]/div/div/div[2]/button'))
)
purchase_date.click()
time.sleep(2)
purchase_date_enter= wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[5]'))
)
purchase_date_enter.click()
time.sleep(2)




select_date= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[7]/div/div/div[2]/button'))
)
select_date.click()
time.sleep(2)

select_date_1= wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[6]'))
)
select_date_1.click()
time.sleep(2)

# received
# received= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[5]'))
# )
# received.click()
# time.sleep(2)
# select_1= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/button[6]'))
# )
# select_1.click()
# time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1.0)
# Add_expenses 

add_expanses= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[9]/div[1]/div/button[1]'))
)
add_expanses.click()
time.sleep(2)
expenses_button= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="name-0"]/div/div[1]/div[2]'))
)
expenses_button.click()

# Step 2: Wait for first option and click it
first_option_expenses_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_expenses_button.click()
time.sleep(3)

#add value

value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="value-0"]')))
value.send_keys("120")
time.sleep(2)

#add expenses
Add_expenses = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[1]/div/div/div[3]/button')))
Add_expenses.click()
time.sleep(2)  

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1.0)

#Total Units
Total_Units = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="total-units-input"]')))
Total_Units.send_keys("100")
time.sleep(1.0)

#Usable_units
Usable_units = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="usable-units-input"]')))
Usable_units.send_keys("90")
time.sleep(1.0)

#Purchase_Price_Per_Unit

Purchase_Price_Per_Unit = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="purchase-price-input"]')))
Purchase_Price_Per_Unit.send_keys("120")
time.sleep(1.0)



driver.execute_script("window.scrollBy(0, 400);")
time.sleep(1.0)
#click_on_next_step

click_on_next_step = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/button')))
click_on_next_step.click()
time.sleep(3)

#scroll up 

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
#

# available_for_listing= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[2]'))
# )
# available_for_listing.click()

time.sleep(8)