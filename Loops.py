# for i in range(10):
#     print('*' * (i + 1))

# num= int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num}: {factorial}")

# # my_string = "Hello, World!"
# # vowel_count = 0
# # for char in my_string:
# #     if char.lower() in 'aeiou':
# #         vowel_count += 1
# # print("Number of vowels:", vowel_count)
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
    "justice.marin@gmail.com",
    "aldo.murphy@gmail.com",
    "bella.sierra@gmail.com",
    "dayton.pena@gmail.com",
    "rachel.mendez@gmail.com",
    "arthur.burton@gmail.com",
    "miriam.hardy@gmail.com",
    "jayceon.fischer@gmail.com",
    "maci.acevedo@gmail.com",
    "dakari.bruce@gmail.com",

    "marilyn.wade@gmail.com",
    "jake.grant@gmail.com",
    "alaina.martinez@gmail.com",
    "alexander.lee@gmail.com",
    "scarlett.hoover@gmail.com",
    "jaziel.christensen@gmail.com",
    "carmen.terrell@gmail.com",
    "jaxen.buck@gmail.com",
    "livia.romero@gmail.com",
    "bryson.todd@gmail.com",


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
for email in zip(emails):
    driver.get("https://bav-client-hera.vercel.app/")
    driver.maximize_window()
    time.sleep(3)

    # Click login
    login = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
    )
    login.click()
    time.sleep(4)

  

    email_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    email_field.send_keys(email)

    password = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))
    )
    password.send_keys("Bmr@112233")


    create_account = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Sign in"]'))
    )
    create_account.click()
    time.sleep(7)

    print(f"✅ Account created for:  ({email})")

print("🎉 All signups completed successfully!")
driver.quit()
