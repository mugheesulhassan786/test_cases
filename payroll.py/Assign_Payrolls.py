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

HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="9. HR Management"]')))
HR_Management.click()
time.sleep(2)

Assign_Payrolls = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="9.6 Assign Payroll"]')))
Assign_Payrolls.click()

Add_Payrolls = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
Add_Payrolls.click()
time.sleep(1)

# Add_Payrolls_feild = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//*[@id="categoryName"]'
# )))
# Add_Payrolls_feild .click()
# time.sleep(1)

# # Step 2: Click on the first option that appears
# first_option = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//div[contains(@id,"react-select") and @role="option"][5]'
# )))
# first_option.click()
# time.sleep(3)

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Step 1: Dropdown open karo
dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="categoryName"]'))
)
dropdown.click()

# Step 2: First visible option locate aur click karo
first_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="categoryName"]/option[6]'))
)
first_option.click()
# Scroll into view + click (JS fallback)
# driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", first_option)

time.sleep(2)

# Step 1: Dropdown open karo
dropdown_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="userId"]'))
)
dropdown_2.click()

# Step 2: First visible option locate aur click karo
first_option_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="userId"]/option[2]'))
)
first_option_2.click()

time.sleep(2)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Next = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/form/div[2]/button')))
Next.click()

time.sleep(3)

# Thoda neeche scroll (200px)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(0.6)


Base_Salary = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter base salary"]')))
Base_Salary.send_keys("25000")
time.sleep(3)
gov_Base_Salary = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter government base salary"]')))
gov_Base_Salary.send_keys("25000")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 400);")

time.sleep(3)

Add_Allowance = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Allowance name"]')))
Add_Allowance.send_keys("YOUSAF")
time.sleep(3)

Add_Allowance = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="allowanceValue"]')))
Add_Allowance.send_keys("25000")
time.sleep(3)

Add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/form/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/div/div/button')))
Add.click()
time.sleep(3)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

Add_Deduction = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Deduction name"]')))
Add_Deduction.click()
time.sleep(3)

# enter your dedution 
Deduction= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Deduction name"]')))
Deduction.send_keys("tester")
time.sleep(3)

Add_Value  = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="deductionValue"]')))
Add_Value .send_keys("25000")
time.sleep(3)

Next_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/form/div[1]/div[5]/div/div/div[3]/div[1]/div[4]/div/div/button')))
Next_2.click()
time.sleep(3)
# driver.execute_script("window.scrollBy(0, 300);")


Next_0= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/form/div[2]/button[2]')))
Next_0.click()
time.sleep(5)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

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


# submit= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/form/div[2]/button[2]')))
# submit.click()
time.sleep(7)