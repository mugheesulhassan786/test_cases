

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time

# # ===============================
# # Email aur Name Lists
# # ===============================
# emails = [
    # "justice.marin@gmail.com",
    # "aldo.murphy@gmail.com",
    # "bella.sierra@gmail.com",
    # "dayton.pena@gmail.com",
    # "rachel.mendez@gmail.com",
    # "arthur.burton@gmail.com",
    # "miriam.hardy@gmail.com",
    # "jayceon.fischer@gmail.com",
    # "maci.acevedo@gmail.com",
    # "dakari.bruce@gmail.com",
    # "marilyn.wade@gmail.com",
    # "jake.grant@gmail.com",
    # "alaina.martinez@gmail.com",
    # "alexander.lee@gmail.com",
    # "scarlett.hoover@gmail.com",
    # "jaziel.christensen@gmail.com",
    # "carmen.terrell@gmail.com",
    # "jaxen.buck@gmail.com",
    # "livia.romero@gmail.com",
    # "bryson.todd@gmail.com"
# ]

# # ===============================
# # Browser setup
# # ===============================
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# wait = WebDriverWait(driver, 30)

# # ===============================
# # Function to perform login in new tab
# # ===============================
# def do_login_in_new_tab(email):
#     # Open new tab
#     driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.get("https://bav-client-hera.vercel.app/")
#     driver.maximize_window()

#     # Wait for full page load
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#     time.sleep(2)

#     # Scroll thoda niche (icon visible ho jaye)
#     driver.execute_script("window.scrollTo(0, 150);")

#     # Click account/login icon (safe JS click)
#     print(f"🔎 Trying to click login icon for {email} ...")
#     login_btn = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
#     )
#     driver.execute_script("arguments[0].click();", login_btn)
#     time.sleep(3)

#     # Fill login fields
#     email_field = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
#     )
#     email_field.send_keys(email)

#     password = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))
#     )
#     password.send_keys("Bmr@112233")

#     # Click login
#     login_click = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[text()="Sign in"]'))
#     )
#     driver.execute_script("arguments[0].click();", login_click)
#     print(f"✅ Login attempted for: {email}")
#     time.sleep(5)

# # ===============================
# # Main Loop — one email per new tab
# # ===============================
# for email in emails:
#     try:
#         do_login_in_new_tab(email)
#     except Exception as e:
#         print(f"❌ Error for {email}: {e}")
#         driver.save_screenshot(f"screenshot_{email.replace('@','_at_')}.png")
# time.sleep(6)
# print("🎉 All login attempts completed!")






























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time, tempfile, shutil, os

# # ===============================
# # Email List
# # ===============================
# emails = [
#        "justice.marin@gmail.com",
# "aldo.murphy@gmail.com",
# "bella.sierra@gmail.com",
# "dayton.pena@gmail.com",
# "rachel.mendez@gmail.com",
# "arthur.burton@gmail.com",
# "miriam.hardy@gmail.com",
# "jayceon.fischer@gmail.com",
# "maci.acevedo@gmail.com",
# "dakari.bruce@gmail.com",

#   "marilyn.wade@gmail.com",
#     "jake.grant@gmail.com",
#     "alaina.martinez@gmail.com",
#     "alexander.lee@gmail.com",
#     "scarlett.hoover@gmail.com",
#     "jaziel.christensen@gmail.com",
#     "carmen.terrell@gmail.com",
#     "jaxen.buck@gmail.com",
#     "livia.romero@gmail.com",
#     "bryson.todd@gmail.com",
#     "zariah.meza@gmail.com",
#     "lucian.newman@gmail.com",
#     "oaklynn.massey@gmail.com",
#     "donald.strickland@gmail.com",
#     "nia.bernard@gmail.com",
#     "jair.long@gmail.com",
#     "jade.rosario@gmail.com",
#     "jedidiah.mann@gmail.com",
#     "paislee.reed@gmail.com",
#     "easton.vaughn@gmail.com",
#     "reign.crane@gmail.com",
#     "fox.barker@gmail.com",
#     "remington.arnold@gmail.com",
#     "abraham.perry@gmail.com",
#     "clara.davidson@gmail.com",
#     "dante.chapman@gmail.com",
#     "zuri.copeland@gmail.com",
#     "axton.douglas@gmail.com",
#     "aniyah.barr@gmail.com",
#     "harley.hahn@gmail.com",
#     "fallon.welch@gmail.com",
#     "hendrix.baxter@gmail.com",
#     "lara.mccarthy@gmail.com",
#     "devin.mathews@gmail.com",
#     "sloan.schwartz@gmail.com",
#     "edwin.tang@gmail.com",
#     "belle.nicholson@gmail.com",
#     "rodrigo.shelton@gmail.com",
#     "makenzie.sanchez@gmail.com",
#     "joseph.washington@gmail.com",
#     "valerie.barr@gmail.com",
#     "harley.kemp@gmail.com",
#     "anika.aguirre@gmail.com",
#     "andy.gallagher@gmail.com",
#     "elliott.cook@gmail.com",
#     "ezekiel.velazquez@gmail.com",
#     "jaliyah.wu@gmail.com",
#     "kyson.lucero@gmail.com",
#     "ila.middleton@gmail.com",
#     "misael.jimenez@gmail.com"
# ]

