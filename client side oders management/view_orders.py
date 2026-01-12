import html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

from selenium.webdriver.common.keys import Keys

# --------------------------
# Browser options
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
driver.get("https://gamerpc-client-prod.vercel.app/")
driver.maximize_window()
time.sleep(2)

for _ in range(2):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(0.5)


# ----------------------------------------------------------------------------------------------
# 4) Navigate to client side  -> view orders  -> create order  -> add to cart -> go to checkout
# ----------------------------------------------------------------------------------------------

gaming_pc= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Gaming Pc"]')))
gaming_pc.click()
time.sleep(1)
#--------------------------------------------------------------        
             # click on  create order list 
# --------------------------------------------------------------

create_order= wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Network Equipments"]')))
create_order.click()
time.sleep(4)

#--------------------------------------------------------------
                # scroll down the page
html = driver.find_element(By.XPATH, "/html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(5)


# --------------------------------------------------------------             
             # click on  add to cart button 
# --------------------------------------------------------------
add_to_cart= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/button')))
add_to_cart.click()
time.sleep(3)

# --------------------------------------------------------------             
             # click on  Wishlist icon
# --------------------------------------------------------------
shoipping_icon= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Shopping cart"]')))
shoipping_icon.click()
time.sleep(3)

# --------------------------------------------------------------             
             # click on  go to cart button
# --------------------------------------------------------------
go_to_checkout= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Go to Checkout"]')))
go_to_checkout.click()
time.sleep(4)


driver.execute_script("window.scrollBy(0, 100);")
time.sleep(1)


email_address= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="your@email.com"]')))
email_address.send_keys("jon.blake@demoemail.com")
time.sleep(3)


first_name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="John"]')))
first_name.send_keys("jack")
time.sleep(1)


last_name= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Doe"]')))
last_name.send_keys("son")
time.sleep(1)



street_address= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="123 Main Street"]')))
street_address.send_keys("street  number 45")
time.sleep(1)



city= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="New York"]')))
city.send_keys("Waterford")
time.sleep(1)

# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1)

# placeholder="10001"

state_Region= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="NY"]')))
state_Region.send_keys("Mason Brown")
time.sleep(1)



state_Region= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="10001"]')))
state_Region.send_keys("B15 2TT")
time.sleep(4)



phone_number= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="phone"]')))
phone_number.send_keys("+44 7876 304192")
time.sleep(3)

html.send_keys(Keys.PAGE_DOWN)
time.sleep(4)

Continue_to_Payment= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Continue to Payment"]')))
Continue_to_Payment.click()
time.sleep(3)



popup_guest_button= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Continue as Guest"]')))
popup_guest_button.click()
time.sleep(5)



html.send_keys(Keys.PAGE_DOWN)
time.sleep(4)

# cart=  wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Field-numberInput"]')))
# cart.send_keys("4242424242424242")
# time.sleep(8)


# # Switch to the iframe first (use correct index or XPath)
# iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@name,"__privateStripeFrame")]')))
# driver.switch_to.frame(iframe)

# # Now find the field and interact
# cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Field-numberInput"]')))
# cart.click()
# cart.send_keys("4242424242424242")

# # Switch back to main content
# driver.switch_to.default_content()

# time.sleep(3)




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_stripe_field(driver, wait, field_xpath, value, iframe_hint=None, timeout=10):
    """
    Attempts to find the iframe that contains the target field (field_xpath).
    Loops through candidate iframes and switches into the correct one, then fills value.
    iframe_hint: optional partial attribute to prefer certain iframes (like 'card' or '__privateStripeFrame')
    """
    # get candidate iframes (common Stripe pattern)
    candidates = driver.find_elements(By.XPATH, '//iframe[contains(@name,"__privateStripeFrame") or contains(@src,"stripe") or contains(@title,"Secure card")]')

    # if none found, try any iframe on page
    if not candidates:
        candidates = driver.find_elements(By.TAG_NAME, "iframe")

    last_err = None
    for idx, fr in enumerate(candidates):
        try:
            # switch to default first then to this iframe
            driver.switch_to.default_content()
            driver.switch_to.frame(fr)
            # small wait for element presence inside this iframe
            el = WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, field_xpath)))
            # if found, try to make it clickable / focus and send keys
            try:
                WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, field_xpath)))
            except:
                pass
            elem = driver.find_element(By.XPATH, field_xpath)
            elem.click()
            time.sleep(0.2)
            elem.clear()
            elem.send_keys(value)
            driver.switch_to.default_content()
            return True  # success
        except Exception as e:
            last_err = e
            # not the right iframe — continue to next
            continue

    # none matched
    driver.switch_to.default_content()
    print(f"[!] Could not find field {field_xpath} in any iframe. Last error: {last_err}")
    return False

# --- USAGE ---

# ensure wait is defined earlier:
# wait = WebDriverWait(driver, 15)

# 1) Card number
filled = fill_stripe_field(driver, wait, '//*[@id="Field-numberInput"]', "4242424242424242")
time.sleep(1)

# 2) Expiry — sometimes stripe expects MM/YY or MMYY; try common formats
if not fill_stripe_field(driver, wait, '//*[@id="Field-expiryInput"]', "12/26"):
    # fallback formats
    fill_stripe_field(driver, wait, '//*[@id="Field-expiryInput"]', "1226")
time.sleep(1)

# 3) CVC (use placeholder match if id differs)
# common CVC XPaths: //*[@placeholder='CVC']  or //*[@id='Field-cvcInput'] etc.
filled_cvc = fill_stripe_field(driver, wait, '//*[@placeholder="CVC"]', "124")
if not filled_cvc:
    # alternative: try placeholder lower/upper or name contains cvc
    fill_stripe_field(driver, wait, "//*[contains(translate(@placeholder,'cvc','CVC'),'CVC')]", "124")
time.sleep(1)





# Email= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="you@example.com"]')))
# Email.send_keys("jon.blake@demoemail.com")
# time.sleep(1)



# mobile_number = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="0301 2345678"]')))
# mobile_number.send_keys("03240644978")
# time.sleep(7)



payment = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div[2]/section/div/div[2]/div[2]/form/button')))

# payment.click()

inject_badge = """
var badge = document.createElement('div');
badge.innerText = '🔧 Automated by Yousaf khan';
badge.style.position = 'fixed';
badge.style.top = '10px';
badge.style.right = '10px';
badge.style.backgroundColor = '#1e1e1e';
badge.style.color = '#00ffcc';
badge.style.padding = '8px 14px';
badge.style.borderRadius = '8px';
badge.style.fontSize = '14px';
badge.style.fontFamily = 'Arial, sans-serif';
badge.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';
badge.style.zIndex = '9999';
document.body.appendChild(badge);
"""

driver.execute_script(inject_badge)
driver.execute_script("console.log('✅ Automation started by Yousaf khan');")
print("khan  injected the vs successfully.")

# time.sleep(3)
# html.send_keys(Keys.PAGE_DOWN)
# time.sleep(1)

# html.send_keys(Keys.PAGE_DOWN)

time.sleep(15)