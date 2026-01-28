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
driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
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
View_Blog= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="15.2 View Blogs"]')))
View_Blog.click()

time.sleep(2)


Add_Blogs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blog"]')))
Add_Blogs.click()
time.sleep(2)

# # Dropdown element wait karke click
# Blog_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[1]/div[1]/div/div[1]/div[2]')))
# Blog_Category.click()
# time.sleep(1)

# # Dropdown ke second option select karna
# select = Select(Blog_Category)
# select.select_by_index(1)  # index 0 = first option, 1 = second option

# 1. Type text in Product Categories input
Blog_Category = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[1]/div[1]/div/div[1]/div[2]'))
)
Blog_Category.click()
# Blog_Category.send_keys("you")
time.sleep(2)  # thoda rukna zaroori hai dropdown ke liye

first_option_danger = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id,"react-select") and @role="option"][2]'))
    )
first_option_danger.click()
time.sleep(3)                           

# Blog_Category= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-22-input"]')))
# Blog_Category.send_keys("Yousaf is testing")
# time.sleep(2)

Title= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter blog title"]')))
Title.send_keys("testing")
time.sleep(2)

# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(2)

Cover_Image_Alt_Text= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter cover image alt text"]')))
Cover_Image_Alt_Text.send_keys("Description  is testing by Yousaf")
time.sleep(2)


# ✅ Step 1: Wait for input field to be clickable
Bundle_Name_4 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@placeholder="Press Enter or add comma (,) to create a keyword"]'
)))

# ✅ Step 2: Send new value + press Enter
Bundle_Name_4.send_keys("automation")
Bundle_Name_4.send_keys(Keys.ENTER)   # 👈 Enter key press
time.sleep(2)
Bundle_Name_4 = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@placeholder="Press Enter or add comma (,) to create a keyword"]'
)))

# ✅ Step 2: Send new value + press Enter
Bundle_Name_4.send_keys("tester")
Bundle_Name_4.send_keys(Keys.ENTER)   # 👈 Enter key press
time.sleep(2)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

SEO= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter SEO title"]')))
SEO.send_keys("Future of Work: Automation and Algorithms")
time.sleep(2)

Author_Name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[6]/input')))
Author_Name.send_keys("testing")
time.sleep(3)

content= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@contenteditable="true"]')))
content.send_keys("Experience music like never before with our Wireless Bluetooth Headphones, designed for crystal-clear audio, deep bass, and a comfortable fit. Whether you’re working, traveling, or relaxing, these headphones give you uninterrupted sound with advanced noise cancellation technology.")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)


# ✅ Step 1: File input locate karo
upload_input = wait.until(EC.presence_of_element_located((
    By.XPATH, '//input[@type="file"]'
)))

# ✅ Step 2: Apni file ka path bhejo
file_path = "./img/Image_1.png"
upload_input.send_keys(file_path)

time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

#Publish Blog

# Publish_Blog= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Publish Blog"]')))
# Publish_Blog.click()
time.sleep(10)


































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
# # 1) Browser Setup
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
# # 2) Login
# # ============================================================
# driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
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

# # 3) Navigate to policies -> view FAQs category  -> Add FAQs
# # ============================================================

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

# # Ab "View FAQ Category" pe click karo
# View_Blog= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="16.2 View Blogs"]')))
# View_Blog.click()
# time.sleep(2)


# # ✅ Yahan se loop start ho raha hai (50 blogs)
# for i in range(1, 51):

#     Add_Blogs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Blog"]')))
#     Add_Blogs.click()
#     time.sleep(2)

#     Blog_Category = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[1]/div[1]/div/div[1]/div[2]'))
#     )
#     Blog_Category.click()
#     time.sleep(2)

#     first_option = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "yousaf is testing")]'))
#     ) 
#     first_option.click()
#     time.sleep(3)

#     Title= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter blog title"]')))
#     Title.send_keys(f"testing blog {i}")
#     time.sleep(2)

#     Cover_Image_Alt_Text= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter cover image alt text"]')))
#     Cover_Image_Alt_Text.send_keys(f"Description is testing by Yousaf #{i}")
#     time.sleep(2)

#     Bundle_Name_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Press Enter or add comma (,) to create a keyword"]')))
#     Bundle_Name_4.send_keys(f"automation{i}")
#     Bundle_Name_4.send_keys(Keys.ENTER)
#     time.sleep(1)
#     Bundle_Name_4.send_keys(f"tester{i}")
#     Bundle_Name_4.send_keys(Keys.ENTER)
#     time.sleep(2)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     SEO= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Enter SEO title"]')))
#     SEO.send_keys(f"Future of Work: Automation and Algorithms #{i}")
#     time.sleep(2)

#     Author_Name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div/div[6]/input')))
#     Author_Name.send_keys("testing")
#     time.sleep(3)

#     content= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@contenteditable="true"]')))
#     content.send_keys(f"Experience music automation loop blog number {i}.")
#     time.sleep(3)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(1)

#     upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
#     file_path = "./img/Image_1.png"
#     upload_input.send_keys(file_path)
#     time.sleep(2)

#     driver.execute_script("window.scrollBy(0, 200);")
#     time.sleep(2)

#     Publish_Blog= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Publish Blog"]')))
#     Publish_Blog.click()
#     time.sleep(5)

#     print(f"✅ Blog {i} published successfully!")

# time.sleep(10)
# driver.quit()
