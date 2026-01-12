# ==========================
# Selenium Automation Script
# With One-by-One Email + Phone Logic + Map Marker Nudge
# ==========================

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


                        # --------------------------
                          # 1) Test Emails + Phones List + Counter (100 Items)
                        # --------------------------
emails = [
    # Batch 1
    "user.auto001@testmail.com", "user.auto002@testmail.com", "user.auto003@testmail.com",
    "user.auto004@testmail.com", "user.auto005@testmail.com", "user.auto006@testmail.com",
    "user.auto007@testmail.com", "user.auto008@testmail.com", "user.auto009@testmail.com",
    "user.auto010@testmail.com",

    # Batch 2
    "qatest001@fakeinbox.com", "qatest002@fakeinbox.com", "qatest003@fakeinbox.com",
    "qatest004@fakeinbox.com", "qatest005@fakeinbox.com", "qatest006@fakeinbox.com",
    "qatest007@fakeinbox.com", "qatest008@fakeinbox.com", "qatest009@fakeinbox.com",
    "qatest010@fakeinbox.com",

    # Batch 3
    "temp.user001@devmail.com", "temp.user002@devmail.com", "temp.user003@devmail.com",
    "temp.user004@devmail.com", "temp.user005@devmail.com", "temp.user006@devmail.com",
    "temp.user007@devmail.com", "temp.user008@devmail.com", "temp.user009@devmail.com",
    "temp.user010@devmail.com",

    # Batch 4
    "testing.a001@autobot.com", "testing.a002@autobot.com", "testing.a003@autobot.com",
    "testing.a004@autobot.com", "testing.a005@autobot.com", "testing.a006@autobot.com",
    "testing.a007@autobot.com", "testing.a008@autobot.com", "testing.a009@autobot.com",
    "testing.a010@autobot.com",

    # Batch 5
    "demo.check001@systemmail.com", "demo.check002@systemmail.com",
    "demo.check003@systemmail.com", "demo.check004@systemmail.com",
    "demo.check005@systemmail.com", "demo.check006@systemmail.com",
    "demo.check007@systemmail.com", "demo.check008@systemmail.com",
    "demo.check009@systemmail.com", "demo.check010@systemmail.com",
]

# 100 phones (sequential Pakistan style)
phones = [
    f"30{str(i).zfill(8)}" for i in range(11110001, 11110101)
]

                                        # --------------------------
                                            # 2) Counter System
                                        # --------------------------
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    index = int((f.read() or "0").strip())

if index >= len(emails) or index >= len(phones):
    print("⚠️ All test emails/phones already used. Reset counter.txt to start again.")
    raise SystemExit

current_email = emails[index]
current_phone = phones[index]
print(f"📧 Using email: {current_email}")
print(f"📱 Using phone: {current_phone}")

# save next index
# with open(counter_file, "w") as f:
#     f.write(str(index + 1))

                                           # --------------------------
                                               # 2) Browser Setup
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

# --------------------------
# 4) Navigate to Users -> View Users -> Add User

# --------------------------
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="10. HR Management"]')))
HR_Management.click()
time.sleep(2)
view_teams = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.2 View Teams"]')))
view_teams.click()
time.sleep(2)
add_team = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
add_team.click()
time.sleep(2)
                              # --------------------------
                                 # 5) Fill User Form
                              # --------------------------
# Category
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

user_category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
)
user_category.click()
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="react-select__input"]')))
search_box.send_keys("qua")
time.sleep(0.8)
first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"react-select__option")]')))
first_option.click()

# Names
first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter team name"]')))
first_name.send_keys("Salar")

#team name

last_name = wait.until(EC.presence_of_element_located((By.XPATH, ' //input[@placeholder="Enter team name"]')))
last_name.send_keys("Khan")


# description

last_name = wait.until(EC.presence_of_element_located((By.XPATH, ' //textarea[@name="description"]')))
last_name.send_keys("new This category is created for testing purposes by Muhammad Yousaf Liaquat Ali Khan . It includes mini PCs and related products.")
time.sleep(2)
inject_badge = """
var badge = document.createElement('div');
badge.innerText = '🔧 Automated by Yousaf khan';
badge.style.position = 'fixed';
badge.style.top = '10px';
badge.style.right = '10px';
badge.style.backgroundColor = '#1e1e1e';
badge.style.color = '#00ffcc';
badge.style.padding = '8px 14px';
badge.style.borderRadius = '8px';
badge.style.fontSize = '14px';
badge.style.fontFamily = 'Arial, sans-serif';
badge.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';
badge.style.zIndex = '9999';
document.body.appendChild(badge);
"""

driver.execute_script(inject_badge)
driver.execute_script("console.log('✅ Automation started by Yousaf khan');")

# button = wait.until(EC.presence_of_element_located((By.XPATH, '  //button[@class="mx-2 btn btn-primary"]')))
# button.click()



time.sleep(7)

#print(f"✅ User form filled successfully with: {current_email} | {current_phone}")

driver.quit()

# --------------------------
# 7) Update counter for next run
# --------------------------
with open(counter_file, "w") as f:
    f.write(str(index + 1))
