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

import os

# --------------------------
# 1) Test Emails + Phones List + Counter
# --------------------------

emails = [
    # Gmail
    "ali.test101@gmail.com", "ali.test102@gmail.com", "ali.test103@gmail.com",
    "ali.test104@gmail.com", "ali.test105@gmail.com", "ali.test106@gmail.com",
    "ali.test107@gmail.com", "ali.test108@gmail.com", "ali.test109@gmail.com",
    "ali.test110@gmail.com",

    # Yahoo
    "sara.dev101@yahoo.com", "sara.dev102@yahoo.com", "sara.dev103@yahoo.com",
    "sara.dev104@yahoo.com", "sara.dev105@yahoo.com", "sara.dev106@yahoo.com",
    "sara.dev107@yahoo.com", "sara.dev108@yahoo.com", "sara.dev109@yahoo.com",
    "sara.dev110@yahoo.com",

    # Outlook
    "hamza.qa101@outlook.com", "hamza.qa102@outlook.com", "hamza.qa103@outlook.com",
    "hamza.qa104@outlook.com", "hamza.qa105@outlook.com", "hamza.qa106@outlook.com",
    "hamza.qa107@outlook.com", "hamza.qa108@outlook.com", "hamza.qa109@outlook.com",
    "hamza.qa110@outlook.com",

    # Mailinator
    "test.user101@mailinator.com", "test.user102@mailinator.com", "test.user103@mailinator.com",
    "test.user104@mailinator.com", "test.user105@mailinator.com", "test.user106@mailinator.com",
    "test.user107@mailinator.com", "test.user108@mailinator.com", "test.user109@mailinator.com",
    "test.user110@mailinator.com",

    # Protonmail
    "random.demo101@protonmail.com", "random.demo102@protonmail.com", "random.demo103@protonmail.com",
    "random.demo104@protonmail.com", "random.demo105@protonmail.com", "random.demo106@protonmail.com",
    "random.demo107@protonmail.com", "random.demo108@protonmail.com", "random.demo109@protonmail.com",
    "random.demo110@protonmail.com",

    # iCloud
    "zara.sample101@icloud.com", "zara.sample102@icloud.com", "zara.sample103@icloud.com",
    "zara.sample104@icloud.com", "zara.sample105@icloud.com", "zara.sample106@icloud.com",
    "zara.sample107@icloud.com", "zara.sample108@icloud.com", "zara.sample109@icloud.com",
    "zara.sample110@icloud.com",

    # Zoho
    "qa.testing101@zoho.com", "qa.testing102@zoho.com", "qa.testing103@zoho.com",
    "qa.testing104@zoho.com", "qa.testing105@zoho.com", "qa.testing106@zoho.com",
    "qa.testing107@zoho.com", "qa.testing108@zoho.com", "qa.testing109@zoho.com",
    "qa.testing110@zoho.com",

    # Ymail
    "fake.mail101@ymail.com", "fake.mail102@ymail.com", "fake.mail103@ymail.com",
    "fake.mail104@ymail.com", "fake.mail105@ymail.com", "fake.mail106@ymail.com",
    "fake.mail107@ymail.com", "fake.mail108@ymail.com", "fake.mail109@ymail.com",
    "fake.mail110@ymail.com",

    # Inbox
    "example.tester101@inbox.com", "example.tester102@inbox.com", "example.tester103@inbox.com",
    "example.tester104@inbox.com", "example.tester105@inbox.com", "example.tester106@inbox.com",
    "example.tester107@inbox.com", "example.tester108@inbox.com", "example.tester109@inbox.com",
    "example.tester110@inbox.com",

    # Live
    "dummy.account101@live.com", "dummy.account102@live.com", "dummy.account103@live.com",
    "dummy.account104@live.com", "dummy.account105@live.com", "dummy.account106@live.com",
    "dummy.account107@live.com", "dummy.account108@live.com", "dummy.account109@live.com",
    "dummy.account110@live.com",
]

# 100 fake phones
phones = [
    f"30{str(i).zfill(8)}" for i in range(1001, 1101)
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

# Save new index for next run
with open(counter_file, "w") as f:
    f.write(str(index + 1))

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
suppliers = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="2. Suppliers"]')))
suppliers.click()

view_suppliers = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="2.2 View Suppliers"]')))
view_suppliers.click()

add_suppliers = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
add_suppliers.click()
time.sleep(5)
#--------------------------
#5) Fill User Form
#--------------------------

user_category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
)
user_category.click()
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="react-select__input"]')))
search_box.send_keys("lap")
time.sleep(0.8)
first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"react-select__option")]')))
first_option.click()

# Names
first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="firstName"]')))
first_name.send_keys("Salar")

last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="lastName"]')))
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
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
password_field.clear()
password_field.send_keys("Bmr@112233")

confirm_password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="confirmPassword"]')))
confirm_password.clear()
confirm_password.send_keys("Bmr@112233")

# ------------- location logic (same as before) -------------


html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html.send_keys(Keys.PAGE_UP)
time.sleep(0.6)

location_input = wait.until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search for a location (e.g., London, Manchester, etc.)"]'))
)
location_input.clear()
location_input.send_keys(
    "H-8, Islamabad, Zone 1, Islamabad Capital Territory, 44000, Pakistan"
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

# ✅ File upload section
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# Apni image ka full path send karo (extension zaroori hai)
upload_input.send_keys("./img/Image_1.png")

time.sleep(2)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(1.0)



# add_user = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//button[text()="Add Supplier"]'))
# )
# add_user.click()

time.sleep(7)    

print(f"✅ User form filled successfully with: {current_email} | {current_phone}")

driver.quit()

# --------------------------
# 7) Update counter for next run
# --------------------------
with open(counter_file, "w") as f:
    f.write(str(index + 1))
