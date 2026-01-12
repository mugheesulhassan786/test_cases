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
# 3) Login
# --------------------------
driver.get("https://gamerpc-test.vercel.app/admin/login")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admintest@gmail.com")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------
# 4) Navigate to inventory -> View listing -> Add listing
# ----------------------------------------------------------------------------------------------

inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="3. Inventory"]')))
inventory_section.click()
time.sleep(1.0)

View_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="3.3 View Listing"]')))
View_listing.click()
time.sleep(1.0)

add_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Listing"]')))
add_listing.click()
time.sleep(2)



# Wait for Publish_to_Website and click
Publish_to_Website = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="SwitchCheckWebsite"]')))
Publish_to_Website.click()
time.sleep(1)

# Choose item type
# Choose_Item_Type = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]')))
# Choose_Item_Type.click()
# time.sleep(1)

# # Select category
# select_category = wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="categorySelect"]/div/div[1]/div[2]'))
# )
# select_category.click()

# first_option_danger = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_danger.click()
# time.sleep(2)

# # Select Inventory — with scroll into view fix
# Select_Inventory = wait.until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]'))
# )

# # Scroll into view before clicking
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", Select_Inventory)
# time.sleep(0.5)

# # Wait until clickable, then click
# wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]'))).click()
# Select category
select_category = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="categorySelect"]/div/div[1]/div[2]'))
)
select_category.click()

first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()
time.sleep(7)

# Select Inventory — with scroll into view fix
Select_Inventory = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]'))
)
Select_Inventory.click()

first_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option.click()
time.sleep(2)
# # Scroll into view before clicking
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", Select_Inventory)
# time.sleep(0.5)

# # Wait until clickable, then click
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]'))
# ).click()


#####################################################################
####################################################
############################ ✅ Modal locate karna##################################


modal_container = wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div[1]')
))

# ✅ Modal ke andar scroll karna
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)

Select_Stock = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[3]/div/div/div/div[1]/div[2]'))
)

# Type category
Select_Stock .click()
time.sleep(1)

first_option_option_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_1.click()
time.sleep(1)

create_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Listing"]')))
create_listing.click()

time.sleep(6)

# Product_Condition = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="condition_type"]/div/div[2]/div')))
# Product_Condition.click()
# first_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option.click()
# time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)



button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sku"]')))
button.send_keys("12345")

time.sleep(3)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3)

Proceed_button= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/form/div[2]/button[2]')))
Proceed_button.click()
time.sleep(6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
html.send_keys(Keys.PAGE_UP)
time.sleep(3)


# --- Step 1: Click the Processor field to focus ---
processor_box = driver.find_element(By.XPATH, '(//input[contains(@id, "react-select") and @type="text"])[1]')
processor_box.click()
time.sleep(0.5)

# --- Step 2: Type value (e.g., haserre) ---
processor_box.send_keys("haserre")
time.sleep(1)  # wait for dropdown suggestion to appear

# --- Step 3: Select "Create 'haserre'" from dropdown ---
# Option 1: Press Enter key (if works)
processor_box.send_keys(Keys.ENTER)


Type= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/div/div/div/div[1]/div[2]')))
Type.click()
first_option_option_7 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_7.click()


Model= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]')))
Model.click()
first_option_option_9 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_9.click()

MPN= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter MPN"]')))
MPN.send_keys("dada")


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)


Storage_Type= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-56-input"]')))
Storage_Type.send_keys("123")



Hard_Drive_Capacity= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-63-input"]')))
Hard_Drive_Capacity.send_keys("")

SSD_Capacity= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-71-input"]')))
SSD_Capacity.send_keys("128 GB")


Operating_System= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-57-input"]')))
Operating_System.send_keys("dad")





Release_Year= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-64-input"]')))
Release_Year.send_keys("mom")






colour= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-72-input"]')))
colour.send_keys("Nvidia Ge Force Rtx 5060 - Black")



Features= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-58-input"]')))
Features.send_keys("khan")




Maximum_Resolution= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-65-input"]')))
Maximum_Resolution.send_keys("1280 x 720 ")


GPU= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-73-input"]')))
GPU.send_keys("2160")


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)


Unit_Quantity = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Unit Quantity"]')))
Unit_Quantity.send_keys("hight")



Unit_type = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-66-input"]')))
Unit_type.send_keys("c")
first_option_option_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_1.click()
time.sleep(1)




Most_Suitable_For= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-74-input"]')))
Most_Suitable_For.send_keys("asad")
first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(1)


Manufacturer_Warranty= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-67-input"]')))
Manufacturer_Warranty.send_keys("eye")
first_option_option_3 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_3.click()





Graphics_Processing_Type= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-75-input"]')))
Graphics_Processing_Type.send_keys("280")
first_option_option_4 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_4.click()
time.sleep(1)




Connectivity= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-60-input"]')))
Connectivity.send_keys("fdsfdsfsd")
first_option_option_5 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_5.click()
time.sleep(1)




Country_of_Origin= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-68-input"]')))
Country_of_Origin.send_keys("sdgfvsd")
first_option_option_6 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_6.click()
time.sleep(1)





Item_Height= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Item Height"]')))
Item_Height.send_keys("12")





Item_Weight= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Item Weight"]')))
Item_Weight.send_keys("21")



