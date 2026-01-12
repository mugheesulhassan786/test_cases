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
email_field_login.send_keys("admin@gmail.com")
print("🎉 1 Script execution complete")
password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("Bmr@1234")
print("🎉 2 Script execution complete")
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(2)
print("🎉 3 Script execution complete")

             # ----------------------------------------------------------------------------------------------

                         # 4) Navigate to inventory -> View product catalogue -> Add product catalogue

             # ----------------------------------------------------------------------------------------------

inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="3. Inventory"]')))
inventory_section .click()
time.sleep(1)   
print("🎉 4 Script execution complete")

View_Product_Catalogue = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="3.1 View Product Catalogue"]')))
View_Product_Catalogue .click()
time.sleep(1)             
print("🎉 5 Script execution complete")
inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
inventory_section .click()
time.sleep(1)   
print("🎉 6 Script execution complete")   
             # ----------------------------------------------------------------------------------------------

                                   # Open new page 

            # ----------------------------------------------------------------------------------------------
                       
# part = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//label[@for="partRadio"]'))
# )
# part.click()


# input_box = wait.until(
#     EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-5-input"]'))
# )
# input_box.send_keys("cr")

# Wait for dropdown options to appear
time.sleep(1.5)   # dropdown render hone ka chhota delay
print("🎉 7 Script execution complete")
# Move to first option and press Enter (react-select reliable method)
# input_box.send_keys(Keys.ARROW_DOWN)
# input_box.send_keys(Keys.ENTER)

time.sleep(1)  # ensure selection ho jaye

# Submit form
submit_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue"]'))
)
submit_button.click()
time.sleep(2)
print("🎉 8 Script execution complete")
             # ----------------------------------------------------------------------------------------------

                                          #basic info 

            # ----------------------------------------------------------------------------------------------

time.sleep(5)
# Click to open dropdown
product_catagory = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="productCategory"]'))
)
product_catagory.click()

print("🎉 9 Script execution complete")
# Find the actual input box inside react-select
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="productCategory"]//input'))
)

# Type value
input_box.send_keys("gaming pc")
time.sleep(1.5)   # dropdown render hone ka chhota delay

# Select first option
# input_box.send_keys(Keys.ARROW_DOWN)
input_box.send_keys(Keys.ENTER)

                                                 # option 2
print("🎉 10 Script execution complete")
# Click to open dropdown
# Product_Condition = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
# )
# Product_Condition.click()
# Click to open dropdown (Product Condition)
Product_Condition = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
)
Product_Condition.click()

# Find the actual input box inside react-select (under productCondition)
input_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="condition_type"]//input'))
)
input_box.send_keys("new")

# Select first option
input_box.send_keys(Keys.ARROW_DOWN)
input_box.send_keys(Keys.ENTER)
time.sleep(2.0)
print("🎉 11 Script execution complete")
                              # part titel
Product_Title = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@id="item_name"]'))
)
Product_Title.send_keys("Corsair RM750x Fully Modular Power Supply 750W, 80 Plus Gold ")
time.sleep(2.0)
print("🎉 12 Script execution complete")
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
                                    #Brand

# Wait for Brand input box
Brand = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="brand"]/div[1]/div[2]/div'))
)

# Type the brand
Brand.click()
time.sleep(1)
# Step 2: Wait for first option and click it
first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(1)   # thoda wait do taake dropdown load ho

# Select the first option from dropdown
# Brand.send_keys(Keys.ARROW_DOWN)
# Brand.send_keys(Keys.ENTER)

time.sleep(1)
print("🎉 13 Script execution complete")
# Thoda neeche scroll (200px)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(0.6)

# Aur neeche scroll karna ho to aur run kar lo
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(0.6)


                                


Part_Description = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="textbox"]'))
)
Part_Description .send_keys("High-performance fully modular PSU with low noise fan and reliable Japanese capacitors for long-lasting performance. ")
time.sleep(2)
print("🎉 14 Script execution complete")
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# # ✅ Dropzone ke andar actual input[type="file"] dhundo
# upload_input = wait.until(EC.presence_of_element_locatepyinstaller-d((By.XPATH, '//input[@type="file"]')))

# # Agar input hidden hai to visible karo
# driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
# driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# # ✅ Apni file ka full path do (newline '\n' se separate karo)
# file_path = (
#     r"C:\Users\M Yunas Khan\Downloads\81jz31K29fL._AC_SX67..._imresizer.png\n"
#     r"C:\Users\M Yunas Khan\Downloads\81CCoo68oyL._AC_SX67..._imresizer.png\n"
#     r"C:\Users\M Yunas Khan\Downloads\71lXNxuvvnL._AC_SX67..._imresizer.png"
# )

# upload_input.send_keys(file_path)

