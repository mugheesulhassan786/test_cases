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

accounting= wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="11. Accounting"]')))
accounting.click()
time.sleep(1.0)
# # ✅ Sidebar ko bottom tak scroll karo
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", accounting)

# # ✅ Agar thoda thoda scroll karna ho (step by step)
# driver.execute_script("arguments[0].scrollBy(1, 100);", accounting)  #


  ######################## 

  # Element locate karo
element = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[1]')

# Mid tak scroll karne ke liye JavaScript
driver.execute_script("""
    const el = arguments[0];
    el.scrollTop = (el.scrollHeight - el.clientHeight) / 2;
""", element)

time.sleep(2)


View_Recurring_Expenses= wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="11.2 View Recurring Expense"]')))
View_Recurring_Expenses.click()
time.sleep(1.0)

Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button/i')))
Add_Expense_Category.click()
time.sleep(2 )


###########################################


Title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter recurring expense title"]')))
Title.send_keys("tester")
time.sleep(2)


# enter your amount 


Amount = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="0.00"]')))
Amount.send_keys("20000")
time.sleep(2)

#enter your frequency

#select_category
frequency= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frequency"]/div/div[1]/div[2]')))
frequency.click()

# Step 2: Wait for first option and click it
first_option_danger = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
)
first_option_danger.click()
time.sleep(2)

#enter  your   date  in this field 

# Enter_date  = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[3]/div[2]/div/div/div/div[1]')))
# Enter_date.click()
# time.sleep(2)

# Month field
# Enter_months = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//input[contains(@id,"-month")]')
# ))
# Enter_months.clear()
# Enter_months.send_keys("10")   # October
# time.sleep(1)

# # Day field
# Enter_day = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//input[contains(@id,"-day")]')
# ))
# Enter_day.clear()
# Enter_day.send_keys("19")      # Day
# time.sleep(1)

# # Year field
# Enter_year = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//input[contains(@id,"-year")]')
# ))
# Enter_year.clear()
# Enter_year.send_keys("2025")   # Year
# time.sleep(2)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
#Enter your description

description = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter detailed description of the recurring expense"]')))
description.send_keys("this automation testing script is created by yousaf")
time.sleep(2)

#############  Create Recurring Expense

Create_Recurring_Expense = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[5]/button[2]')))
Create_Recurring_Expense.click()
time.sleep(6)