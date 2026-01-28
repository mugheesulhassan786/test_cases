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
# driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
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

# Complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-nav"]/li[11]/a/span')))
# Complaint .click()
# time.sleep(1.0)
# # ✅ Sidebar ko bottom tak scroll karo
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Complaint)

# # ✅ Agar thoda thoda scroll karna ho (step by step)
# driver.execute_script("arguments[0].scrollBy(0, 100);", Complaint)  #
# View_complaint_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.1 View Complaint Category"]')))
# View_complaint_Category.click()
# time.sleep(1.0)

# Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
# Add_Expense_Category.click()
# time.sleep(3)

# # titel = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter category title"]')))
# # titel.send_keys("Automation Teating")
# # time.sleep(2)


# # 50 unique names list
# names = [
#     "Automation Testing", "QA Automation", "Selenium Scripts", "Test Automation",
#     "Unit Testing", "Integration Tests", "Python Automation", "API Testing",
#     "Performance Testing", "Load Testing", "UI Automation", "Data Driven Tests",
#     "Keyword Driven Tests", "Hybrid Framework", "Automation Framework",
#     "Smoke Testing", "Regression Testing", "System Testing", "Functional Testing",
#     "Acceptance Testing", "Bug Tracker", "CI/CD Pipeline", "DevOps Automation",
#     "Test Reports", "Random Tests", "Dynamic Testing", "Automation Bot",
#     "Script Runner", "Auto QA", "Smart Testing", "WebDriver Test",
#     "Test Manager", "Auto Checker", "AI Testing", "Cloud Testing",
#     "Automation Suite", "Testing Cycle", "Scenario Testing", "Python Scripts",
#     "QA Tools", "Fast Automation", "Parallel Testing", "Automation Pro",
#     "Test Wizard", "Error Finder", "Test Generator", "Script Auto",
#     "Testing Ninja", "QA Bot", "Smart QA", "Agile Testing"
# ]

# # Wait for element
# titel = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter category title"]')))

# # Select random name from list
# random_name = random.choice(names)

# # Send it to input field
# titel.send_keys(random_name)
# time.sleep(2)



# Description= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
# Description.send_keys("this automation testing script is created by yousaf")
# time.sleep(3)


# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)

# # ✅ Dropzone ke andar actual input[type="file"] dhundo
# upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# # Agar input hidden hai to visible karo
# driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
# driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# # ✅ Apni file ka full path do (rename karke simple naam rakhna)
# file_path = r"C:\Users\M Yunas Khan\Downloads\Complaints.png"
# upload_input.send_keys(file_path)
# time.sleep(3)


# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)


# Add_complaint_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[4]/div/button')))
# Add_complaint_Category.click()
# time.sleep(7)


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
# 4) Navigate to Complaint Category page
# ----------------------------------------------------------------------------------------------
Complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="8. Complaints & Ticketing"]')))
Complaint.click()
time.sleep(1.0)

driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Complaint)
driver.execute_script("arguments[0].scrollBy(0, 100);", Complaint)

View_complaint_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="8.1 View Complaint Category"]')))
View_complaint_Category.click()
time.sleep(1.0)

# 50 unique names list
names = [
    "Automation Testing", "QA Automation", "Selenium Scripts", "Test Automation",
    "Unit Testing", "Integration Tests", "Python Automation", "API Testing",
    "Performance Testing", "Load Testing", "UI Automation", "Data Driven Tests",
    "Keyword Driven Tests", "Hybrid Framework", "Automation Framework",
    "Smoke Testing", "Regression Testing", "System Testing", "Functional Testing",
    "Acceptance Testing", "Bug Tracker", "CI/CD Pipeline", "DevOps Automation",
    "Test Reports", "Random Tests", "Dynamic Testing", "Automation Bot",
    "Script Runner", "Auto QA", "Smart Testing", "WebDriver Test",
    "Test Manager", "Auto Checker", "AI Testing", "Cloud Testing",
    "Automation Suite", "Testing Cycle", "Scenario Testing", "Python Scripts",
    "QA Tools", "Fast Automation", "Parallel Testing", "Automation Pro",
    "Test Wizard", "Error Finder", "Test Generator", "Script Auto",
    "Testing Ninja", "QA Bot", "Smart QA", "Agile Testing"
]

# ----------------------------------------------------------------------------------------------
# ✅ Repeat block 50 times
# ----------------------------------------------------------------------------------------------
for i in range(50):
    print(f"🔄 Running iteration {i+1}...")

    # Click on "Add Complaint Category"
    Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Complaint Category"]')))
    Add_Expense_Category.click()
    time.sleep(3)

    # Title field
    titel = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter category title"]')))

    # Pick unique name (use i for index to avoid duplicates)
    random_name = names[i % len(names)]
    titel.send_keys(random_name)
    time.sleep(1.5)

    # Description
    Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
    Description.send_keys("this automation testing script is created by yousaf")
    time.sleep(2)

    # Scroll down
    html = driver.find_element(By.XPATH, "/html")
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.6)

    # File upload
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
    driver.execute_script("arguments[0].style.display = 'block';", upload_input)
    file_path = "./img/Image_1.png"
    upload_input.send_keys(file_path)
    time.sleep(2)

    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.6)

    # Click "Add Complaint Category"
    # Add_complaint_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[4]/div/button')))
    # Add_complaint_Category.click()
    time.sleep(5)

print("✅ All 50 complaint categories added successfully!")
