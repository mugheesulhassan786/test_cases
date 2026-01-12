# ============================================================
# 🔒 PRIVATE AUTOMATION SCRIPT 🔒
# Author: YOUSAF LIAQUAT ALI KHAN
# ============================================================

import time
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field.send_keys("admin@gmail.com")

password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(5)

# ============================================================
# 3) Navigate to Forum Category Page Once
# ============================================================
Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
Gamers.click()
time.sleep(2)

sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
scroll_script = """
let sidebar = arguments[0];
let totalHeight = sidebar.scrollHeight;
let current = sidebar.scrollTop;
let step = 200;
let interval = setInterval(() => {
    if (current + step >= totalHeight) {
        sidebar.scrollTop = totalHeight;
        clearInterval(interval);
    } else {
        current += step;
        sidebar.scrollTop = current;
    }
}, 200);
"""
driver.execute_script(scroll_script, sidebar)
time.sleep(3)

View_Forum = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[text()="15.4 View Forums"]'))
)
View_Forum.click()
time.sleep(2)



Add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Forum"]')))
Add_button.click()
time.sleep(3)

Forum_Category= wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="react-select__input-container css-19bb58m"]'))
    )
Forum_Category.click()
time.sleep(2)

first_option_danger = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
    )
first_option_danger.click()
time.sleep(3) 

Title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter forum title"]')))
Title.send_keys("Automation Testing Category ")
time.sleep(1)

Bundle_Name_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Press Enter or add comma (,) to create a keyword"]')))
Bundle_Name_4.send_keys("automation")
Bundle_Name_4.send_keys(Keys.ENTER)
time.sleep(2)
Bundle_Name_4.send_keys("tester")
Bundle_Name_4.send_keys(Keys.ENTER)
time.sleep(2)


Content = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="ql-editor ql-blank"]')))
Content.send_keys("This is QA Automation testing by YOUSAF KHAN ")
time.sleep(5)


html_el = driver.find_element(By.XPATH, "/html")
html_el.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)


Create_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[5]/button[2]')))
Create_Category.click()
time.sleep(5)

    # Optional: Wait or refresh between iterations if needed
# driver.refresh()
time.sleep(5)

print("🎉 All 50 categories created successfully!")