# Upload hone ke liye thoda wait
# time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Add_Supplier_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Proceed to Technical Info"]')))
Add_Supplier_Category.click()
time.sleep(6)
print("add supplier button done")

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(1 )
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3 )

Brand_Recommended_Browse_Nodes = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="12345678"]'))
)

# Type the brand
Brand_Recommended_Browse_Nodes.send_keys("10971181011 ")

time.sleep(1) 
Bullet_Point= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Breathable leather lining, Classic look and feel"]'))
)
Bullet_Point.send_keys("Fully modular design for easy cable management")
time.sleep(1)

driver.execute_script("window.scrollBy(200, 0);")
time.sleep(1)

# Output_Wattage= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="800"]'))
# )
# Output_Wattage.send_keys("200")
# time.sleep(1)


# # Step 1: Click the container to activate the dropdown
# container = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div')))
# container.click()


# first_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
# )
# first_option.click()
# time.sleep(2)

# # driver.execute_script("window.scrollBy(0, 200);")
# # time.sleep(2)



#     #########################################################################
#             ################# DONE HAIN YAHA TAK #############
#     #########################################################################


# Form_Factor= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Stand alone, Plastic, Upholstered"]'))
# )
# Form_Factor.send_keys("stand alone")
# time.sleep(1)
# print("🎉 1 Script execution complete")

# ################################
# Maximum_Power= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="100"]'))
# )
# Maximum_Power.send_keys("100")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)

# print("🎉 2 Script execution complete")



# # # Step 1: Find the input box
# Maximum_Power_Unit= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]')))
# Maximum_Power_Unit.click()
# print("🎉 3 Script execution complete")

# # Step 2: Wait for first option and click it
# first_option_danger = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
# )
# first_option_danger.click()
# time.sleep(1)
# print("🎉 4 Script execution complete")

# #####################################
# # Step 1: Find the input box
# Output_Voltage= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="120"]')))
# Output_Voltage.send_keys("150")
# time.sleep(1)
# print("🎉 5 Script execution complete")

# Output_Voltage= wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]')))
# Output_Voltage.click()
# # Step 2: Wait for first option and click it
# first_option_type0 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_type0.click()
# print("🎉 6 Script execution complete")

# ###################################
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)

Country_of_Origin= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[5]/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div')))
Country_of_Origin.click()
time.sleep(6)
# Step 2: Wait for first option and click it
first_option_type1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_type1.click()
print("🎉 7 Script execution complete")
#############################################
time.sleep(3)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)

driver.execute_script("window.scrollBy(0, 200);")

# Dangerous_Goods_Regulations= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]')))
# Dangerous_Goods_Regulations.click()
# time.sleep(3)
# # Step 2: Wait for first option and click it
# first_option_type1 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
# )
# first_option_type1.click()
# print("🎉 8 Script execution complete")

# Step 1: Click on Dangerous Goods Regulations dropdown
Dangerous_Goods_Regulations = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div'))
)

# Scroll element into view before clicking (prevents interception)
driver.execute_script("arguments[0].scrollIntoView(true);", Dangerous_Goods_Regulations)
time.sleep(1)

# Click dropdown
Dangerous_Goods_Regulations.click()
time.sleep(1)

# Step 2: Wait for the dropdown option to appear and click it
first_option_type1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", first_option_type1)
time.sleep(1)
first_option_type1.click()

print("🎉 Step 8: Script execution complete ✅")


html = driver.find_element(By.XPATH, "/html")


html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)



Type= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div/div/div/div/div[2]/div')))
Type.click()
time.sleep(6)
# Step 2: Wait for first option and click it
first_option_type1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_type1.click()
print("🎉 9 Script execution complete")



html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)


show_button= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Show all fields"]')))
show_button.click()

## ya ha tak code theak chal raha hain 


html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)





#################################
Merchant_Suggested_ASIN = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div/div/button')))
Merchant_Suggested_ASIN.click()
# time.sleep(6)//*[@placeholder="B007KQBXN0"]
Merchant_Suggested_ASIN_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="B007KQBXN0"]')))
Merchant_Suggested_ASIN_1.send_keys("khani")

print("box number 1")


Model_Number= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[3]/div/div/div/button')))
Model_Number.click()

Model_Number_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="RXZER23, 123"]')))
Model_Number_1.send_keys("khani1")
  

print("box number 2 ")  




Model_Name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div/div/div/button')))
Model_Name.click()
# time.sleep(6)//*[@placeholder="B007KQBXN0"]
Model_Name_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Juliet, MacBook Pro, Rebel, iPhone, Xbox One"]')))
Model_Name_1.send_keys("khani2")
####################################




Manufacturer = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[4]/div/div/div/button')))
Manufacturer.click()
# time.sleep(6)//*[@placeholder="B007KQBXN0"]
Manufacturer_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Nike, Procter & Gamble"]')))
Manufacturer_1.send_keys("khani3")
####################################





