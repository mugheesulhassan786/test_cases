"""
======================================================
   🔒 PRIVATE AUTOMATION SCRIPT 🔒
   Author: YOUSAF LIAQUAT ALI KHAN
   Note: This script is written by YOUSAF LIAQUAT ALI KHAN only.
   Do not copy, modify, or reuse without permission.
======================================================
"""

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
                                               # 2) Browser Setup
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
time.sleep(7)

# --------------------------
# 4) Navigate to Users -> View Users -> Add User

# --------------------------

# Sidebar locate karo
sidebar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]'))
)

# ✅ Sidebar ko bottom tak scroll karo
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# ✅ Agar thoda thoda scroll karna ho (step by step)
driver.execute_script("arguments[0].scrollBy(0, 100);", sidebar)  # 200px 

HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="10. HR Management"]')))
HR_Management.click()
time.sleep(2)

# Sidebar locate karo
# sidebar = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]'))
# )

# # ✅ Sidebar ko bottom tak scroll karo
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# # ✅ Agar thoda thoda scroll karna ho (step by step)
# driver.execute_script("arguments[0].scrollBy(0, 50);", sidebar)  # 200px 


view_Document = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.8 Manage Documents"]')))
view_Document.click()
time.sleep(2)
Add_Document = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Document"]')))
Add_Document.click()
time.sleep(4)

target_field = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="docCategory"]/div/div[1]/div[2]'
)))
target_field.click()
time.sleep(1)

# Step 2: Click on the first option that appears
first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
)))
first_option.click()
time.sleep(3)
#//*[@placeholder="Document Author"]

# ✅ Step 1: Wait for input field to be clickable
Bundle_Name_1 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@placeholder="Document Author"]'
)))

# ✅ Step 2: Clear using CTRL + A + DELETE
Bundle_Name_1.send_keys(Keys.CONTROL + "a")
Bundle_Name_1.send_keys(Keys.DELETE)
time.sleep(1)

# ✅ Step 3: Send new value
Bundle_Name_1.send_keys("YOUSAF KHAN")
time.sleep(2)

# ✅ Step 1: Wait for input field to be clickable
Bundle_Name_2 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//input[@placeholder="Document Title"]'
)))

# ✅ Step 3: Send new value
Bundle_Name_2.send_keys("automation tester")
time.sleep(2)

# ✅ Step 1: Wait for input field to be clickable
Bundle_Name_3 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//input[@placeholder="Document Version"]'
)))

# ✅ Step 3: Send new value
Bundle_Name_3.send_keys("0.3")
time.sleep(2)
# ✅ Step 1: Wait for input field to be clickable
Bundle_Name_4 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//input[@class="react-tagsinput-input"]'
)))

# ✅ Step 2: Send new value + press Enter
Bundle_Name_4.send_keys("automation")
Bundle_Name_4.send_keys(Keys.ENTER)   # 👈 Enter key press
time.sleep(2)
Bundle_Name_4 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//input[@class="react-tagsinput-input"]'
)))

# ✅ Step 2: Send new value + press Enter
Bundle_Name_4.send_keys("tester")
Bundle_Name_4.send_keys(Keys.ENTER)   # 👈 Enter key press
time.sleep(2)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2 )
# ✅ Step 1: File input locate karo
upload_input = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[@type="file"]'
)))

# ✅ Step 2: Apni file ka path bhejo
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)

time.sleep(3)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)


Filter_by_Roles = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[6]/div/div[1]/div/div/div[1]/div[2]')))
Filter_by_Roles.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][5]'))
)
first_option_danger.click()


time.sleep(3)

# Select_Users= wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[6]/div/div[2]/div/div/div[1]/div[2]'
# )))
# Select_Users.click()
# time.sleep(1)

# # Step 2: Click on the first option that appears
# first_option = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
# )))
# first_option.click()
# first_option.send_keys(Keys.ENTER)
# Bundle_Name_4.send_keys(Keys.ENTER)   # 👈 Enter key press




# ✅ Step 1: Click dropdown
Select_Users = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[6]/div/div[2]/div/div/div[1]/div[2]'
)))
Select_Users.click()
time.sleep(1)

# ✅ Step 2: Select second option
first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
)))
first_option.click()
time.sleep(1)

# ✅ Step 3: Click on empty space in body
body = driver.find_element(By.TAG_NAME, "body")
ActionChains(driver).move_to_element_with_offset(body, 0, 0).click().perform()
time.sleep(1)

time.sleep(3)

# ✅ Wait for expiry date field
expiry_date = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@contenteditable="false"]'
)))

# ✅ Clear (in case koi purani value ho)
# expiry_date.clear()

# ✅ Send your date (format MM/DD/YYYY)
expiry_date.send_keys("12/12/2025")

time.sleep(3)


# Add_Document = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class=" tw-w-40 btn btn-primary"]')))
# Add_Document.click()

time.sleep(6)


