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

guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="19. Guides"]')))
guides.click()
time.sleep(2)

view_guides_category  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="19.1 View Guides Category"]')))
view_guides_category.click()
time.sleep(3)


add_guides_category  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Category"]')))
add_guides_category.click()
time.sleep(3)

titel  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category title"]')))
titel.send_keys("QA Automation Testing 0.2")
time.sleep(3)

Description  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
Description .send_keys("QA Automation Testing  Description ")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")

# ✅ Step 1: File input locate karo (actual <input type="file"> element)
upload_input = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[@type="file"]'
)))

# ✅ Step 2: Apni file ka path bhejo
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)

time.sleep(4)


driver.execute_script("window.scrollBy(0, 300);")


# Add_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[4]/button[2]')))
# Add_category.click()
time.sleep(6)

# view_guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebarApps"]/ul/li[2]/a')))
# view_guides.click()
# time.sleep(2)

# Add_guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
# Add_guides.click()
# time.sleep(6)