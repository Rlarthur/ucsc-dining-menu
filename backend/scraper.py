from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument("--headless=new") # comment for visual testing of functionality
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)
driver.get("https://nutrition.sa.ucsc.edu/")

try:
    # Wait for the dining hall links to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.locations a"))
    )

    # Find and click the “Slug Stop” link or whichever place we need menu data from
    for a in driver.find_elements(By.CSS_SELECTOR, "li.locations a"):
        if "Slug Stop" in a.text:
            a.click()
            break

    # Wait for menu items to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.shortmenurecipes span"))
    )

    # Collect and print item names
    items = [e.text.strip() for e in driver.find_elements(By.CSS_SELECTOR, "div.shortmenurecipes span") if e.text.strip()]
    print(" | ".join(items))

finally:
    driver.quit()

# Previous issue was cuased by Selenium using direct links to dining locations,
# which failed due to missing session cookies. Resolved by first loading the
# homepage to establish cookies before navigating to the deseried dining menu.