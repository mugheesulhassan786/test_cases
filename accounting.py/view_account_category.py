# import html
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time
# import random

# from selenium.webdriver.common.keys import Keys

# # --------------------------
# # Browser options
# # --------------------------
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # --------------------------
# # 3) Login
# # --------------------------
# driver.get("https://bavit-dev.vercel.app/admin/login")
# driver.maximize_window()
# time.sleep(2)

# for _ in range(2):
#     driver.execute_script("window.scrollBy(0, 800);")
#     time.sleep(0.5)

# email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field_login.send_keys("admin@gmail.com")

# password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field_login.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(2)

# # ----------------------------------------------------------------------------------------------
# # 4) Navigate to inventory -> View listing -> Add listing
# # ----------------------------------------------------------------------------------------------

# accounting= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="12. Accounting"]')))
# accounting.click()
# time.sleep(1.0)
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
# #
# View_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="12.1 View Account Categories"]')))
# View_Expense_Category.click()
# time.sleep(1.0)


# Sub_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[1]/ul/li[2]/a')))
# Sub_Expense_Category.click()
# time.sleep(3)

# Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/button')))
# Add_Expense_Category.click()
# time.sleep(5)
# titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category title"]')))
# titel.send_keys("testung")

# Description = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category description"]')))
# Description.send_keys("testung")



# # Step 1: Click the dropdown
# dropdown = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@class="select__input-container css-19bb58m"]'))
# )
# driver.execute_script("arguments[0].click();", dropdown)
# dropdown.click()
# time.sleep(1)  # short delay to allow dropdown to open

# # Step 2: Wait for and click the first option
# first_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '(//div[contains(@class,"select__option")])[1]'))
# )
# driver.execute_script("arguments[0].scrollIntoView(true);", first_option)
# driver.execute_script("arguments[0].click();", first_option)

# time.sleep(2)

# button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Sub Category"]')))
# button.click()
# time.sleep(3)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# # --------------------------
# # Browser setup
# # --------------------------
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # --------------------------
# # Login
# # --------------------------
# driver.get("https://bavit-dev.vercel.app/admin/login")
# driver.maximize_window()
# time.sleep(2)

# email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field_login.send_keys("admin@gmail.com")

# password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field_login.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(3)

# # --------------------------
# # Navigate to Accounting > Sub Category
# # --------------------------
# accounting = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="12. Accounting"]')))
# accounting.click()
# time.sleep(2)

# sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)
# time.sleep(2)

# view_expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="12.1 View Account Categories"]')))
# view_expense.click()
# time.sleep(2)

# sub_expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[1]/ul/li[2]/a')))
# sub_expense.click()
# time.sleep(3)

# # --------------------------
# # List of titles to create
# # --------------------------
# titles = [
# "Accountancy fees", "Advertising and PR", "Amortisation of goodwill", "Audit fees", "Bad debts", "Bank charges",
# "Bonuses", "Cleaning", "Consultancy fees", "Courier services", "Depreciation", "Directors salaries", "Employers NI",
# "Entertaining", "Equipment expensed", "Equipment hire", "Exchange differences & charges",
# "Gain/loss on revaluation of current asset investments - listed",
# "Gain/loss on revaluation of current asset investments - unlisted",
# "Gain/loss on revaluation of fixed asset investments", "Information and publications", "Insurance", "Interest - bank",
# "Interest - leases & HP", "Interest - other", "Light and heat", "Management fees", "Motor expenses",
# "Non-equity dividends", "Other legal and prof", "P/L on disposal of investments",
# "P/L on disposal of land and buildings", "P/L on disposal of plant and machinery", "Pensions", "Postage", "Rates",
# "Rent", "Repairs and maintenance", "Service charges", "Software", "Solicitors fees", "Staff training & welfare",
# "Stationery and printing", "Subscriptions", "Sundry", "Telephone and internet", "Temps and recruitment",
# "Travel and subsistence", "Use of home", "Wages and salaries", "Write backs/discounts", "Cost of sales", "Carriage",
# "Commissions payable", "Decrease/(increase) in stocks", "Direct labour", "Discounts allowed", "Other", "Purchases",
# "Subcontractor costs"
# ]

# # --------------------------
# # Loop to add each category
# # --------------------------
# for title in titles:
#     try:
#         print(f"Adding: {title}")

