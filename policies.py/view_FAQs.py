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

# Wait until Policies menu appears and click
policies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="18. Policies"]')))
policies.click()
time.sleep(1)

# Sidebar locate karo
sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# Element locate karo
layout_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# --- Scroll step by step (smooth) ---
for _ in range(3):   # jitna neeche le jana ho utna loop
    driver.execute_script("arguments[0].scrollBy(0, 300);", layout_div)
    time.sleep(1)

# --- OR direct neeche tak scroll karna ho to ---
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", layout_div)


# Ab "View FAQ Category" pe click karo
View_FAQs = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="18.6 View FAQs"]')))
View_FAQs.click()

time.sleep(2)


# Ab "Add FAQs" pe click karo
Add_FAQs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
Add_FAQs.click()
time.sleep(2)

# category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[1]/div/select')))
# category.click()
# time.sleep(1)

# Dropdown open karna
category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[1]/div/div/div/div[1]/div[2]')))
category.click()
time.sleep(1)

# Dropdown ke second option par click karna
second_option = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@role="option" or @class="option"])[1]')))
second_option.click()

time.sleep(2)

Question  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter question"]')))
Question.send_keys("automation question")
time.sleep(2)

Answer   = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter detailed answer"]')))
Answer .send_keys("automation Answer")
time.sleep(2)


# Add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[4]/button[2]')))
# Add_button .click()
# time.sleep(6)