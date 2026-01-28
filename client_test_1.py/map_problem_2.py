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
    # Gmail (10)
    "ali.test001@gmail.com", "ali.test002@gmail.com", "ali.test003@gmail.com",
    "ali.test004@gmail.com", "ali.test005@gmail.com", "ali.test006@gmail.com",
    "ali.test007@gmail.com", "ali.test008@gmail.com", "ali.test009@gmail.com",
    "ali.test010@gmail.com",

    # Yahoo (10)
    "sara.dev001@yahoo.com", "sara.dev002@yahoo.com", "sara.dev003@yahoo.com",
    "sara.dev004@yahoo.com", "sara.dev005@yahoo.com", "sara.dev006@yahoo.com",
    "sara.dev007@yahoo.com", "sara.dev008@yahoo.com", "sara.dev009@yahoo.com",
    "sara.dev010@yahoo.com",

    # Outlook (10)
    "hamza.qa001@outlook.com", "hamza.qa002@outlook.com", "hamza.qa003@outlook.com",
    "hamza.qa004@outlook.com", "hamza.qa005@outlook.com", "hamza.qa006@outlook.com",
    "hamza.qa007@outlook.com", "hamza.qa008@outlook.com", "hamza.qa009@outlook.com",
    "hamza.qa010@outlook.com",

    # Mailinator (10)
    "test.user001@mailinator.com", "test.user002@mailinator.com", "test.user003@mailinator.com",
    "test.user004@mailinator.com", "test.user005@mailinator.com", "test.user006@mailinator.com",
    "test.user007@mailinator.com", "test.user008@mailinator.com", "test.user009@mailinator.com",
    "test.user010@mailinator.com",

    # Protonmail (10)
    "random.demo01@protonmail.com", "random.demo02@protonmail.com", "random.demo03@protonmail.com",
    "random.demo04@protonmail.com", "random.demo05@protonmail.com", "random.demo06@protonmail.com",
    "random.demo07@protonmail.com", "random.demo08@protonmail.com", "random.demo09@protonmail.com",
    "random.demo10@protonmail.com",

    # iCloud (10)
    "zara.sample001@icloud.com", "zara.sample002@icloud.com", "zara.sample003@icloud.com",
    "zara.sample004@icloud.com", "zara.sample005@icloud.com", "zara.sample006@icloud.com",
    "zara.sample007@icloud.com", "zara.sample008@icloud.com", "zara.sample009@icloud.com",
    "zara.sample010@icloud.com",

    # Zoho (10)
    "qa.testing001@zoho.com", "qa.testing002@zoho.com", "qa.testing003@zoho.com",
    "qa.testing004@zoho.com", "qa.testing005@zoho.com", "qa.testing006@zoho.com",
    "qa.testing007@zoho.com", "qa.testing008@zoho.com", "qa.testing009@zoho.com",
    "qa.testing010@zoho.com",

    # Ymail (10)
    "fake.mail01@ymail.com", "fake.mail02@ymail.com", "fake.mail03@ymail.com",
    "fake.mail04@ymail.com", "fake.mail05@ymail.com", "fake.mail06@ymail.com",
    "fake.mail07@ymail.com", "fake.mail08@ymail.com", "fake.mail09@ymail.com",
    "fake.mail10@ymail.com",

    # Inbox (10)
    "example.tester01@inbox.com", "example.tester02@inbox.com", "example.tester03@inbox.com",
    "example.tester04@inbox.com", "example.tester05@inbox.com", "example.tester06@inbox.com",
    "example.tester07@inbox.com", "example.tester08@inbox.com", "example.tester09@inbox.com",
    "example.tester10@inbox.com",

    # Live (10)
    "dummy.account01@live.com", "dummy.account02@live.com", "dummy.account03@live.com",
    "dummy.account04@live.com", "dummy.account05@live.com", "dummy.account06@live.com",
    "dummy.account07@live.com", "dummy.account08@live.com", "dummy.account09@live.com",
    "dummy.account10@live.com",
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

# --------------------------
# 4) Navigate to Users -> View Users -> Add User

# --------------------------
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="10. HR Management"]')))
HR_Management.click()
time.sleep(2)
view_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.1 View Teams"]')))
view_user.click()
time.sleep(2)
add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
add_user.click()
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

last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Last Name"]')))
last_name.send_keys("Khan")

# Email (test email from list)
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_input.clear()
email_input.send_keys(current_email)

# Phone (test phone from list)
phone = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="form-control "]')))
phone.clear()
phone.send_keys(current_phone)

# Passwords
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="password"]')))
password_field.clear()
password_field.send_keys("Bmr@112233")

confirm_password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]')))
confirm_password.clear()
confirm_password.send_keys("Bmr@112233")

# ------------- location logic (same as before) -------------

html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

location_input = wait.until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search for a location (e.g., London, Manchester, etc.)"]'))
)
location_input.clear()
location_input.send_keys(
    "Street 95, I-8/1, I-8 Markaz Ground, Islamabad, Zone 1, Islamabad Capital Territory, 44000, Pakistan"
)

search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="input-group-text btn btn-primary"]')))
search_button.click()

time.sleep(1.2)

try:
    location_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@role="button"]')))
    location_button.click()
    time.sleep(0.8)
except Exception:
    pass

actions = ActionChains(driver)
moved = False
for locator in [
    (By.CSS_SELECTOR, ".leaflet-marker-icon"),
    (By.XPATH, '//img[contains(@class,"leaflet-marker-icon")]'),
    (By.XPATH, '//img[contains(@src,"marker") or contains(@alt,"marker")]')
]:
    try:
        marker = wait.until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", marker)
        time.sleep(0.3)
        actions.click_and_hold(marker).move_by_offset(5, 5).pause(0.2).move_by_offset(-3, -3).release().perform()
        moved = True
        break
    except Exception:
        continue

if not moved:
    try:
        driver.execute_script(
            "const el=arguments[0]; el.dispatchEvent(new Event('input',{bubbles:true})); "
            "el.dispatchEvent(new Event('change',{bubbles:true}));", location_input
        )
    except Exception:
        pass

time.sleep(1.2)

html.send_keys(Keys.PAGE_UP)
time.sleep(1.0)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)

save_addres = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="d-flex align-items-center gap-2 btn btn-success"]'))
)
save_addres.click()

html.send_keys(Keys.PAGE_UP)
time.sleep(1.0)
html.send_keys(Keys.PAGE_UP)
time.sleep(1.0)

html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)

add_user = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="mx-2 btn btn-primary"]'))
)
add_user.click()

time.sleep(7)

print(f"✅ User form filled successfully with: {current_email} | {current_phone}")

driver.quit()

# --------------------------
# 7) Update counter for next run
# --------------------------
with open(counter_file, "w") as f:
    f.write(str(index + 1))
