"""
======================================================
   🔒 PRIVATE AUTOMATION SCRIPT 🔒
   Author: YOUSAF LIAQUAT ALI KHAN
   Note: This script is written by YOUSAF LIAQUAT ALI KHAN only.
   Do not copy, modify, or reuse without permission.
======================================================
"""

import time
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import Select


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

# Scroll down a bit before login
for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)

# Enter login details
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field.send_keys("admin@gmail.com")

password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field.send_keys("Bmr@1234")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(5)

# 3) Navigate to policies -> view FAQs category  -> Add FAQs
# ============================================================

# Wait until Policies menu appears and click
Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
Gamers.click()
time.sleep(1)

# Sidebar locate karo
sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# Element locate karo
layout_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# --- Scroll step by step (smooth) ---
for _ in range(3):   # jitna neeche le jana ho utna loop
    driver.execute_script("arguments[0].scrollBy(0, 300);", layout_div)
    time.sleep(1)

# --- OR direct neeche tak scroll karna ho to ---
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", layout_div)


# Ab "View FAQ Category" pe click karo
View_Blog_Category= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15.1 View Blog Category"]')))
View_Blog_Category.click()

time.sleep(2)


Add_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Category"]')))
Add_Category.click()
time.sleep(2)


Name_feild = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category name"]')))
Name_feild.send_keys("Yousaf is testing")
time.sleep(2)

Description= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
Description.send_keys("Description  is testing by Yousaf")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(2)


# ✅ Dropzone ke andar actual input[type="file"] dhundo
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# ✅ Apni file ka full path do (rename karke simple naam rakhna)
file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
upload_input.send_keys(file_path)
time.sleep(4)


driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)



# Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blog Category"]')))
# Add_Button.click()


time.sleep(4)











































# """
# ======================================================
#    🔒 PRIVATE AUTOMATION SCRIPT 🔒
#    Author: YOUSAF LIAQUAT ALI KHAN
#    Note: This script is written by YOUSAF LIAQUAT ALI KHAN only.
#    Do not copy, modify, or reuse without permission.
# ======================================================
# """

# import time
# import html
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.support.ui import Select


# # ============================================================
# #                 1) Browser Setup
# # ============================================================
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # ============================================================
# #                  2) Login
# # ============================================================
# driver.get("https://bavit-test.vercel.app/admin/login")
# driver.maximize_window()
# time.sleep(2)

# # Scroll down a bit before login
# for _ in range(2):
#     driver.execute_script("window.scrollBy(0, 800);")
#     time.sleep(0.5)

# # Enter login details
# email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field.send_keys("admin@gmail.com")

# password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(5)

# # ============================================================
# #  3) Navigate to Gamers Community -> Blog Category Section
# # ============================================================

# # Wait until Gamers menu appears and click
# Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="16. Gamers Community"]')))
# Gamers.click()
# time.sleep(1)

# # Sidebar locate karo
# sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# # Element locate karo
# layout_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# # --- Scroll step by step (smooth) ---
# for _ in range(3):   # jitna neeche le jana ho utna loop
#     driver.execute_script("arguments[0].scrollBy(0, 300);", layout_div)
#     time.sleep(1)

# # --- OR direct neeche tak scroll karna ho to ---
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", layout_div)

# # Ab "View Blog Category" pe click karo
# View_Blog_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="16.1 View Blog Category"]')))
# View_Blog_Category.click()
# time.sleep(2)


# # ============================================================
# #   4) Add Blog Categories in Loop (50 times)
# # ============================================================
# for i in range(1, 51):   # 1 se 50 tak chalega
#     Add_Blogs_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blogs Category"]')))
#     Add_Blogs_Category.click()
#     time.sleep(2)

#     Name_feild = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category name"]')))
#     Name_feild.clear()
#     Name_feild.send_keys(f"Yousaf Testing Category {i}")   # unique name
#     time.sleep(1)

#     Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
#     Description.clear()
#     Description.send_keys(f"Description for Category {i} - automated by Yousaf")
#     time.sleep(1)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     # ✅ File upload
#     upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
#     driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
#     driver.execute_script("arguments[0].style.display = 'block';", upload_input)

