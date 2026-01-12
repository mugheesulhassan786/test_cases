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
 # 3 Login
# --------------------------
driver.get("https://gamerpc-test.vercel.app/admin/login")
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
# 4 Navigate to inventory -> View listing -> Add listing
# ----------------------------------------------------------------------------------------------


# content_managrment= wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//a[@href="/content-management/manage-landing"]'))
# )
# content_managrment.click()

# Communications= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="12. Communications"]')))
# Communications.click()

# time.sleep(1.0)
# # ✅ Sidebar ko bottom tak scroll karo
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Communications)

# # ✅ Agar thoda thoda scroll karna ho (step by step)
# driver.execute_script("arguments[0].scrollBy(0, 100);", Communications)  #
# Chat_Management= wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="5. Orders Management"]')))
# Chat_Management.click()
# time.sleep(7)
# ---- Communications ----
communications = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"Communications")]'))
)
driver.execute_script("arguments[0].click();", communications)
time.sleep(1)

# ---- Scroll sidebar / page ----
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

# ---- Orders Management ----
orders_management = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"5. Orders Management")]'))
)
driver.execute_script("arguments[0].click();", orders_management)
time.sleep(7)