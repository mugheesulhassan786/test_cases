# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time
# from selenium.webdriver.common.keys import Keys


# # Browser options
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )

# # Driver setup
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # 1. Open bavit login page directly
# driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/")
# driver.maximize_window()
# time.sleep(3)

# # Wait and click on login button
# login = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
# )
# login.click()
# time.sleep(4)

# # Scroll 1000px niche
# scroll=driver.find_element(By.XPATH,'/html')
# scroll.send_keys(Keys.PAGE_DOWN)
# time.sleep(2)

# # Wait and click on Sign Up
# click_sign_up = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//a[@class='text-sm font-medium text-red-600 hover:text-red-700 transition-colors']"))
# )
# click_sign_up.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 100);")

# time. sleep(4)
# # 2. Enter full name
# fullName = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//input[@name="fullName"]'))
# )
# fullName.send_keys("Salar Khan")   # <-- apna name likh
# time.sleep (3)
# # 2. Enter Email
# email_field = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
# )
# email_field.send_keys("Abrarahmed@gmail.com")   # <-- apna email likh
# time.sleep (3)
# # valid password
# password = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))
# )
# password.send_keys("Bmr@112233")   # <-- apna email likh
# scroll=driver.find_element(By.XPATH,'/html')
# scroll.send_keys(Keys.PAGE_DOWN)
# time.sleep(2)
# #confirmPassword
# confirmPassword = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]'))
# )
# confirmPassword.send_keys("Bmr@112233")   # <-- apna email likh
# time.sleep(2)

# # Click Create Account
# agree_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="terms"]'))
#     )
# agree_btn.click()
# # Wait and click on login button
# login = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[text()="Create account"]'))
# )
# login.click()
# time.sleep(7)
# print("✅ Successfully scrolled and clicked on Sign Up")







############################################
#####################################3
######################################3
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time

# # Sample data
# names = [f"User{i}" for i in range(1, 21)]
# emails = [f"user{i}@example.com" for i in range(1, 21)]
# passwords = [f"Pass{i}@123" for i in range(1, 21)]

# # Browser options
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )

# # Driver setup
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# for i in range(20):
#     name = names[i]
#     email = emails[i]
#     password_value = passwords[i]

#     # 1. Open signup page
#     driver.get("https://bav-client-kohl.vercel.app/auth/signup")
#     driver.maximize_window()
#     time.sleep(3)

#     # Click on login icon
#     login = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
#     )
#     login.click()
#     time.sleep(4)

#     # Scroll down
#     scroll = driver.find_element(By.XPATH, '/html')
#     scroll.send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)

#     # Click on Sign Up
#     click_sign_up = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//a[@class='text-sm font-medium text-red-600 hover:text-red-700 transition-colors']")
#         )
#     )
#     click_sign_up.click()
#     time.sleep(3)
#     driver.execute_script("window.scrollBy(0, 100);")
#     time.sleep(4)

#     # Fill full name
#     fullName = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@name="fullName"]'))
#     )
#     fullName.send_keys(name)
#     time.sleep(2)

#     # Fill email
#     email_field = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
#     )
#     email_field.send_keys(email)
#     time.sleep(2)

#     # Fill password
#     password = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))
#     )
#     password.send_keys(password_value)
#     time.sleep(2)

#     # Scroll down
#     scroll.send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)

#     # Confirm password
#     confirmPassword = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]'))
#     )
#     confirmPassword.send_keys(password_value)
#     time.sleep(2)
# # Click Create Account
#     agree_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="terms"]'))
#     )
#     agree_btn.click()
#     # Click Create Account
#     create_account = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[text()="Create account"]'))
#     )
#     create_account.click()
#     time.sleep(4)

#      #####################################################################

#                  # Login to admin and verify user creation

#      #####################################################################
#  # Fill email
#     email_field_1 = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@name="email"]'))
#     )
#     email_field_1.send_keys(email)
#     time.sleep(2)

#     # Fill password
#     password_1 = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@name="password"]'))
#     )
#     password_1.send_keys(password_value)
#     time.sleep(2)

#     # Scroll down
#     scroll.send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)



