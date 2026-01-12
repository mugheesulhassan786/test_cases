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

                         # 4) Navigate to inventory -> View product catalogue -> Add product catalogue

             # ----------------------------------------------------------------------------------------------

inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="3. Inventory"]')))
inventory_section .click()
time.sleep(1.0)   


View_Product_Catalogue = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="3.1 View Product Catalogue"]')))
View_Product_Catalogue .click()
time.sleep(1.0)             

inventory_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
inventory_section .click()
time.sleep(1.0)      
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
# time.sleep(1.5)   # dropdown render hone ka chhota delay

# # Move to first option and press Enter (react-select reliable method)
# input_box.send_keys(Keys.ARROW_DOWN)
# input_box.send_keys(Keys.ENTER)

# time.sleep(1)  # ensure selection ho jaye

# Submit form
submit_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="px-4 btn btn-primary btn-md"]'))
)
submit_button.click()
time.sleep(6)
 
             # ----------------------------------------------------------------------------------------------

                                          #basic info 

            # ----------------------------------------------------------------------------------------------


# Click to open dropdown
product_catagory = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="productCategory"]'))
)
product_catagory.click()

# Find the actual input box inside react-select
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="productCategory"]//input'))
)

# Type value
input_box.send_keys("lap")
time.sleep(1.5)   # dropdown render hone ka chhota delay

# Select first option
input_box.send_keys(Keys.ARROW_DOWN)
input_box.send_keys(Keys.ENTER)

                                                 # option 2

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

                              # part titel
Part_Title = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@id="item_name"]'))
)
Part_Title.send_keys("My Digital Partner Speed Beast  Innovation Hub ")
time.sleep(2.0)


                                    #Brand

# Wait for Brand input box
Brand = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@id="react-select-10-input"]'))
)

# Type the brand
Brand.send_keys("Apple")
time.sleep(1)   # thoda wait do taake dropdown load ho

# Select the first option from dropdown
Brand.send_keys(Keys.ARROW_DOWN)
Brand.send_keys(Keys.ENTER)

time.sleep(1)

# Thoda neeche scroll (200px)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(0.6)

# Aur neeche scroll karna ho to aur run kar lo
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(0.6)


                                #


Part_Description = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="textbox"]'))
)
Part_Description .send_keys("A powerful companion designed to handle everything from coding and designing to entertainment and learning. With speed, reliability, and style, this laptop is not just a machine but a hub of creativity, productivity, and innovation – always ready to support me in every task, anywhere, anytime. ")
time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# ✅ Dropzone ke andar actual input[type="file"] dhundo
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# ✅ Apni file ka full path do (rename karke simple naam rakhna)
file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
upload_input.send_keys(file_path)


# Upload hone ke liye thoda wait
time.sleep(3)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

Add_Supplier_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Proceed to Technical Info"]')))
Add_Supplier_Category.click()
Add_Supplier_Category.click()

time.sleep(6)
print("click on proced to technical info button done")

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(1)
print("scroll up done")
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_UP)
time.sleep(1)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(6)

Brand_Recommended_Browse_Nodes = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="12345678"]'))
)

# Type the brand
Brand_Recommended_Browse_Nodes.send_keys(" Electronics ")

time.sleep(1) 
Bullet_Point= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Breathable leather lining, Classic look and feel"]'))
)
Bullet_Point.send_keys("bullet 1")
time.sleep(1)


#processor description


processor_description= wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Intel Pentium, BIONZ, EXR Processor II"]'))
)
processor_description.send_keys("intel pentium")
time.sleep(1)



driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)


# Step 1: Click the container to activate the dropdown
country_of_origin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div')))
country_of_origin.click()


first_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option.click()
time.sleep(2)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1 )


# Step 1: Find the input box
Dangerous_Goods_Regulations = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-14-input"]')))
Dangerous_Goods_Regulations.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
)
first_option_danger.click()

# Step 1: Find the input box
# type_0 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div[2]')))
# type_0.click()

# # Step 2: Wait for first option and click it
# first_option_type0 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_type0.click()
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)




show_button= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Show all fields"]')))
show_button.click()



time.sleep(2)

Merchant_Suggested_ASIN= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div/div/button')))
Merchant_Suggested_ASIN.click()
Merchant_Suggested_ASIN_1= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="B007KQBXN0"]')))
Merchant_Suggested_ASIN_1.send_keys("khani")


##################


# ##############################

Model_Name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div/div/div/button')))
Model_Name.click()
Model_Name_2= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Juliet, MacBook Pro, Rebel, iPhone, Xbox One"]')))
Model_Name_2.send_keys("macbook pro")

######################################



Manufacturer= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[4]/div/div/div/button')))
Manufacturer.click()
Manufacturer_3= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Nike, Procter & Gamble"]')))
Manufacturer_3.send_keys("nike")

##############################3

Model_Year= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[4]/div/div/div/button')))
Model_Year.click()
Model_Year_4= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="2018"]')))
Model_Year_4.send_keys("2022")
time.sleep(3)

#####################################

Fulfillment_Availabilityr= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[4]/div/div/div/button')))
Fulfillment_Availabilityr.click()
# Fulfillment_Availabilityr_5= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="2018"]')))
# Fulfillment_Availabilityr_5.send_keys("2022")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)


Number_of_Items= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[8]/div/div/div/button')))
Number_of_Items.click()
Number_of_Items_6= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="1, 5, 20"]')))
Number_of_Items_6.send_keys("12")
# next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-label nexttab"]')))
# next_btn.click()
# time.sleep(2)

Display_Colour_Support= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[8]/div/div/div/button')))
Display_Colour_Support.click()

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
Screen_Size= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[8]/div/div/div/div/div[2]/div[4]/div/div/div/button')))
Screen_Size.click()


