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
driver.get("https://gamerpc-test.vercel.app/admin/login")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admin@gmail.com")
print("Email entered successfully.")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("Bmr@1234")
print("Password entered successfully.")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(7)
print("Login button clicked successfully.")

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
print("Sidebar scrolled successfully.")

guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="19. Guides"]')))
guides.click()
time.sleep(2)
print("Guides section clicked successfully.")


view_guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="19.2 View Guides"]')))
view_guides.click()
time.sleep(3)
print("View Guides section clicked successfully.")

Add_guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Guide"]')))
Add_guides.click()
time.sleep(3)
print("Add Guide button clicked successfully.")


# Step 1: Dropdown open karo
dropdown_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="type"]/div/div[1]/div[2]'))
)
dropdown_1.click()


options = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))

)
# Select 2nd option safely using JavaScript (to avoid intercept error)
driver.execute_script("arguments[0].click();", options[1])
time.sleep(1)

# Step 1: Dropdown open karo
dropdown_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="category"]/div/div[1]/div[2]'))
)
dropdown_2.click()



options = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))
)

# Select 2nd option safely using JavaScript (to avoid intercept error)
driver.execute_script("arguments[0].click();", options[1])
time.sleep(1)
print("Dropdown options selected successfully.")


Titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Title"]')))
Titel.send_keys("YOUSAF KHAN")
time.sleep(4)
print("Title entered successfully.")  

Description = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="description"]')))
Description .send_keys("QA Automation Testing is currently in progress  to Quality Assurance the process of ensuring software meets quality ")
time.sleep(2)
print("Description entered successfully.")

Focus_keyword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Press Enter or add comma (,) to create a keyword"]')))
Focus_keyword.send_keys("automation")
Focus_keyword.send_keys(Keys.ENTER)
time.sleep(3)
print("Focus keyword entered successfully.")

driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)

Content  = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[6]/div/div[2]/div[1]')))
Content .send_keys("QA → Refers to Quality Assurance, the process of ensuring the software meets quality standards.")
time.sleep(6)
print("Content entered successfully.")

driver.execute_script("window.scrollBy(0, 400);")
# ✅ Step 1: File input locate karo
upload_input = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[@type="file"]'
)))

# ✅ Step 2: Apni file ka path bhejo
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)

time.sleep(9)
print("File uploaded successfully.")


driver.execute_script("window.scrollBy(0, 400);")

print("Scrolled down successfully.")
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
print("khan  injected the vs successfully.")

# Add_guides = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Guie"]')))
# Add_guides.click()
time.sleep(7)