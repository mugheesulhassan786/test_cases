"""
======================================================
   🔒 PRIVATE AUTOMATION SCRIPT 🔒
   Author: YOUSAF LIAQUAT ALI KHAN
   Note: This script is written by YOUSAF LIAQUAT ALI KHAN only.
   Do not copy, modify, or reuse without permission.
======================================================
"""

import time
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ============================================================
                 # 1) Browser Setup
# ============================================================
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# ============================================================
                  # 2) Login
# ============================================================
driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
driver.maximize_window()
time.sleep(2)

# Scroll down a bit before login
for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

# Enter login details
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field.send_keys("admin@gmail.com")

password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(5)

# ============================================================
# 3) Navigate to HR Management -> Manage Documents -> Add Document
# ============================================================
# sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# # Scroll sidebar to bottom
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)
# driver.execute_script("arguments[0].scrollBy(0, 500);", sidebar)


sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))
driver.execute_script("arguments[0].scrollBy(0, 200);", sidebar)



HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="9. HR Management"]')))
HR_Management.click()
time.sleep(2)

view_document = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="9.8 Manage Documents"]')))
view_document.click()
time.sleep(2)

add_document = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button'
)))
add_document.click()
time.sleep(4)

# ============================================================
# 4) Document Category Selection
# ============================================================
doc_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="docCategory"]/div/div[1]/div[2]')))
doc_category.click()
time.sleep(1)

first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
)))
first_option.click()
time.sleep(3)

# ============================================================
                     # 5) Fill Document Details
# ============================================================
author_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Document Author"]')))
author_field.send_keys(Keys.CONTROL + "a")
author_field.send_keys(Keys.DELETE)
author_field.send_keys("YOUSAF KHAN")
time.sleep(2)

title_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Document Title"]')))
title_field.send_keys("automation tester")
time.sleep(2)

version_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Document Version"]')))
version_field.send_keys("0.3")
time.sleep(2)

# Tags input (multiple values with Enter)
tags_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="react-tagsinput-input"]')))
tags_input.send_keys("automation")
tags_input.send_keys(Keys.ENTER)
time.sleep(2)

tags_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="react-tagsinput-input"]')))
tags_input.send_keys("tester")
tags_input.send_keys(Keys.ENTER)
time.sleep(2)

# ============================================================
                     # 6) Upload File
# ============================================================
driver.find_element(By.XPATH, "/html").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)
time.sleep(3)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)

# ============================================================
                   # 7) Assign Roles and Users
# ============================================================
filter_by_roles = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[6]/div/div[1]/div/div/div[1]/div[2]'
)))
filter_by_roles.click()

role_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][5]'
)))
role_option.click()
time.sleep(3)

# Select User
select_users = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[6]/div/div[2]/div/div/div[1]/div[2]'
)))
select_users.click()
time.sleep(1)

user_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'
)))
user_option.click()
time.sleep(1)

# Click empty space in body
body = driver.find_element(By.TAG_NAME, "body")
ActionChains(driver).move_to_element_with_offset(body, 0, 0).click().perform()
time.sleep(1)

# ============================================================
                  # 8) Set Expiry Date
# ============================================================
expiry_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@contenteditable="false"]')))
expiry_date.send_keys("12/12/2025")
time.sleep(3)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
# ============================================================
               # 9) Save Document
# ============================================================
# save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class=" tw-w-40 btn btn-primary"]')))
# save_button.click()

# ============================================================
# 🔧 Inject Yousaf khan Signature Badge + Console Log
# ============================================================
inject_badge = """
var badge = document.createElement('div');
badge.innerText = '🔧 Automated by Yousaf khan';
badge.style.position = 'fixed';
badge.style.top = '10px';
badge.style.right = '10px';
badge.style.backgroundColor = '#1e1e1e';
badge.style.color = '#00ffcc';
badge.style.padding = '8px 14px';
badge.style.borderRadius = '8px';
badge.style.fontSize = '14px';
badge.style.fontFamily = 'Arial, sans-serif';
badge.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';
badge.style.zIndex = '9999';
document.body.appendChild(badge);
"""

driver.execute_script(inject_badge)
driver.execute_script("console.log('✅ Automation started by Yousaf khan');")

# Optional: Keep browser open to view badge
time.sleep(8)
driver.quit()



