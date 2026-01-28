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

# content_managrment= wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//a[@href="/content-management/manage-landing"]'))
# )
# content_managrment.click()

calender= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="16. Calendar"]')))
calender.click()

time.sleep(1.0)
# ✅ Sidebar ko bottom tak scroll karo
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", calender)

# ✅ Agar thoda thoda scroll karna ho (step by step)
driver.execute_script("arguments[0].scrollBy(0, 100);", calender)  #
Tasks= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15.1 Tasks"]')))
Tasks.click()
time.sleep(4)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)

# Tasks_1= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[4]/div/div[2]/div[1]/a/div')))
# Tasks_1.click()
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

# replace current Tasks_1 click block with this
try:
    Tasks_1 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[4]/div/div[2]/div[1]/a/div')
    ))
    # ensure element is in view
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", Tasks_1)

    # wait common overlays/modals/spinners to disappear (adjust selector if your app uses different classes)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal, .modal-backdrop, .overlay, .spinner")))

    # try normal click, fallback to JS click if intercepted
    try:
        Tasks_1.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", Tasks_1)

except TimeoutException:
    print("Tasks_1 element not found or not clickable (timeout).")
# ...existing code...
time.sleep(10)



# ...existing code...

# Locate the sidebar / dialog container and scroll it down by 300px (adjust repeats as needed)
sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))

# single step 300px scroll
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 200;", sidebar)

# or stepwise scroll (3 steps of 300px each), with small pauses to allow rendering
for _ in range(3):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 200;", sidebar)
    time.sleep(0.3)

# ...existing code...






start= wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@title="Set status to In Progress and start timer"]')))
start.click()


time.sleep(10)   