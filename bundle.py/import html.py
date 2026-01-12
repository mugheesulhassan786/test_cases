import html
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
# Helper function for dropdowns
# --------------------------
def select_from_dropdown(dropdown_xpath, value):
    # Click on dropdown
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
    time.sleep(1)

    # Type in react-select input
    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id,"react-select")]'))
    )
    input_box.send_keys(value)
    time.sleep(1)

    # Select first option
    first_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
    )
    first_option.click()
    time.sleep(1)

                                      # --------------------------
                                            # 3) Login 
                                      # --------------------------
driver.get("https://admin.buildmyrig.co.uk/admin/login")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admin@gmail.com")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("BuildMyRig@123!")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(2)

bundles = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-nav"]/li[5]/a/span')))
bundles.click()

Add_bundle = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button/i')))
Add_bundle.click()
time.sleep(2)

Bundle_Name  = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="e.g., Gaming PC Bundle"]')))
Bundle_Name.send_keys("gamming PC b")

select_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="products-radio"]')))
select_field.click()
time.sleep(2)

# ✅ Use helper function for category
select_from_dropdown('//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[1]/div[2]', "ga")


driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)


# Step 1: Find the input box
danger = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div/div/div/div[1]/div[2]')))
danger.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()

# Add_product = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[2]/button')))
# Add_product.click()
time.sleep(3)
# Step 1: Find the input box
select_stock = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div[2]/div/div/div[1]/div[2]')))
select_stock.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()


time.sleep(3)

driver.execute_script("window.scrollBy(0, 100);")
time.sleep(1)
# Bundle_Name  = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[1]/div[2]/input')))
# Bundle_Name.send_keys("55")
# time.sleep(4)

# Find the field
Bundle_Name  = wait.until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[1]/div[2]/input'
)))

# Clear existing value
Bundle_Name.clear()

# Send new value
Bundle_Name.send_keys("55")
time.sleep(2)

add_product  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[2]/div/button ')))
add_product.click()
time.sleep(5)

# One product is uploaded sufly

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(2 )
# from selenium.webdriver.common.keys import Keys

# ✅ Clear aur new value enter
# Bundle_Name  = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="bundleName"]')))
# Bundle_Name.send_keys(Keys.CONTROL + "a")
# Bundle_Name.send_keys(Keys.DELETE)
# Bundle_Name.send_keys("memory card")
# time.sleep(2)

# ✅ Click "parts" and "products"
# part = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="parts-radio"]')))
# part.click()
# time.sleep(2)

# ✅ Click "parts" radio button
part_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="parts-radio"]')))
part_label.click()
time.sleep(4)

# # ✅ Ensure "parts" input is actually selected
# part_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="parts-radio"]')))
# if not part_input.is_selected():
#     driver.execute_script("arguments[0].click();", part_input)  # force via JS
# time.sleep(1)

# select_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="products-radio"]')))
# select_field.click()
# time.sleep(2)

# # ✅ Custom dropdown select
# def select_from_dropdown(xpath, value):
#     # Step 1: Click the dropdown
#     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#     dropdown.click()
#     time.sleep(1)

#     # Step 2: Type search value
#     dropdown.send_keys(value) 
#     time.sleep(1)

#     # Step 3: Wait for options to appear
#     options = wait.until(EC.presence_of_all_elements_located(
#         (By.XPATH, '//div[contains(@id,"react-select") and @role="option"]')
#     ))

#     if len(options) == 0:
#         raise Exception("⚠️ No options found in dropdown")

#     # Step 4: Click first option
#     options[0].click()
#     time.sleep(1)

# # ✅ Call helper
# select_from_dropdown(
#     '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[1]/div[2]',
#     "memo"
# )

# driver.execute_script("window.scrollBy(0, 100);")
# time.sleep(5)
# ✅ input field find karo (placeholder ya xpath se)
# input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[1]/div[2]')))

# # ✅ pehle clear karo
# input_box.clear()

# # ✅ fir send_keys karo
# input_box.send_keys("")

# ✅ Step 1: dropdown input find karo
# ✅ Step 2: ab uske andar ka input box lo
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[contains(@id,"react-select") and @type="text"]'
)))
input_box.send_keys("mous")   # text type karo
time.sleep(1)

# ✅ Step 3: first option wait & click
first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
)))
first_option.click()
time.sleep(2)

# # Step 1: Select part
# select_part = wait.until(EC.presence_of_element_located((
#     By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div/div/div/div[1]/div[2]'
# )))
# select_part.send_keys("ra")
# time.sleep(1)
# Step 1: Click on the dropdown/input field
target_field = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div/div/div/div[1]/div[2]'
)))
target_field.click()
time.sleep(1)

# Step 2: Click on the first option that appears
first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
)))
first_option.click()
time.sleep(1)

# # Step 2: Click first option for part
# first_option_part = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
# )))
# first_option_part.click()
# time.sleep(2)
target_field_2 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div[2]/div/div/div[1]/div[2]'
)))
target_field_2.click()
time.sleep(1)

# Step 2: Click on the first option that appears
first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
)))
first_option.click()
time.sleep(3)


# # Step 3: Select stock
# select_stock = wait.until(EC.presence_of_element_located((
#     By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div/div[2]/div/div/div[1]/div[2]'
# )))
# select_stock.send_keys("bat")
# time.sleep(1)

# # Step 4: Click first option for stock
# first_option_stock = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
# )))
# first_option_stock.click()
# time.sleep(2)

Bundle_Name_1  = wait.until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[1]/div[2]/input'
)))

# Clear existing value
Bundle_Name_1.clear()

# Send new value
Bundle_Name_1.send_keys("190")
time.sleep(2)

add_product  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/div[2]/div[2]/div/button ')))
add_product.click()
time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3 )
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3 )
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3 )

Add_bundle_button  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[9]/button[2]')))
Add_bundle_button.click()
time.sleep(7)
