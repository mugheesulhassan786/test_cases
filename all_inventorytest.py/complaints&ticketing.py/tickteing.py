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
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
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
# 4) Navigate to inventory -> View listing -> Add listing
# ----------------------------------------------------------------------------------------------

Complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="8. Complaints & Ticketing"]')))
Complaint .click()
time.sleep(1.0)


                 # ✅ Sidebar ko bottom tak scroll karo



driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Complaint)



                  # ✅ Agar thoda thoda scroll karna ho (step by step)


driver.execute_script("arguments[0].scrollBy(0, 100);", Complaint)  #
View_ticketing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="8.3 View Ticketing"]')))
View_ticketing.click()
time.sleep(1.0)

Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Ticket"]')))
Add_Expense_Category.click()
time.sleep(7)


                            # Titel field

titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Ticket Title"]')))
titel.send_keys("Automation Tester")
time.sleep(2)

                         # Client field
                        

client = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Client Name"]')))
client.send_keys("Tester")
time.sleep(6)                        

                           # Role  field

Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter ticket description (minimum 50 characters)"]')))
Description.send_keys("Complaint has been submitted and will be reviewed for timely resolution."+"")
time.sleep(2)
# # Select category
# Role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/select')))
# Role.click()

# first_option_danger = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/select/option[3]and @role="option"][2]'))
#     )
# first_option_danger.click()
# time.sleep(2)                           
# Dropdown locate karke click karo
# Role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[4]/div[1]/div/div[2]/div')))
# Role.click()

# # Select class ka object banao
# # select = Select(Role)

# # # Second option select karo (index 1, kyunki index 0 se start hota hai)
# # select.select_by_index(2)

# first_option_1 = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
#     )
# first_option_1.click()
# time.sleep(3)
# Click on Role dropdown
# Click on Role dropdown
role_dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[4]/div[1]/div/div[2]/div'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", role_dropdown)
role_dropdown.click()

# Wait for all options to be visible
options = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))
)

# Select 2nd option safely using JavaScript (to avoid intercept error)
driver.execute_script("arguments[0].click();", options[1])
time.sleep(1)

# ...existing code...
# Dropdown locate karke click karo

# ...existing code...

                           # Assigned To



Assigned = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[5]/div/div/div[2]/div')))
Assigned.click()

first_option_danger = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
    )
first_option_danger.click()
time.sleep(3)                           




#####################
# Platform = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="e.g., Amazon, eBay, Shopify"]')))
# Platform.send_keys("web")
# time.sleep(2)



                                    # Status field

# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(6)

# status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[5]/select')))
# status.click()

# select = Select(status)

# # Second option select karo (index 1, kyunki index 0 se start hota hai)
# select.select_by_index(2)


                                   # Priority field 




# Priority = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[6]/select')))
# Priority.click()

# first_option_danger = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
#     )
# first_option_danger.click()
# time.sleep(2)                                     
# select = Select(Priority)

# Second option select karo (index 1, kyunki index 0 se start hota hai)
# select.select_by_index(2)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)

                                          #Platform




Platform = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Order reference number"]')))
Platform.send_keys("12345web")
time.sleep(2)



                           # Order reference field



# Order_Reference= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Order reference number"]')))
# Order_Reference.send_keys("web12345")
# time.sleep(2)


                                 #  Description field


# Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter ticket description (minimum 50 characters)"]')))
# Description.send_keys("Complaint has been submitted and will be reviewed for timely resolution."+"")
# time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)


                             # Date field



Date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[10]/div/div/div[2]/button')))
Date.click()
time.sleep(2)
date_0 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/button[2]')))
date_0.click()
time.sleep(2)


  # Upload file
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
driver.execute_script("arguments[0].style.display = 'block';", upload_input)
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)
time.sleep(2)


# Scroll down
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# done_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[13]/button[2]')))
# done_button.click()
time.sleep(7)



















                            # --------------------------
                           # 50 time loop code  options

                            # --------------------------












# import os
# import html
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time
# import random
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# # --------------------------
# # Browser options
# # --------------------------
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # --------------------------
# # 3) Login
# # --------------------------
# driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
# driver.maximize_window()
# time.sleep(2)

# for _ in range(2):
#     driver.execute_script("window.scrollBy(0, 800);")
#     time.sleep(0.5)

# email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field_login.send_keys("admin@gmail.com")

# password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field_login.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(3)

# # --------------------------
# # Complaint menu click only once
# # --------------------------
# Complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="8. Complaints & Ticketing"]')))
# Complaint.click()
# time.sleep(1)

# # --------------------------
# # LOOP start (50 tickets)
# # --------------------------
# for i in range(1, 51):
#     print(f"▶ Ticket Run: {i}")

#     # View Ticketing
#     View_ticketing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="8.6 View Ticketing"]')))
#     View_ticketing.click()
#     time.sleep(1)

#     Add_Expense_Category = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Ticket"]'))
#     )
#     Add_Expense_Category.click()
#     time.sleep(1)

#     # Titel field
#     titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Ticket Title"]')))
#     titel.send_keys(f"Automation Tester {i}")
#     time.sleep(2)

#     # Client field
#     client = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Client Name"]')))
#     client.send_keys(f"Tester {i}")
#     time.sleep(6)

#     # Role field
#     Role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div')))
#     Role.click()
#     time.sleep(6)
#     select = Select(Role)
#     select.select_by_index(2)

#     # Assigned To
#     Assigned = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[4]/div[1]/div/div[1]/div[2]')))
#     Assigned.click()
#     time.sleep(2)
#     first_option_danger = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
#     )
#     first_option_danger.click()
#     time.sleep(2)

#     # Status field
#     status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[5]/select')))
#     status.click()
#     time.sleep(2)
#     select = Select(status)
#     select.select_by_index(2)

#     # Priority field
#     Priority = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[6]/select')))
#     Priority.click()
#     time.sleep(2)
#     select = Select(Priority)
#     select.select_by_index(2)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(2)

#     # Platform
#     Platform = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="e.g., Amazon, eBay, Shopify"]')))
#     Platform.send_keys("web automation")
#     time.sleep(2)

#     # Order reference
#     Order_Reference = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Order reference number"]')))
#     Order_Reference.send_keys(f"REF-{i}-{random.randint(1000,9999)}")
#     time.sleep(2)

#     # Description
#     Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter ticket description (minimum 50 characters)"]')))
#     Description.send_keys(f"Complaint {i} has been submitted and will be reviewed for timely resolution and QA validation.")
#     time.sleep(2)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(2)

#     # Date field
#     Date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[11]/div/div/div[2]/button')))
#     Date.click()
#     time.sleep(2)
#     date_0 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/button[3]')))
#     date_0.click()
#     time.sleep(2)

#     # Upload file
#     upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
#     driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
#     driver.execute_script("arguments[0].style.display = 'block';", upload_input)
#     file_path = "./img/Image_1.png"
#     upload_input.send_keys(file_path)
#     time.sleep(2)

#     # Scroll down
#     html = driver.find_element(By.XPATH, "/html")
#     html.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

#     # done_button = wait.until(
#     #     EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[13]/button[2]'))
#     # )
#     # done_button.click()
#     time.sleep(3)

#     print(f"✅ Ticket {i} created successfully!\n")

# print("🎉 All 50 tickets created successfully!")
