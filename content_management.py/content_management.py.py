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

content_managrment= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="13. Content Management"]')))
content_managrment.click()

time.sleep(1.0)
# ✅ Sidebar ko bottom tak scroll karo
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", content_managrment)

# ✅ Agar thoda thoda scroll karna ho (step by step)
driver.execute_script("arguments[0].scrollBy(0, 100);", content_managrment)  #
Deals= wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Deals"]')))
Deals.click()
time.sleep(3)

# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)

Add_Deals = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Deals"]')))
Add_Deals.click()
time.sleep(5)


Select_unit= wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@name="dealType"]'))
)

# Type category

Select_unit.click()

# first_option_option_2 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][1]'))
# )
# first_option_option_2.click()
# time.sleep(3)                                          


Discount_Value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter percentage (e.g., 10)"]')))

Discount_Value.send_keys("12")

Apply_Deal_To = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[2]/div/div/div[1]/div'))
)

# Type category

# Apply_Deal_To.click()

time.sleep(4)


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(3)

