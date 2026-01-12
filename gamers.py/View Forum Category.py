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

from selenium.webdriver.support.ui import Select


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
driver.get("https://gamerpc-test.vercel.app/admin/login")
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

# 3) Navigate to policies -> view FAQs category  -> Add FAQs
# ============================================================

# Wait until "Gamers Community" menu appears and click
Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
Gamers.click()
time.sleep(2)

# Sidebar locate karo
sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))

# --- Smooth scroll sidebar step by step ---
scroll_script = """
let sidebar = arguments[0];
let totalHeight = sidebar.scrollHeight;
let current = sidebar.scrollTop;
let step = 200; // jitna neeche per scroll hoga ek step mein
let interval = setInterval(() => {
    if (current + step >= totalHeight) {
        sidebar.scrollTop = totalHeight;
        clearInterval(interval);
    } else {
        current += step;
        sidebar.scrollTop = current;
    }
}, 200);
"""
driver.execute_script(scroll_script, sidebar)

# Wait a bit for scroll to complete
time.sleep(3)

# Ab "View Forum Category" pe click karo
View_Forum_Category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[text()="15.3 View Forum Category"]'))
)
View_Forum_Category.click()
time.sleep(2)


Add_Category= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Category"]')))
Add_Category.click()
time.sleep(3)


Author_Name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category name"]')))
Author_Name.send_keys(" Automation testing")
time.sleep(2)

#Description

Description= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
Description.send_keys("This is QA Automation testing by YOUSAF KHAN")
time.sleep(2)

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
time.sleep(3)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# Create_Category= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Category"]')))
# Create_Category.click()
time.sleep(7)

# # ============================================================
# # 🔒 PRIVATE AUTOMATION SCRIPT 🔒
# # Author: YOUSAF LIAQUAT ALI KHAN
# # ============================================================

# import time
# import html
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# # ============================================================
# # 1) Browser Setup
# # ============================================================
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # ============================================================
# # 2) Login
# # ============================================================
# driver.get("https://bavit-test.vercel.app/admin/login")
# driver.maximize_window()
# time.sleep(2)

# for _ in range(2):
#     driver.execute_script("window.scrollBy(0, 800);")
#     time.sleep(0.5)

# email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field.send_keys("admin@gmail.com")

# password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(5)

# # ============================================================
# # 3) Navigate to Forum Category Page Once
# # ============================================================
# Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
# Gamers.click()
# time.sleep(2)

# sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
# scroll_script = """
# let sidebar = arguments[0];
# let totalHeight = sidebar.scrollHeight;
# let current = sidebar.scrollTop;
# let step = 200;
# let interval = setInterval(() => {
#     if (current + step >= totalHeight) {
#         sidebar.scrollTop = totalHeight;
#         clearInterval(interval);
#     } else {
#         current += step;
#         sidebar.scrollTop = current;
#     }
# }, 200);
# """
# driver.execute_script(scroll_script, sidebar)
# time.sleep(3)

# View_Forum_Category = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[text()="15.3 View Forum Category"]'))
# )
# View_Forum_Category.click()
# time.sleep(2)

# # ============================================================
# # 4) Loop for Adding 50 Categories
# # ============================================================
# for i in range(1, 51):  # 1 se 50 tak loop
#     print(f"✅ Creating category {i}...")

#     Add_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Category"]')))
#     Add_Category.click()
#     time.sleep(2)

#     Author_Name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category name"]')))
#     Author_Name.send_keys(f"Automation Testing Category {i}")

#     Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
#     Description.send_keys(f"This is QA Automation testing by YOUSAF KHAN - Batch {i}")

#     html_el = driver.find_element(By.XPATH, "/html")
#     html_el.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.6)

#     upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
#     driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
#     driver.execute_script("arguments[0].style.display = 'block';", upload_input)

#     file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
#     upload_input.send_keys(file_path)
#     time.sleep(4)

#     html_el.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.5)

#     Create_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Category"]')))
#     Create_Category.click()
#     time.sleep(5)

#     # Optional: Wait or refresh between iterations if needed
#     driver.refresh()
#     time.sleep(5)

# print("🎉 All 50 categories created successfully!")
