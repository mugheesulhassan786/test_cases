# import html
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time
# import random

# from selenium.webdriver.common.keys import Keys

# # --------------------------
# # Browser options
# # --------------------------
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 20)

# # --------------------------
# # 3) Login
# # --------------------------
# driver.get("https://bavit-test.vercel.app/admin/login")
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

# # ----------------------------------------------------------------------------------------------
# # 4) Navigate to inventory -> View listing -> Add listing
# # ----------------------------------------------------------------------------------------------

# accounting= wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="11. Accounting"]')))
# accounting.click()
# time.sleep(1.0)
# # # ✅ Sidebar ko bottom tak scroll karo
# # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", accounting)

# # # ✅ Agar thoda thoda scroll karna ho (step by step)
# # driver.execute_script("arguments[0].scrollBy(1, 100);", accounting)  #


#   ######################## 

#   # Element locate karo
# element = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[1]')

# # Mid tak scroll karne ke liye JavaScript
# driver.execute_script("""
#     const el = arguments[0];
#     el.scrollTop = (el.scrollHeight - el.clientHeight) / 2;
# """, element)

# time.sleep(2)


# View_taxation= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="11.4 View Taxation"]')))
# View_taxation.click()
# time.sleep(1.0)

# Add_Expense = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add Tax Record"]')))
# Add_Expense.click()
# time.sleep(3)

# ###########


# taxation_title = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter taxation title"]')))
# taxation_title.send_keys("Yousaf  automation tester")
# time.sleep(1)

# description = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Enter detailed description"]')))
# description.send_keys("As an Automation Tester at our tech shop, you are the gatekeeper of quality and efficiency. ")
# time.sleep(3)


# VAT_Rate = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="vatRate"]')))
# VAT_Rate.send_keys("1.02")
# time.sleep(1)

# VAT_Amount = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="vatAmount"]')))
# VAT_Amount.send_keys("100")
# time.sleep(1)
# html = driver.find_element(By.XPATH, "/html")
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(0.6)


# Create_Taxation_Record= wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Create Taxation Record"]')))
# print("Creating Taxation Record...")
# time.sleep(2)
# Create_Taxation_Record.click()
# time.sleep(8)



# print("Taxation Record created successfully.")  




import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# 1
# Automation script: View Revenue -> Add Revenue
# 2
# This file is a cleaned and robust version of your original script.
# 3
def create_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
# 4
def wait_for_ready(driver, timeout=20):
    wait = WebDriverWait(driver, timeout)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    return wait
# 5
def safe_click(driver, wait, by, selector, overlay_selectors=None, scroll=True):
    overlay_selectors = overlay_selectors or [".modal", ".modal-backdrop", ".overlay", ".spinner"]
    element = wait.until(EC.element_to_be_clickable((by, selector)))
    if scroll:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
    # wait overlays to disappear
    for sel in overlay_selectors:
        try:
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, sel)))
        except Exception:
            pass
    try:
        element.click()
    except Exception:
        # fallback to JS click
        driver.execute_script("arguments[0].click();", element)
    return element
# 6
def scroll_container_by(driver, wait, container_xpath, dy=300, steps=1, pause=0.2):
    container = wait.until(EC.presence_of_element_located((By.XPATH, container_xpath)))
    for _ in range(steps):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[1];", container, dy)
        time.sleep(pause)
    return container
# 7
def upload_file(driver, wait, file_input_xpath, file_path):
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, file_input_xpath)))
    # make visible if hidden
    driver.execute_script("arguments[0].removeAttribute('hidden'); arguments[0].style.display='block';", upload_input)
    upload_input.send_keys(file_path)
    return upload_input
# 8
def main():
    driver = create_driver()
    wait = wait_for_ready(driver, 20)

    # open site and login
    driver.get("https://bavit-test.vercel.app/admin/login")
    driver.maximize_window()
    time.sleep(2)

    # tiny scroll to ensure elements lazy load
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(0.5)

    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
    email_field.clear()
    email_field.send_keys("admin@gmail.com")

    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    password_field.clear()
    password_field.send_keys("Bmr@1234")

    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_btn.click()
    time.sleep(2)

    # Navigate sidebar to Accounting -> View Revenue -> Add Revenue
    accounting_xpath = '//span[text()="11. Accounting"]'
    safe_click(driver, wait, By.XPATH, accounting_xpath)
    time.sleep(0.7)

    # scroll the main sidebar container (dialog) to reveal deeper items
    dialog_xpath = '//div[@role="dialog"]'
    scroll_container_by(driver, wait, dialog_xpath, dy=300, steps=2)

    view_xpath = '//*[text()="11.5 View Revenue"]'
    safe_click(driver, wait, By.XPATH, view_xpath)
    time.sleep(0.8)

    add_rev_xpath = '//*[text()="Add Revenue"]'
    safe_click(driver, wait, By.XPATH, add_rev_xpath)
    time.sleep(1.2)

    # Now on Add Revenue form
    # Select Revenue category
    revenue_cat_xpath = '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[1]/div[1]/div[1]/div/div[2]/div'
    safe_click(driver, wait, By.XPATH, revenue_cat_xpath)
    # choose first option
    opt_xpath = '//div[contains(@id,"react-select") and @role="option"][1]'
    safe_click(driver, wait, By.XPATH, opt_xpath)
    time.sleep(0.8)

    # Revenue receive type
    recv_type_xpath = '//*[@id="layout-wrapper"]/div[3]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]'
    safe_click(driver, wait, By.XPATH, recv_type_xpath)
    safe_click(driver, wait, By.XPATH, opt_xpath)
    time.sleep(0.8)

    # Amount, title, description
    amt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="amount"]')))
    amt.clear()
    amt.send_keys("1.02")
    time.sleep(0.4)

    title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter revenue title"]')))
    title.clear()
    title.send_keys("Automation Tester")
    time.sleep(0.4)

    desc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter revenue description"]')))
    desc.clear()
    desc.send_keys("As an Automation Tester at our tech shop, you are the gatekeeper of quality and efficiency.")
    time.sleep(0.4)

    # Scroll page down to reveal file upload
    page_html = driver.find_element(By.TAG_NAME, "html")
    page_html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.6)

    # File upload
    file_input_xpath = '//input[@type="file"]'
    file_path = "./img/Image_1.png"
    upload_file(driver, wait, file_input_xpath, file_path)
    time.sleep(1.0)

    # Finalize: click Add/Submit if present
    submit_xpath_candidates = [
        '//*[text()="Add Revenue"]',
        '//button[@type="submit" and (contains(.,"Add") or contains(.,"Submit"))]'
    ]
    submitted = False
    for sx in submit_xpath_candidates:
        try:
            btn = wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
            # ensure overlays gone
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal, .modal-backdrop, .overlay, .spinner")))
            btn.click()
            submitted = True
            break
        except Exception:
            continue

    if not submitted:
        print("Submit button not found; aborting save.")
    else:
        # wait for success notification or redirect
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"success") or contains(.,"Success") or contains(.,"added")]')))
        except Exception:
            pass

    # Optional: take a screenshot for record
    try:
        driver.save_screenshot("add_revenue_result.png")
    except Exception:
        pass

    # Clean up and close
    time.sleep(2)
    driver.quit()
# 9

if __name__ == "__main__":
    main()