Item_Weight= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Item Weight"]')))
Item_Weight.send_keys("22")



Series= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-61-input"]')))
Series.send_keys("234")
first_option_option_6 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_6.click()
time.sleep(1)




# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_UP)
# time.sleep(0.6)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_UP)
# time.sleep(3)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)


Proceed_1= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/button')))
Proceed_1.click()
time.sleep(8)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(2)
# ✅ Dropzone ke andar actual input[type="file"] dhundo
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# ✅ Apni file ka full path do (rename karke simple naam rakhna)
file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
upload_input.send_keys(file_path)


# Upload hone ke liye thoda wait
time.sleep(7)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Proceed_2= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[3]/div/form/div[2]/button')))
Proceed_2.click()
time.sleep(6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(2)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Quantity_For_Sale= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[4]/form/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[6]/div/input')))
Quantity_For_Sale.send_keys("10")


#sdfghj

Discount_Type= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="discountType"]/div/div[1]/div[2]'))
)

# Type category
Discount_Type .click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Pricing_Format= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pricingFormat"]/div/div[1]/div[2]'))
)

# Type category
Pricing_Format .click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)


Payment_Policy= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="paymentPolicy"]/div/div[1]/div[2]'))
)

# Type category
Payment_Policy .click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)

# Warranty_Coverage= wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="paymentPolicy"]/div/div[1]/div[2]'))
# )

# # Type category
# Warranty_Coverage.click()

# first_option_option_2 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_option_2.click()
# time.sleep(2)

Warranty_Duration = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="warrantyDuration"]/div/div[1]/div[2]'))
)

# Type category
Warranty_Duration .click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)
first_option_option_2.click()
time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

Proceed_3= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[4]/form/div/div[2]/button')))
Proceed_3.click()
time.sleep(6)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(1)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(1)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(4)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1)

# Postage_Policye= wait.until(By.XPATH,
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]'))
# )

# # Type category
# Postage_Policye.click()

# first_option_option_2 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_option_2.click()
# time.sleep(2)
# Wait for the element to be present
Postage_Policye = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]'))
)

# Now wait until it is clickable
Postage_Policye = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]'))
)

# Click on the element
Postage_Policye.click()

# Select first option
first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)



Item_Display_Weight = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/input')))
Item_Display_Weight.send_keys("2")
time.sleep(1)



# Select_unit= wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div[2]'))
# )

# # Type category

# Select_unit.click()

# first_option_option_2 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_option_2.click()
# time.sleep(2)
# Step 1: Click on dropdown (Select unit)
Select_unit = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div'))
)
Select_unit.click()

# Step 2: Select first option
first_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="option"][1]'))
)
first_option.click()
 
Enable_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div[2]'))
)
Enable_button.click()
time.sleep(2)
Item_Package_Weight = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="item_package_weight_value"]')))
Item_Package_Weight.send_keys("2.5")
time.sleep(2)


Item_Package_Weight = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div'))
)
Item_Package_Weight.click()

# Step 2: Select first option
first_option_0 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="option"][1]'))
)
first_option_0.click()
time.sleep(3)

# Enable_button_2= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[3]/div[1]/div/div[2]'))
# )
# Enable_button_2.click()
# driver.execute_script("window.scrollBy(0, 200);")


# Item_Package_Dimensions



                                        # --- Length ---


# length_input = wait.until(
#     EC.presence_of_element_located((By.NAME, "item_package_dimensions_length_value"))
# )
# length_input.send_keys("14")
# time.sleep(1)

# length_dropdown = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/div'))
# )
# length_dropdown.click()

# length_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@role="option"][2]'))  # first option
# )
# length_option.click()


# # --- Width ---
# width_input = wait.until(
#     EC.presence_of_element_located((By.NAME, "item_package_dimensions_width_value"))
# )
# width_input.send_keys("8.82")
# time.sleep(1)

# width_dropdown = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div[2]'))
# )
# width_dropdown.click()

# width_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@role="option"][2]'))
# )
# width_option.click()


# # --- Height ---
# height_input = wait.until(
#     EC.presence_of_element_located((By.NAME, "item_package_dimensions_height_value"))
# )
# height_input.send_keys("8")
# time.sleep(1)

# height_dropdown = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[3]/div[4]/div[2]/div/div[2]/div'))
# )
# height_dropdown.click()

# height_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@role="option"][2]'))
# )
# height_option.click()

# time.sleep(5)

# driver.execute_script("window.scrollBy(0, 300);")
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

SEO= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[2]/button'))
)
SEO.click()
time.sleep(2)


# Tags input (multiple values with Enter)
Product_SEO = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[6]/form/div/div[1]/div[1]/div[2]/div/div/div[2]/div/span/input')))
Product_SEO.send_keys("automation")
Product_SEO.send_keys(Keys.ENTER)
time.sleep(2)

tags_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[6]/form/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span/input')))
tags_input.send_keys("tester")
tags_input.send_keys(Keys.ENTER)
time.sleep(2)

tags_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[6]/form/div/div[1]/div[3]/div[2]/div/div/div[2]/div/span/input')))
tags_input.send_keys("tester khani ")
tags_input.send_keys(Keys.ENTER)
time.sleep(2)

proceed_to_finish= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[6]/form/div/div[2]/div[2]/button[2]'))
)
proceed_to_finish.click()
time.sleep(6)