#     # Click Create Account
#     create_account = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[text()="Sign in"]'))
#     )
#     create_account.click()

#     time.sleep(7)

#     print(f"✅ Account created for {name} | {email}")

# driver.quit()


















###########################################
##########################################





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# ===============================
# Email aur Name Lists
# ===============================
emails = [
   "logan.whitaker@gmail.com",
"serena.calderon@gmail.com",
"miles.hensley@gmail.com",
"ayla.morrow@gmail.com",
"declan.velez@gmail.com",
"jasmine.porter@gmail.com",
"kyler.donovan@gmail.com",
"elena.shepard@gmail.com",
"grayson.tate@gmail.com",
"nova.harrington@gmail.com",


    # "marilyn.wade@gmail.com",
    # "jake.grant@gmail.com",
    # "alaina.martinez@gmail.com",
    # "alexander.lee@gmail.com",
    # "scarlett.hoover@gmail.com",
    # "jaziel.christensen@gmail.com",
    # "carmen.terrell@gmail.com",
    # "jaxen.buck@gmail.com",
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
]

names = [
 "Logan Whitaker",
"Serena Calderon",
"Miles Hensley",
"Ayla Morrow",
"Declan Velez",
"Jasmine Porter",
"Kyler Donovan",
"Elena Shepard",
"Grayson Tate",
"Nova Harrington",

    # "Marilyn Wade",
    # "Jake Grant",
    # "Alaina Martinez",
    # "Alexander Lee",
    # "Scarlett Hoover",
    # "Jaziel Christensen",
    # "Carmen Terrell",
    # "Jaxen Buck",
    # "Livia Romero",
    # "Bryson Todd",
    # "Zariah Meza",
    # "Lucian Newman",
    # "Oaklynn Massey",
    # "Donald Strickland",
    # "Nia Bernard",
    # "Jair Long",
    # "Jade Rosario",
    # "Jedidiah Mann",
    # "Paislee Reed",
    # "Easton Vaughn",
    # "Reign Crane",
    # "Fox Barker",
    # "Remington Arnold",
    # "Abraham Perry",
    # "Clara Davidson",
    # "Dante Chapman",
    # "Zuri Copeland",
    # "Axton Douglas",
    # "Aniyah Barr",
    # "Harley Hahn",
    # "Fallon Welch",
    # "Hendrix Baxter",
    # "Lara McCarthy",
    # "Devin Mathews",
    # "Sloan Schwartz",
    # "Edwin Tang",
    # "Belle Nicholson",
    # "Rodrigo Shelton",
    # "Makenzie Sanchez",
    # "Joseph Washington",
    # "Valerie Barr",
    # "Harley Kemp",
    # "Anika Aguirre",
    # "Andy Gallagher",
    # "Elliott Cook",
    # "Ezekiel Velazquez",
    # "Jaliyah Wu",
    # "Kyson Lucero",
    # "Ila Middleton",
    # "Misael Jimenez"
]

# ===============================
# Browser setup
# ===============================
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ===============================
# Automation Loop
# ===============================
for name, email in zip(names, emails):
    driver.get("https://gamerpc-client-prod.vercel.app/")
    driver.maximize_window()
    time.sleep(3)

    # Click login
    login = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
    )
    login.click()
    time.sleep(4)

    # Scroll & click Sign Up
    scroll = driver.find_element(By.XPATH, '/html')
    scroll.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    click_sign_up = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='text-sm font-medium text-red-600 hover:text-red-700 transition-colors']"))
    )
    click_sign_up.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(2)

    # Fill form
    fullName = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="fullName"]'))
    )
    fullName.send_keys(name)

    email_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    email_field.send_keys(email)

    password = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))
    )
    password.send_keys("Bmr@112233")

    confirmPassword = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="confirmPassword"]'))
    )
    confirmPassword.send_keys("Bmr@112233")

    # Agree and submit
    agree_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="terms"]'))
    )
    agree_btn.click()

    create_account = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Create account"]'))
    )
    create_account.click()
    time.sleep(7)

    print(f"✅ Account created for: {name} ({email})")

print("🎉 All signups completed successfully!")
driver.quit()
