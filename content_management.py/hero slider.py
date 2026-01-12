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


content_managrment= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="14. Content Management"]')))
content_managrment.click()

time.sleep(4)
# ✅ Sidebar ko bottom tak scroll karo
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", content_managrment)

# ✅ Agar thoda thoda scroll karna ho (step by step)
driver.execute_script("arguments[0].scrollBy(0, 100);", content_managrment)  #
hero_slider= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Hero Slider"]')))
hero_slider.click()
time.sleep(3)


Add_new_slider = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add New Slide"]')))
Add_new_slider.click()
time.sleep(3) 


slide_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Slide Title"]')))
slide_title.send_keys("Summer Sale")
time.sleep(3)


slide_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Slide Subtitle"]')))
slide_title.send_keys("Summer Saleeee 50% Off on All Items!")
time.sleep(3)

# ✅ Step 1: File input locate karo
upload_input = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[@type="file"]'
)))

# ✅ Step 2: Apni file ka path bhejo
file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
upload_input.send_keys(file_path)


time.sleep(3)


Titel = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="https://example.com""]')))
Titel.send_keys("YOUSAF KHAN")
time.sleep(7)