Screen_Size_7= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="75, 150, 5"]')))
Screen_Size_7.send_keys("27")

driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)

Display_Type= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[8]/div/div/div/div/div[2]/div[6]/div/div/div/button')))
Display_Type.click()
Display_Type.click()
time.sleep(2)
Display_Type_8= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Digital, Analogue, LCD"]')))
Display_Type_8.send_keys("digital")






Graphics_Description= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[11]/div/div/div/button')))
Graphics_Description.click()
time.sleep(2)
Graphics_Description_9= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Dedicated"]')))
Graphics_Description_9.send_keys("description")

time.sleep(2)
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)

Video_Processor= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[10]/div/div/div/button')))
Video_Processor.click()
time.sleep(4)
Graphics_Processor_Manufacturer_10= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Dedicated"]')))
Graphics_Processor_Manufacturer_10.send_keys("itel")

driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)
#########################################################
Processor_Count= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[13]/div/div/div/button')))
Processor_Count.click()
time.sleep(2)
Processor_Count_11= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="1, 2, 3"]')))
Processor_Count_11.send_keys("1")

time.sleep(2)   
##############################
Operating_Systems= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[22]/div/div/div/button')))
Operating_Systems.click()
time.sleep(2)
Operating_Systems_12= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Mac OS X 10.13 High Sierra, Windows 10 Home"]')))
Operating_Systems_12.send_keys("1")




Accepted_Voltage_Frequency= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[20]/div/div/div/button')))
Accepted_Voltage_Frequency.click()
time.sleep(2)
# Accepted_Voltage_Frequency_13= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Mac OS X 10.13 High Sierra, Windows 10 Home"]')))
# Accepted_Voltage_Frequency_13.send_keys("1")

#########################################


Ram_Memory= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[25]/div/div/div/button')))
Ram_Memory.click()
time.sleep(2)
RAM_Memory_Installed_14= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[25]/div/div/div/div/div[2]/div[1]/div/div/div/button')))
RAM_Memory_Installed_14.click()
RAM_Memory_Installed_14= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="8.0"]')))
RAM_Memory_Installed_14.send_keys("16")
print("ram memory installed done")
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)
##################################



Ram_Memory_Maximum_Size= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[25]/div/div/div/div/div[2]/div[2]/div/div/div/button')))
Ram_Memory_Maximum_Size.click()
time.sleep(2)
Ram_Memory_Maximum_Size= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="8.0"]')))
Ram_Memory_Maximum_Size.send_keys("46")

###########################################################


driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)


RAM_Memory_Technology= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[25]/div/div/div/div/div[2]/div[3]/div/div/div/button')))
RAM_Memory_Technology.click()
time.sleep(2)
RAM_Memory_Technology= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="DDR3"]')))
RAM_Memory_Technology.send_keys("DDR4")

#######################################


html.send_keys(Keys.PAGE_UP)
time.sleep(1)

Power_Plug_Type= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[20]/div/div/div/button')))
Power_Plug_Type.click()
time.sleep(2)
# RAM_Memory_Technology_1= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="DDR3"]')))
# RAM_Memory_Technology_1.send_keys("DDR4")


html.send_keys(Keys.PAGE_DOWN)
time.sleep(1)


##########################################



Graphics_Card_Interface= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[23]/div/div/div/button')))
Graphics_Card_Interface.click()
time.sleep(2)

################################

Graphics_Ram= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[29]/div/div/div/button')))
Graphics_Ram.click()
time.sleep(2)
Graphics_Ram_type= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/div[29]/div/div/div/div/div[2]/div[2]/div/div/div/button')))
Graphics_Ram_type.click()
time.sleep(2)

##################################################


Specific_Uses_For_Product= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div[27]/div/div/div/button')))
Specific_Uses_For_Product.click()
time.sleep(2)
Specific_Uses_For_Product= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Business, Gaming, Personal"]')))
Specific_Uses_For_Product.send_keys("gamming")


############################################

Flash_Memory_Installed_Size_in_MB= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[29]/div/div/div/button')))
Flash_Memory_Installed_Size_in_MB.click()
time.sleep(2)
Flash_Memory_Installed= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[29]/div/div/div/div/div[2]/div/div/div/div/button')))
Flash_Memory_Installed.click()
time.sleep(2)

Flash_Memory_Installed= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="flash_memory[0].installed_size[0].value"]')))
Flash_Memory_Installed.send_keys("8")

# ...existing code...

# from selenium.common.exceptions import ElementClickInterceptedException

# try:
#     # Button jo dropdown open karta hai
#     display_btn = wait.until(EC.element_to_be_clickable((
#         By.XPATH,
#         '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[8]/div/div/div/div/div[2]/div[6]/div/div/div/button'
#     )))

#     # ensure in view and no overlay blocking
#     driver.execute_script("arguments[0].scrollIntoView({block:'center'});", display_btn)
#     wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal, .modal-backdrop, .overlay, .spinner")))

#     # try normal click, fallback to JS click if intercepted
#     try:
#         display_btn.click()
#     except ElementClickInterceptedException:
#         driver.execute_script("arguments[0].click();", display_btn)

#     # now the input inside the dropdown (use clickable)
#     display_input = wait.until(EC.element_to_be_clickable((
#         By.XPATH,
#         '//*[@placeholder="Digital, Analogue, LCD"]'
#     )))
#     display_input.clear()
#     display_input.send_keys("digital")

# except Exception as e:
#     print("Display type click failed:", e)

# # ...existing code...


# Add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Done"]')))
# Add_btn.click()
time.sleep(9)
print("🎉 Script execution complete")