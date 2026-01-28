from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# --------------------------
# Login Function
# --------------------------
def login(driver, wait):
    driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")   # <-- yahan apna actual URL dalna
    driver.maximize_window()

    # Example login steps (update locators as per your login page)
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.send_keys("admin@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Bmr@1234")

    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_btn.click()

    print("✅ Logged in successfully")
    time.sleep(3)


# --------------------------
# Module 3.1: View Product Catalogue
# --------------------------
def view_product_catalogue(driver, wait):
    inventory = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Inventory')]")))
    inventory.click()

    view_catalogue = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Product Catalogue')]")))
    view_catalogue.click()

    print("✅ View Product Catalogue opened")
    time.sleep(2)


# --------------------------
# Module 3.2: View Stock
# --------------------------
def view_stock(driver, wait):
    inventory = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Inventory')]")))
    inventory.click()

    view_stock_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Stock')]")))
    view_stock_btn.click()

    print("✅ View Stock opened")
    time.sleep(2)


# --------------------------
# Module 3.3: View Listing
# --------------------------
def view_listing(driver, wait):
    inventory = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Inventory')]")))
    inventory.click()

    view_listing_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Listing')]")))
    view_listing_btn.click()

    print("✅ View Listing opened")
    time.sleep(2)


# --------------------------
# Main Flow
# --------------------------
def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 20)

    try:
        login(driver, wait)
        view_product_catalogue(driver, wait)
        view_stock(driver, wait)
        view_listing(driver, wait)

        print("🎉 All Inventory modules executed successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