#     file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
#     upload_input.send_keys(file_path)
#     time.sleep(2)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     # ✅ Submit button
#     Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blog Category"]')))
#     Add_Button.click()
#     time.sleep(3)

#     print(f"✅ Category {i} added successfully")

# print("🎉 50 categories added successfully!")








           ###############################
                    # dev env 
              ###############################






# """
# ======================================================
#    🔒 PRIVATE AUTOMATION SCRIPT 🔒
#    Author: YOUSAF LIAQUAT ALI KHAN
#    Note: This script is written by YOUSAF LIAQUAT ALI KHAN only.
#    Do not copy, modify, or reuse without permission.
# ======================================================
# """

# import time
# import html
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.support.ui import Select


# # ============================================================
# #                 1) Browser Setup
# # ============================================================
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # ============================================================
# #                  2) Login
# # ============================================================
# driver.get("https://gamerpc-test.vercel.app/admin/login")
# driver.maximize_window()
# time.sleep(2)

# # Scroll down a bit before login
# for _ in range(2):
#     driver.execute_script("window.scrollBy(0, 800);")
#     time.sleep(0.5)

# # Enter login details
# email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
# email_field.send_keys("admin@gmail.com")

# password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
# password_field.send_keys("Bmr@1234")

# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
# login_button.click()
# time.sleep(5)

# # ============================================================
# #  3) Navigate to Gamers Community -> Blog Category Section
# # ============================================================

# # Wait until Gamers menu appears and click
# # Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
# # Gamers.click()
# # time.sleep(1)

# # # Sidebar locate karo
# # sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
# # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

# # # Element locate karo
# # layout_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[1]')))

# # # --- Scroll step by step (smooth) ---
# # for _ in range(3):   # jitna neeche le jana ho utna loop
# #     driver.execute_script("arguments[0].scrollBy(0, 300);", layout_div)
# #     time.sleep(1)

# # # --- OR direct neeche tak scroll karna ho to ---
# # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", layout_div)

# # # Ab "View Blog Category" pe click karo
# # View_Blog_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15.1 View Blog Category"]')))
# # View_Blog_Category.click()
# # time.sleep(2)
# # ...existing code...
# Gamers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15. Gamers Community"]')))
# Gamers.click()
# time.sleep(1)

# # Sidebar locate karo and scroll it (use the actual scrollable container)
# sidebar = wait.until(EC.presence_of_element_located((By.ID, "sidebarApps")))
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)

# # optional smooth small scrolls if needed
# for _ in range(3):
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 300;", sidebar)
#     time.sleep(0.5)

# # Ab "View Blog Category" pe click karo — wait for clickable (no trailing dot)
# View_Blog_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15.1 View Blog Category"]')))
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", View_Blog_Category)
# View_Blog_Category.click()
# time.sleep(2)
# # ...existing code...

# # ============================================================
# #   4) Add Blog Categories in Loop (50 times)
# # ============================================================
# for i in range(1, 51):   # 1 se 50 tak chalega
#     Add_Blogs_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blogs Category"]')))
#     Add_Blogs_Category.click()
#     time.sleep(2)

#     Name_feild = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category name"]')))
#     Name_feild.clear()
#     Name_feild.send_keys(f"Yousaf Testing Category {i}")   # unique name
#     time.sleep(1)

#     Description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter category description"]')))
#     Description.clear()
#     Description.send_keys(f"Description for Category {i} - automated by Yousaf")
#     time.sleep(1)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     # ✅ File upload
#     upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
#     driver.execute_script("arguments[0].removeAttribute('hidden');", upload_input)
#     driver.execute_script("arguments[0].style.display = 'block';", upload_input)

#     file_path = r"C:\Users\M Yunas Khan\Downloads\HPLaptop.png"
#     upload_input.send_keys(file_path)
#     time.sleep(3)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(2)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     # ✅ Submit button
#     # Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blog Category"]')))
#     # Add_Button.click()
#     # time.sleep(6)

#     print(f"✅ Category {i} added successfully")

# print("🎉 50 categories added successfully!")
