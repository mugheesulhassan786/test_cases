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

# ============================================================
# 3) Navigate to HR Management -> Manage Documents -> Add Document
# ============================================================
# sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# # Scroll sidebar to bottom
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)
# driver.execute_script("arguments[0].scrollBy(0, 100);", sidebar)

leads= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="17. Leads"]')))
leads.click()
time.sleep(2)

driver.execute_script("arguments[0].scrollBy(0, 100);", leads)  #
view_leads = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Lead"]')))
view_leads.click()
time.sleep(2)

category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[1]/div/div/div[1]/div[1]/div/div[1]/div[2]')))
category.click()
time.sleep(1)

first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
)))
first_option.click()
time.sleep(2)


name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Name"]')))
name.send_keys("Jackson")

time.sleep(2)
email_field_0 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter email"]')))
email_field_0.send_keys("jon.blake@demoemail.com")
time.sleep(2)


Number = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="phoneNumber"]')))
Number.send_keys("0987654321")
time.sleep(2)

Source= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[1]/div/div/div[5]/div/div/div[1]/div[2]')))
Source.click()
time.sleep(1)

first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'
)))
first_option.click()
time.sleep(2)


Purpose= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter purpose of this lead"]')))
Purpose.send_keys("Retail inquiry for showroom display")
time.sleep(2)


Description = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter description"]')))
Description.send_keys("this automation testing script is created by yousaf")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)
Status= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]')))
Status.click()
time.sleep(1)

first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'
)))
first_option.click()
time.sleep(2)



Assign_To= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]')))
Assign_To.click()
time.sleep(1)

first_option = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'
)))
first_option.click()
time.sleep(2)
print("All fields are filled successfully.")
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

# Add_leads= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/form/div[4]/button[2]')))
# Add_leads.click()
# time.sleep(7)