# Connectors= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[4]/div/div/div[1]/div/div[1]/div[2]')))
# Connectors.click()
# time.sleep(6)
# # Step 2: Wait for first option and click it
# first_option_type1 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_type1.click()
# print("🎉 10 Script execution complete")

###################################

# done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Proceed to Finish"]')))
# done_btn.click()
# time.sleep(6)
# #################
# print("🎉 11 Script execution complete")

# done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Done"]')))
# done_btn.click()
# time.sleep(6)
# print("🎉 12Script execution complete")
# show_all_fields = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Show all fields"]')))
# show_all_fields .click()
# time.sleep(1.0)    
   # ----------------------------------------------------------------------------------------------

                                   # view stock

            # ----------------------------------------------------------------------------------------------


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
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[1]/div/div[2]'))
)
product.click()
#select_category
# select_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[2]/div/div/div/div[1]/div[2]')))
# select_category.click()

# # Step 2: Wait for first option and click it
# first_option_danger = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_danger.click()


# Step 1: Click on the box to open dropdown
select_category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[2]/div/div/div/div[1]/div[2]'))
)
select_category.click()

# Step 2: Type value in the hidden input
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//input[contains(@id,"react-select") and @type="text"]'))
)
input_box.send_keys("pow")

# Step 3: Wait for dropdown and click first option
first_option_type1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_type1.click()




# Find the actual input box inside react-select
# input_box = wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[2]/div/div/div/div[1]/div[2]'))
# )

# # Type value
# input_box.send_keys("po")
# time.sleep(1.5)   # dropdown render hone ka chhota delay

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
driver.execute_script("window.scrollBy(0, 400);")
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
#//button[@aria-label="Choose date, selected date is Sep 2, 2025"]
#select Date

purchase_date= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[6]/div/div/div[2]/button'))
)
purchase_date.click()
time.sleep(2)
select_date= wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/button[4]'))
)
select_date.click()
time.sleep(2)

#received_date
received_date= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div/div[7]/div/div/div[2]/button'))
)
received_date.click()
time.sleep(2)
select_date_1= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[text()="14"]'))
)
select_date_1.click()
time.sleep(2)

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
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)
first_option_expenses_button.click()
time.sleep(3)

#add value

value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="value-0"]')))
value.send_keys("120")
time.sleep(2)

#add expenses
Add_expenses = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button')))
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

available_for_listing= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[2]'))
)
available_for_listing.click()

time.sleep(6)

             # ----------------------------------------------------------------------------------------------

                                          # view listing

             # ----------------------------------------------------------------------------------------------



View_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="3.3 View Listing"]')))
View_listing.click()
time.sleep(1.0)

add_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button/i')))
add_listing.click()
time.sleep(2)



Publish_to_Website = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="SwitchCheckWebsite"]')))
Publish_to_Website.click()
time.sleep(1.0)
time.sleep(3)

Choose_Item_Type = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]')))
Choose_Item_Type.click()
time.sleep(1.0)

# ✅ Modal locate karna
modal_container = wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div[1]')
))

# ✅ Modal ke andar scroll karna
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)


# Step 1: Click dropdown
select_category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="categorySelect"]/div/div[2]/div'))
)
select_category.click()

# Step 2: Type inside actual input
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="categorySelect"]//input[@type="text"]'))
)
input_box.send_keys("pow")

# Step 3: Select first option
first_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '(//div[contains(@id,"react-select") and @role="option"])[1]'))
)
first_option.click()
time.sleep(2)




Select_Inventory  = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2] '))
)

# Type category
Select_Inventory .click()
time.sleep(1)

first_option_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option.click()
time.sleep(1)

# ✅ Modal locate karna
modal_container = wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div[1]')
))

# ✅ Modal ke andar scroll karna
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500;", modal_container)
time.sleep(1)

Select_Stock = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[3]/div/div/div/div[1]/div[2]'))
)

# Type category
Select_Stock .click()
time.sleep(1)

first_option_option_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_1.click()
time.sleep(1)

create_listing = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/div/div[4]/button')))
create_listing.click()

time.sleep(6)
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

Proceed= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/form/div[2]/button[2]')))
Proceed.click()
time.sleep(6)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(3)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)


Proceed_1= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/button')))
Proceed_1.click()
time.sleep(3)

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
time.sleep(2)

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
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][4]'))
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
time.sleep(1)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

Postage_Policye= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]'))
)

# Type category
Postage_Policye.click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)



Item_Display_Weight = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/input')))
Item_Display_Weight.send_keys("2")
time.sleep(1)



Select_unit= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[5]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div[2]'))
)

# Type category

Select_unit.click()

first_option_option_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_option_2.click()
time.sleep(2)                                          