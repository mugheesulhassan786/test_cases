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
# View_complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.2 View Complaint"]')))
# View_complaint.click()
# time.sleep(1.0)

# Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
# Add_Expense_Category.click()
# time.sleep(3)

# #select_category
# select_category= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectedCategory"]/div/div[1]/div[2]')))
# select_category.click()

# # Step 2: Wait for first option and click it
# first_option_danger = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
# )
# first_option_danger.click()
# time.sleep(3)


# # Step 1: Click on the dropdown to expand options
# select_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="role"]')))
# select_role.click()

# # Step 2: Wait for dropdown to fully render
# time.sleep(1)  # Short pause to allow dropdown to expand

# # Step 3: Select the desired option (e.g., 3rd option)
# first_option = wait.until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="role"]/option[4]'))
# )
# first_option.click()

# time.sleep(2)
# # Step 1: Click on the dropdown to expand options
# select_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/div/div/div/div[1]/div[2]')))
# select_role.click()

# # Step 2: Wait for dropdown to fully render
# time.sleep(1)  # Short pause to allow dropdown to expand

# # Step 3: Select the desired option (e.g., 3rd option)
# first_option_1 = wait.until(
#     EC.visibility_of_element_located((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
# )
# first_option_1.click()

# time.sleep(2)


# titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter title of the complaint..."]')))
# titel.send_keys("youasf khan")

# time.sleep(2)

# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)
# #this automation testing script is created by Yousaf

# Details  = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="details"]')))
# Details .send_keys("This Automation Testing Script is Created by Yousaf")
# time.sleep(2)

# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)

# # ✅ Dropzone ke andar actual input[type="file"] dhundo
# upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# # Agar input hidden hai to visible karo
# driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
# driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# # ✅ Apni file ka full path do (rename karke simple naam rakhna)
# file_path = r"C:\Users\M Yunas Khan\Downloads\Complaints.png"
# upload_input.send_keys(file_path)
# time.sleep(2)


# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)

# Add_complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[12]/div/button')))
# Add_complaint.click()
# time.sleep(4)


# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(7)

# # Locate the scrollable container (adjust XPath as needed)
# scroll_container = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[3]/div/div/div[2]')

# # Scroll to the far right using JavaScript
# driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_container)
# time.sleep(3)


# Add_Resolution= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cell-actions-undefined"]/div/button[4]')))
# Add_Resolution.click()
# time.sleep(3)


# Resolution= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Add your resolution points here..."]')))
# Resolution.send_keys("This Automation Testing Script is Created by '.......'")
# time.sleep(2) 


# Save= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addResolutionModal"]/div/div[3]/button[1]')))
# Save.click()
# time.sleep(10)

# # Locate the scrollable container (adjust XPath as needed)
# scroll_container = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[3]/div/div/div[2]')

# # Scroll to the far right using JavaScript
# driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_container)
# time.sleep(3)






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
# Navigate to Complaint page once
# ----------------------------------------------------------------------------------------------
Complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-nav"]/li[11]/a/span')))
Complaint.click()
time.sleep(1.0)

driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Complaint)
driver.execute_script("arguments[0].scrollBy(0, 100);", Complaint)

View_complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="8.2 View Complaint"]')))
View_complaint.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------
# ✅ Repeat complaint creation 100 times
# ----------------------------------------------------------------------------------------------
for i in range(100):
    print(f"🔄 Running complaint iteration {i+1}...")

    Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button')))
    Add_Expense_Category.click()
    time.sleep(2)

    # Select category
    select_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectedCategory"]/div/div[1]/div[2]')))
    select_category.click()

    first_option_danger = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
    )
    first_option_danger.click()
    time.sleep(2)

    # Select role
    select_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="role"]')))
    select_role.click()
    time.sleep(1)

    first_option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="role"]/option[4]')))
    first_option.click()
    time.sleep(2)

    # Another dropdown
    select_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[3]/div/div/div/div[1]/div[2]')))
    select_role.click()
    time.sleep(1)

    first_option_1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][3]'))
    )
    first_option_1.click()
    time.sleep(2)

    # Title field (use unique title per iteration)
    titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter title of the complaint..."]')))
    titel.send_keys(f"Automation Complaint {i+1}")
    time.sleep(1.5)

    # Details
    Details = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="details"]')))
    Details.send_keys(f"This is an automation script I wrote, attributed to Yousaf Khan. - Iteration {i+1}")
    time.sleep(1.5)

    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)

    # Upload file
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
    driver.execute_script("arguments[0].style.display = 'block';", upload_input)
    file_path = "./img/Image_1.png"
    upload_input.send_keys(file_path)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)

    # Add complaint
    Add_complaint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[12]/div/button')))
    Add_complaint.click()
    time.sleep(7)

    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)

    # Scroll table
    scroll_container = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[3]/div/div/div[2]')
    driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_container)
    time.sleep(2)

    # Add resolution
    Add_Resolution = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cell-actions-undefined"]/div/button[4]')))
    Add_Resolution.click()
    time.sleep(2)

    Resolution = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Add your resolution points here..."]')))
    Resolution.send_keys(f"This is an automation script I wrote, attributed to Yousaf Khan.{i+1}")
    time.sleep(1.5)

    # driver.execute_script("window.scrollBy(0, 200);")
    # time.sleep(1)

    Save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addResolutionModal"]/div/div[3]/button[1]')))
    Save.click()
    time.sleep(5)

    # Scroll table again
    scroll_container = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/div[3]/div/div/div[2]')
    driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_container)
    time.sleep(2)


# Scroll down
    html = driver.find_element(By.XPATH, "/html")
    html.send_keys(Keys.PAGE_UP)
    time.sleep(0.6)
 # Scroll down
    html = driver.find_element(By.XPATH, "/html")
    html.send_keys(Keys.PAGE_UP)
    time.sleep(0.6)
print("✅ All 100 complaints added with resolutions successfully!")
