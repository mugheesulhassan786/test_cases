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
# ✅ Sidebar ko bottom tak scroll karo
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", accounting)

# ✅ Agar thoda thoda scroll karna ho (step by step)
driver.execute_script("arguments[0].scrollBy(0, 100);", accounting)  #
View_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="11.1 View Account Categories"]')))
View_Expense_Category.click()
time.sleep(1.0)

titel = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Sub Categories"]')))
titel.click()
time.sleep(1)
  
Add_Expense_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Add Sub Category"]')))
Add_Expense_Category.click()
time.sleep(5)



  
  #####################
  

# 50 unique names ki list
names = [
    "automation testing 1", "automation testing 2", "automation testing 3",
    "automation testing 4", "automation testing 5", "automation testing 6",
    "automation testing 7", "automation testing 8", "automation testing 9",
    "automation testing 10", "automation testing 11", "automation testing 12",
    "automation testing 13", "automation testing 14", "automation testing 15",
    "automation testing 16", "automation testing 17", "automation testing 18",
    "automation testing 19", "automation testing 20", "automation testing 21",
    "automation testing 22", "automation testing 23", "automation testing 24",
    "automation testing 25", "automation testing 26", "automation testing 27",
    "automation testing 28", "automation testing 29", "automation testing 30",
    "automation testing 31", "automation testing 32", "automation testing 33",
    "automation testing 34", "automation testing 35", "automation testing 36",
    "automation testing 37", "automation testing 38", "automation testing 39",
    "automation testing 40", "automation testing 41", "automation testing 42",
    "automation testing 43", "automation testing 44", "automation testing 45",
    "automation testing 46", "automation testing 47", "automation testing 48",
    "automation testing 49", "automation testing 50"
]

# Random shuffle (taake har dafa order change ho jaye)
random.shuffle(names)

# Dynamic unique name (timestamp add karke)
unique_name = "automation testing " + str(int(time.time()))

titel = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter category title"]')))
titel.clear()
titel.send_keys(unique_name)
print(f"Entered name: {unique_name}")

Description = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="description"]')))
Description.send_keys("this automation testing script is created by yousaf")
time.sleep(1)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# ✅ Dropzone ke andar actual input[type="file"] dhundo
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# ✅ Apni file ka full path do (rename karke simple naam rakhna)
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)
time.sleep(4)

create_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Create Sub Category"]')))
create_Category.click()
time.sleep(7)