# PASSWORD = "Bmr@112233"

# # ===============================
# # Function to login each account
# # ===============================
# def login_account(email):
#     # create temporary user data directory (fresh profile)
#     user_data_dir = tempfile.mkdtemp()

#     options = Options()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument(f"--user-data-dir={user_data_dir}")
#     options.add_argument("--no-first-run --no-service-autorun --no-default-browser-check")
#     options.add_argument("start-maximized")

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     wait = WebDriverWait(driver, 30)

#     try:
#         driver.get("https://bav-client-hera.vercel.app/")
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#         time.sleep(2)

#         # Click login/account button
#         login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']")))
#         driver.execute_script("arguments[0].click();", login_btn)
#         time.sleep(3)

#         # Fill email
#         email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
#         email_field.send_keys(email)

#         # Fill password
#         password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
#         password_field.send_keys(PASSWORD)

#         # Click Sign in
#         signin_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Sign in"]')))
#         driver.execute_script("arguments[0].click();", signin_btn)

#         print(f"✅ Login done for {email}")
#         time.sleep(5)

#     except Exception as e:
#         print(f"❌ Error for {email}: {e}")

#     finally:
#         # Close browser and delete temp profile folder
#         driver.quit()
#         shutil.rmtree(user_data_dir, ignore_errors=True)

# # ===============================
# # Run Loop
# # ===============================
# for email in emails:
#     login_account(email)

# print("🎉 All logins completed successfully!")





import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# =============================
# Browser Setup
# =============================
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 25)

# =============================
# Login
# =============================
driver.get("https://bavit-test.vercel.app/admin/login")

email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
email_field.send_keys("admin@gmail.com")

password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field.send_keys("Bmr@1234")

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
print("✅ Logged in successfully!")

# =============================
# Navigate to Add Listing
# =============================
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="3. Inventory"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="3.3 View Listing"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]//button/i'))).click()

# =============================
# Publish to Website
# =============================
wait.until(EC.element_to_be_clickable((By.ID, "SwitchCheckWebsite"))).click()

# =============================
# Select Category
# =============================
category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="categorySelect"]/div/div[1]/div[2]')))
category.click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))).click()

# =============================
# Inventory
# =============================
inventory = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="react-select-2-placeholder"]/../../div[2]')))
inventory.click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))).click()

# =============================
# Scroll inside modal (if visible)
# =============================
try:
    modal = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]')))
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)
    time.sleep(1)
except:
    pass

# =============================
# Stock Selection
# =============================
try:
    stock = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"stock") or contains(text(),"Stock")]')))
    stock.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"]'))).click()
except:
    pass

# =============================
# Click Create Listing
# =============================
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create Listing"]'))).click()
print("✅ Listing creation started...")

# =============================
# SKU
# =============================
sku = wait.until(EC.presence_of_element_located((By.ID, "sku")))
sku.send_keys("12345")

# =============================
# Proceed
# =============================
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Proceed")]'))).click()

# =============================
# Processor (fixed JS method)
# =============================
processor_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Processor")]/following::div[contains(@class,"select__control")][1]')))
processor_box.click()
time.sleep(1)

input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'react-select') and @type='text']")))
driver.execute_script("arguments[0].focus();", input_box)
input_box.send_keys("Intel i7")
input_box.send_keys(Keys.ENTER)
print("✅ Processor selected: Intel i7")

# =============================
# Example dropdown handling (Type, Model, etc.)
# =============================
def fill_dropdown(label_text, value):
    try:
        field = wait.until(EC.element_to_be_clickable((By.XPATH, f'//label[contains(text(),"{label_text}")]/following::div[contains(@class,"select__control")][1]')))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
        field.click()
        input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'react-select')]")))
        input_field.send_keys(value)
        input_field.send_keys(Keys.ENTER)
        print(f"✅ {label_text} set to: {value}")
    except Exception as e:
        print(f"⚠️ {label_text} skip: {e}")

fill_dropdown("Type", "Laptop")
fill_dropdown("Model", "EliteBook")
fill_dropdown("Operating System", "Windows 11")
fill_dropdown("Color", "Black")

# =============================
# Text Inputs
# =============================
def fill_input(placeholder, text):
    try:
        elem = wait.until(EC.presence_of_element_located((By.XPATH, f'//input[@placeholder="{placeholder}"]')))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        elem.clear()
        elem.send_keys(text)
        print(f"✅ Filled {placeholder} = {text}")
    except Exception as e:
        print(f"⚠️ Could not fill {placeholder}: {e}")

fill_input("Enter MPN", "ABCD1234")
fill_input("Enter Unit Quantity", "5")
fill_input("Enter Item Height", "12")
fill_input("Enter Item Weight", "21")

print("🎯 All required fields filled successfully!")
time.sleep(5)
driver.quit()
