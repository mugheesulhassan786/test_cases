# # ==========================
# # Selenium Automation Script
# # With One-by-One Email + Phone Logic + Map Marker Nudge
# # ==========================

# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager


#                         # --------------------------
#                           # 1) Test Emails + Phones List + Counter (100 Items)
#                         # --------------------------
# name = [
#     "Amir Khan","Sana Malik","Bilal Ahmed","Zoya Tariq","Rehan Abbas","Aiman Farooq",
#     "Haider Ali","Minal Zafar","Usman Qureshi","Iqra Yousaf","Tariq Nawaz","Nimra Javed",
#     "Waqas Khan","Hina Shah","Arif Siddiqi","Laiba Ansari","Asim Rauf","Maira Azeem",
#     "Adnan Saeed","Fatima Noor",

#     # ➕ New 30 Names
#     "Fahad Mehmood","Kiran Akhtar","Saad Hassan","Mehwish Iqbal","Talha Riaz",
#     "Anum Khalid","Shahzaib Butt","Rimsha Latif","Hassan Raza","Areeba Saleem",
#     "Danish Sheikh","Ayesha Siddique","Umer Farhan","Komal Yasin","Rafay Ahmed",
#     "Hafsa Karim","Nabeel Anwar","Saba Imran","Moiz Khan","Sidra Munir",
#     "Ali Hamza","Maria Rehman","Zain Ul Abideen","Hoorain Bukhari","Sameer Ashraf",
#     "Esha Tariq","Salman Asghar","Iram Naseer","Faraz Baig","Noor Fatima"
# ]


# emails = [
#     "amir.khan@gmail.com","sana.malik@gmail.com","bilal.ahmed@gmail.com","zoya.tariq@gmail.com",
#     "rehan.abbas@gmail.com","aiman.farooq@gmail.com","haider.ali@gmail.com","minal.zafar@gmail.com",
#     "usman.qureshi@gmail.com","iqra.yousaf@gmail.com","tariq.nawaz@gmail.com","nimra.javed@gmail.com",
#     "waqas.khan@gmail.com","hina.shah@gmail.com","arif.siddiqi@gmail.com","laiba.ansari@gmail.com",
#     "asim.rauf@gmail.com","maira.azeem@gmail.com","adnan.saeed@gmail.com","fatima.noor@gmail.com",

#     # ➕ New 30 Emails
#     "fahad.mehmood@gmail.com","kiran.akhtar@gmail.com","saad.hassan@gmail.com",
#     "mehwish.iqbal@gmail.com","talha.riaz@gmail.com","anum.khalid@gmail.com",
#     "shahzaib.butt@gmail.com","rimsha.latif@gmail.com","hassan.raza@gmail.com",
#     "areeba.saleem@gmail.com","danish.sheikh@gmail.com","ayesha.siddique@gmail.com",
#     "umer.farhan@gmail.com","komal.yasin@gmail.com","rafay.ahmed@gmail.com",
#     "hafsa.karim@gmail.com","nabeel.anwar@gmail.com","saba.imran@gmail.com",
#     "moiz.khan@gmail.com","sidra.munir@gmail.com","ali.hamza@gmail.com",
#     "maria.rehman@gmail.com","zain.abideen@gmail.com","hoorain.bukhari@gmail.com",
#     "sameer.ashraf@gmail.com","esha.tariq@gmail.com","salman.asghar@gmail.com",
#     "iram.naseer@gmail.com","faraz.baig@gmail.com","noor.fatima@gmail.com"
# ]


# # 100 phones (sequential Pakistan style)
# phones = [
#     f"30{str(i).zfill(8)}" for i in range(11110001, 11110101)
# ]

#                                         # --------------------------
#                                             # 2) Counter System
#                                         # --------------------------
# counter_file = "counter.txt"
# if not os.path.exists(counter_file):
#     with open(counter_file, "w") as f:
#         f.write("0")

# with open(counter_file, "r") as f:
#     index = int((f.read() or "0").strip())

# if index >= len(emails) or index >= len(phones):
#     print("⚠️ All test emails/phones already used. Reset counter.txt to start again.")
#     raise SystemExit


# current_name = name[index]
# current_email = emails[index]
# current_phone = phones[index]

# print(f"📱 Using phone: {current_name}")
# print(f"📧 Using email: {current_email}")
# print(f"📱 Using phone: {current_phone}")
# # save next index
# # with open(counter_file, "w") as f:
# #     f.write(str(index + 1))

#                                            # --------------------------
#                                                # 2) Browser Setup
#                                            # --------------------------
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

#                                       # --------------------------
#                                             # 3) Login
#                                       # --------------------------
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

# # --------------------------
# # 4) Navigate to Users -> View Users -> Add User

