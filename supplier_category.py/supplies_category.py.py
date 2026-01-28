from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Browser options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

# Driver setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# wait object create karo
wait = WebDriverWait(driver, 15)

# 1. Open login page
driver.get("https://testing.d1z4wu6myne6l0.amplifyapp.com/admin/login")
driver.maximize_window()
time.sleep(4)

# Scroll thoda niche
for i in range(2):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

# 2. Enter Email
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
email_field.send_keys("admin@gmail.com")
time.sleep(0.6)

# 3. Enter Password
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
password_field.send_keys("Bmr@1234")
time.sleep(0.6)

# 4. Click Login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()
time.sleep(0.6)

# 5. Click on supplier section
suppliers = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="2. Suppliers"]')))
suppliers.click()
time.sleep(2)

# 6. Click on supplier
View_Supplier_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="2.1 View Supplier Category"]')))
View_Supplier_Category.click()
time.sleep(2)

# 7. Add supplier category
Add_Supplier_Category = wait.until(EC.element_to_be_clickable((By.XPATH, ' //i[@class="ri-add-line tw-text-sm"]')))
Add_Supplier_Category.click()

#  enter your category name
Enter_Category = wait.until(EC.element_to_be_clickable((By.XPATH, ' //input[@id="name"] ')))
Enter_Category.send_keys("mini pc Supplier don")
time.sleep(3)

# 1. Type text in Product Categories input
product_categories = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//input[@autocapitalize="none"]'))
)
product_categories.send_keys("mini")
time.sleep(2)  # thoda rukna zaroori hai dropdown ke liye

# 2. Click first option in dropdown (mini pc)
first_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "mini pc")]'))
) 
first_option.click()

# Enter a description 
Enter_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@name="description"]')))
Enter_Category.send_keys(" new This category is created for testing purposes by Muhammad Yousaf Liaquat Ali Khan . It includes mini PCs and related products.")
time.sleep(2)

# new and old product selection option 
product_type = "new"   # ya "scrap" jo tum set karna chaho

if product_type.lower() == "new":
    new_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="new"]'))
    )
    new_option.click()
    print("✅ New Products selected")
else:
    scrap_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="scrap"]'))
    )
    scrap_option.click()
    print("✅ Scrap Products selected")

time.sleep(0.4)

# Scroll down
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(0.6)

# ✅ File upload section
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

# Agar input hidden hai to visible karo
driver.execute_script("arguments[0].style.display = 'block';", upload_input)

# Apni image ka full path send karo (extension zaroori hai)
upload_input.send_keys("./img/Image_1.png")

time.sleep(3) 

#Add supplier category

# Add_Supplier_Category = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mx-2 btn btn-primary"]')))
# Add_Supplier_Category.click()


time.sleep(8)

print("✅ Login and supplier section navigation done with image upload!")

driver.quit()