#         # Click Add button
#         add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/button')))
#         add_btn.click()
#         time.sleep(2)

#         # Fill title
#         title_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category title"]')))
#         title_field.clear()
#         title_field.send_keys(title)
#         time.sleep(2) 
#         # Fill description
#         desc_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category description"]')))
#         desc_field.clear()
#         desc_field.send_keys(f"Description for {title}")

#         # Dropdown selection
#         dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="select__input-container css-19bb58m"]')))
#         driver.execute_script("arguments[0].click();", dropdown)
#         dropdown.click()
#         time.sleep(2)

#         first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[contains(@class,"select__option")])[1]')))
#         driver.execute_script("arguments[0].click();", first_option)
#         time.sleep(1)

#         # Click Create button
#         create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Sub Category"]')))
#         driver.execute_script("arguments[0].click();", create_btn)
#         time.sleep(3)

#         print(f"✅ Created: {title}")

#     except Exception as e:
#         print(f"❌ Error on: {title} -> {e}")
#         driver.refresh()
#         time.sleep(5)

# print("🎯 All done!")
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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --------------------------
# Browser setup
# --------------------------
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# --------------------------
# Login
# --------------------------
driver.get("https://bavit-dev.vercel.app/admin/login")
driver.maximize_window()
time.sleep(2)

email_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field_login.send_keys("admin@gmail.com")

password_field_login = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field_login.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(3)

# --------------------------
# Navigate to Accounting > Sub Category
# --------------------------
accounting = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="12. Accounting"]')))
accounting.click()
time.sleep(2)

sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)
time.sleep(2)

view_expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="12.1 View Account Categories"]')))
view_expense.click()
time.sleep(2)

# Retry logic for clicking Sub Category tab
for attempt in range(3):
    try:
        sub_expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[1]/ul/li[2]/a')))
        driver.execute_script("arguments[0].scrollIntoView(true);", sub_expense)
        sub_expense.click()
        time.sleep(3)
        break
    except Exception as e:
        print(f"Retrying Sub Category click... Attempt {attempt+1}")
        time.sleep(2)

# --------------------------
# List of titles to create
# --------------------------
titles = [
  
    
    "Information and publications",
    "Insurance",
    "Light and heat",
    "Management fees",
    "Motor expenses",
    "Other legal and prof",
    "PL on disposal of land and buildings",
    "PL on disposal of plant and machinery",
    "Pensions",
    "Postage",
    "Rent",
    "Repairs and maintenance",
    "Service charges",
    "Software",
    "Solicitors fees",
    "Staff training welfare",
    "Stationery and printing",
    "Subscriptions",
    "Sundry",
    "Telephone and internet",
    "Temps and recruitment",
    "Travel and subsistence",
    "Use of home",
    "Write backs discounts",
    "Cost of sales",
    "Carriage",
    "Commissions payable",
    "Decrease increase in stocks",
    "Discounts allowed",
    "Other",
    "Purchases",
    "Subcontractor costs"
]

# --------------------------
# Loop to add each category
# --------------------------
for title in titles:
    try:
        print(f"Adding: {title}")


        sub_expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[1]/ul/li[2]/a')))
        driver.execute_script("arguments[0].scrollIntoView(true);", sub_expense)
        sub_expense.click()
        time.sleep(3)
        # Click Add button
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/button')))
        add_btn.click()
        time.sleep(2)

        # Fill title
        title_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category title"]')))
        title_field.clear()
        title_field.send_keys(title)
        time.sleep(2)

        # Fill description
        desc_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter category description"]')))
        desc_field.clear()
        desc_field.send_keys(f"Description for {title}")
        time.sleep(2)

        # Dropdown selection
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="select__input-container css-19bb58m"]')))
        driver.execute_script("arguments[0].click();", dropdown)
        dropdown.click()
        time.sleep(3)

        first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[contains(@class,"select__option")])[1]')))
        driver.execute_script("arguments[0].click();", first_option)
        time.sleep(2)
        
        html = driver.find_element(By.XPATH, "/html")
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.6)

        # Click Create button
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Sub Category"]')))
        driver.execute_script("arguments[0].click();", create_btn)
        time.sleep(3)

        print(f"✅ Created: {title}")

    except Exception as e:
        print(f"❌ Error on: {title} -> {e}")
        driver.refresh()
        time.sleep(5)

print("🎯 All done!")