# # --------------------------
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)
# HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="10. HR Management"]')))
# HR_Management.click()
# time.sleep(2)
# view_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="10.1 View Users"]')))
# view_user.click()
# time.sleep(2)
# add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
# add_user.click()
# time.sleep(2)
#                               # --------------------------
#                                  # 5) Fill User Form
#                               # --------------------------
# # # Category
# # html = driver.find_element(By.XPATH, "/html")
# # html.send_keys(Keys.PAGE_DOWN)
# # time.sleep(0.6)
# # html = driver.find_element(By.XPATH, "/html")
# # html.send_keys(Keys.PAGE_DOWN)
# # time.sleep(0.6)

# user_category = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
# )
# user_category.click()
# search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="react-select__input"]')))
# search_box.send_keys("hr")
# time.sleep(0.8)
# first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"react-select__option")]')))
# first_option.click()

# # Names
# first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="firstName"]')))
# first_name.send_keys()
# first_name.send_keys(current_name)  
# time.sleep(1.0)
# last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Last Name"]')))
# last_name.send_keys()
# last_name.send_keys(current_name)   
# time.sleep(1.0)
# # Email (test email from list)
# email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_input.clear()
# email_input.send_keys(current_email)
# time.sleep(1.0)
# # Phone (test phone from list)
# phone = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="form-control "]')))
# phone.clear()
# phone.send_keys(current_phone)
# time.sleep(1.0)
# # Passwords
# password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="password"]')))
# password_field.clear()
# password_field.send_keys("Bmr@112233")
# time.sleep(1.0)
# confirm_password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]')))
# confirm_password.clear()
# confirm_password.send_keys("Bmr@112233")
# time.sleep(1.0)
# # ------------- location logic (same as before) -------------

# # html = driver.find_element(By.XPATH, "/html")
# # html.send_keys(Keys.PAGE_DOWN)
# # time.sleep(0.6)
# # html.send_keys(Keys.PAGE_DOWN)
# # time.sleep(3)

# location_input = wait.until(
#     EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search for a location (e.g., London, Manchester, etc.)"]'))
# )
# location_input.clear()
# location_input.send_keys(
#     "Street 95, I-8/1, I-8 Markaz Ground, Islamabad, Zone 1, Islamabad Capital Territory, 44000, Pakistan"
# )
# time.sleep(2)
# search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="input-group-text btn btn-primary"]')))
# search_button.click()

# time.sleep(3)

# try:
#     location_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@role="button"]')))
#     location_button.click()
#     time.sleep(0.8)
# except Exception:
#     pass

# actions = ActionChains(driver)
# moved = False
# for locator in [
#     (By.CSS_SELECTOR, ".leaflet-marker-icon"),
#     (By.XPATH, '//img[contains(@class,"leaflet-marker-icon")]'),
#     (By.XPATH, '//img[contains(@src,"marker") or contains(@alt,"marker")]')
# ]:
#     try:
#         marker = wait.until(EC.presence_of_element_located(locator))
#         driver.execute_script("arguments[0].scrollIntoView({block:'center'});", marker)
#         time.sleep(0.3)
#         actions.click_and_hold(marker).move_by_offset(5, 5).pause(0.2).move_by_offset(-3, -3).release().perform()
#         moved = True
#         break
#     except Exception:
#         continue

# if not moved:
#     try:
#         driver.execute_script(
#             "const el=arguments[0]; el.dispatchEvent(new Event('input',{bubbles:true})); "
#             "el.dispatchEvent(new Event('change',{bubbles:true}));", location_input
#         )
#     except Exception:
#         pass

# time.sleep(5)

# html.send_keys(Keys.PAGE_UP)
# time.sleep(1.0)
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1.0)
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1.0)

# save_addres = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//button[@class="d-flex align-items-center gap-2 btn btn-success"]'))
# )
# save_addres.click()
# time.sleep(1.0)

# html.send_keys(Keys.PAGE_UP)
# time.sleep(1.0)
# html.send_keys(Keys.PAGE_UP)
# time.sleep(1.0)

# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1.0)
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1.0)
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(3)
# # inject_badge = """
# # var badge = document.createElement('div');
# # badge.innerText = '🔧 Automated by Yousaf khan';
# # badge.style.position = 'fixed';
# # badge.style.top = '10px';
# # badge.style.right = '10px';
# # badge.style.backgroundColor = '#1e1e1e';
# # badge.style.color = '#00ffcc';
# # badge.style.padding = '8px 14px';
# # badge.style.borderRadius = '8px';
# # badge.style.fontSize = '14px';
# # badge.style.fontFamily = 'Arial, sans-serif';
# # badge.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';
# # badge.style.zIndex = '9999';
# # document.body.appendChild(badge);
# # """

# # driver.execute_script(inject_badge)
# # driver.execute_script("console.log('✅ Automation started by Yousaf khan');")
# # add_user = WebDriverWait(driver, 15).until(
# #     EC.presence_of_element_located((By.XPATH, '//button[@class="mx-2 btn btn-primary"]'))
# # )
# # add_user.click()

# time.sleep(7)

# print(f"✅ User form filled successfully with: {current_email} | {current_phone}")

# driver.quit()

