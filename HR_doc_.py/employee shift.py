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
driver.get("https://admin.buildmyrig.co.uk/admin/login")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admin@gmail.com")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("BuildMyRig@123!")

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

Employee_feild = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.3 Employee Shifts"]')))
Employee_feild.click()


Add_Employee = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
Add_Employee.click()

time.sleep(4)

Shift_Name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Shift Name"]')))
Shift_Name.send_keys("night")
time.sleep(3)


Shift_Name_1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/div/div/div[1]')))
Shift_Name_1.send_keys("12")
Shift_Name_1.send_keys("00")
time.sleep(3)

Shift_Name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[4]/div/div/div[1]')))
Shift_Name.send_keys("06")
Shift_Name.send_keys("00")

time.sleep(3)

option_feild = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hasBreak"]')))
option_feild.click()

time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")

time.sleep(3)

# Shift_Name_2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[7]/div/div/div[1]')))
# Shift_Name_2.send_keys("04")
# Shift_Name_2.send_keys("00")
# time.sleep(3)

Shift_Name_3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[7]/div/div/div[1]')))
Shift_Name_3.send_keys("04")
Shift_Name_3.send_keys("00")
time.sleep(3)

Shift_Name_4 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[8]/div/div/div[1]')))
Shift_Name_4.send_keys("04")
Shift_Name_4.send_keys("30")
time.sleep(3)

Shift = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Shift Description"]')))
Shift.send_keys("Worked on assigned automation and testing tasks during the night shift. Focused on ensuring progress continuity by handling pending modules and monitoring script executions.")
time.sleep(3)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[10]/button[2]')))
done.click()

time.sleep(6)