# # --------------------------
# # 7) Update counter for next run
# # --------------------------
# with open(counter_file, "w") as f:
#     f.write(str(index + 1))


# print("Scrolled down successfully.")
# inject_badge = """
# var badge = document.createElement('div');
# badge.innerText = '🔧 Automated by Yousaf khan';
# badge.style.position = 'fixed';
# badge.style.top = '10px';
# badge.style.right = '10px';
# badge.style.backgroundColor = '#1e1e1e';
# badge.style.color = '#00ffcc';
# badge.style.padding = '8px 14px';
# badge.style.borderRadius = '8px';
# badge.style.fontSize = '14px';
# badge.style.fontFamily = 'Arial, sans-serif';
# badge.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';
# badge.style.zIndex = '9999';
# document.body.appendChild(badge);
# """

# driver.execute_script(inject_badge)
# driver.execute_script("console.log('✅ Automation started by Yousaf khan');")
# print("khan  injected the vs successfully.")




















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
# 1) Test Names + Emails + Phones
# --------------------------
name = [
    "Amir Khan",
    "Sana Malik",
    "Bilal Ahmed",
    "Zoya Tariq",
    "Rehan Abbas",
    "Aiman Farooq",
    "Haider Ali",
    "Minal Zafar",
    "Usman Qureshi",
    "Iqra Yousaf",
    "Tariq Nawaz",
    "Nimra Javed",
    "Waqas Khan",
    "Hina Shah",
    "Arif Siddiqi",
    "Laiba Ansari",
    "Asim Rauf",
    "Maira Azeem",
    "Adnan Saeed",
    "Fatima Noor"
]

emails = [
    "amir.khan@gmail.com",
    "sana.malik@gmail.com",
    "bilal.ahmed@gmail.com",
    "zoya.tariq@gmail.com",
    "rehan.abbas@gmail.com",
    "aiman.farooq@gmail.com",
    "haider.ali@gmail.com",
    "minal.zafar@gmail.com",
    "usman.qureshi@gmail.com",
    "iqra.yousaf@gmail.com",
    "tariq.nawaz@gmail.com",
    "nimra.javed@gmail.com",
    "waqas.khan@gmail.com",
    "hina.shah@gmail.com",
    "arif.siddiqi@gmail.com",
    "laiba.ansari@gmail.com",
    "asim.rauf@gmail.com",
    "maira.azeem@gmail.com",
    "adnan.saeed@gmail.com",
    "fatima.noor@gmail.com"
]

# 100 phones (sequential Pakistan style)
phones = [f"30{str(i).zfill(8)}" for i in range(11110001, 11110101)]


# --------------------------
# 2) Counter System with Auto Reset
# --------------------------
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    index = int((f.read() or "0").strip())

# auto reset logic
if index >= len(emails) or index >= len(phones):
    print("⚠️ sab emails/phones use ho chuki hain — counter automatically reset ho gaya ✅")
    index = 0
    with open(counter_file, "w") as f:
        f.write("0")

current_name = name[index]
current_email = emails[index]
current_phone = phones[index]

print(f"👤 Using name: {current_name}")
print(f"📧 Using email: {current_email}")
print(f"📱 Using phone: {current_phone}")

# --------------------------
# 3) Browser Setup
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
# 4) Login
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
# 5) Navigate to Users -> View Users -> Add User
# --------------------------
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

HR_Management = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="9. HR Management"]')))
HR_Management.click()
time.sleep(2)
view_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="9.2 View Users"]')))
view_user.click()
time.sleep(2)
add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="ri-add-line tw-text-sm"]')))
add_user.click()
time.sleep(2)

# --------------------------
# 6) Fill User Form
# --------------------------
user_category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="react-select__input-container css-19bb58m"]'))
)
user_category.click()
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="react-select__input"]')))
search_box.send_keys("hr")
time.sleep(0.8)
first_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"react-select__option")]')))
first_option.click()

# Names
first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="firstName"]')))
first_name.send_keys(current_name.split()[0])  
time.sleep(1.0)
last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Last Name"]')))
last_name.send_keys(current_name.split()[-1])   
time.sleep(1.0)

# Email
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_input.clear()
email_input.send_keys(current_email)
time.sleep(1.0)

# Phone
phone = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="form-control "]')))
phone.clear()
phone.send_keys(current_phone)
time.sleep(1.0)

# Passwords
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="password"]')))
password_field.clear()
password_field.send_keys("Bmr@112233")
time.sleep(1.0)
confirm_password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]')))
confirm_password.clear()
confirm_password.send_keys("Bmr@112233")
time.sleep(1.0)

# ------------- location logic -------------
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

# save_addres = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//button[@class="d-flex align-items-center gap-2 btn btn-success"]'))
# )
# save_addres.click()
time.sleep(1.0)

print(f"✅ User form filled successfully with: {current_email} | {current_phone}")

driver.quit()

# --------------------------
# 7) Update counter for next run
# --------------------------
with open(counter_file, "w") as f:
    f.write(str(index + 1))
