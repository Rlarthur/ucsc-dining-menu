from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument("--headless=new") # comment for visual testing of functionality
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)
driver.get("https://nutrition.sa.ucsc.edu/")

## I dont understand selenium, tried to turn this into a loop, didnt work so I am trying the long and bad way(mult try and finally)
colleges = ["John R. Lewis & College Nine Dining Hall",
            "Cowell & Stevenson Dining Hall",
            "Crown & Merrill Dining Hall and Banana Joe's",
            "Porter & Kresge Dining Hall",
            "Rachel Carson & Oakes Dining Hall"]
#try:
    # Wait for the dining hall links to appear
#    WebDriverWait(driver, 10).until(
#        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.locations a"))
#    )
    
    # Find and click the “Slug Stop” link or whichever place we need menu data from
#    for a in driver.find_elements(By.CSS_SELECTOR, "li.locations a"):
#        if colleges[0] in a.text: #"Slug Stop" in a.text:
#            a.click()
#            break

    # Wait for menu items to load
#    WebDriverWait(driver, 10).until(
#        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.shortmenumeals, div.shortmenurecipes")) #"div.shortmenurecipes span"))
#    )

    # Collect and print item names
#    print("\n==FOR:", colleges[0], "==\n")
#    items = [e.text.strip() for e in driver.find_elements(By.CSS_SELECTOR, "div.shortmenumeals, div.shortmenurecipes") if e.text.strip()]  #"div.shortmenurecipes span") if e.text.strip()]
#    print(" | ".join(items))
#    print("\n")

#finally:
#    driver.quit()

# Previous issue was cuased by Selenium using direct links to dining locations,
# which failed due to missing session cookies. Resolved by first loading the
# homepage to establish cookies before navigating to the deseried dining menu.
i = 0
try:
    # Wait for the dining hall links to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.locations a"))
    )
    
    links = driver.find_elements(By.CSS_SELECTOR, "li.locations a")
    locations = [(link.text.strip, link.get_attribute("href")) for link in links if link.text.strip() in colleges]
    # Find and click the “Slug Stop” link or whichever place we need menu data from
    for name, href in locations:
        driver.get(href)

        # Wait for menu items to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.shortmenumeals, div.shortmenurecipes")) #"div.shortmenurecipes span"))
        )

        # Collect and print item names
        print("\n==FOR:", colleges[i], "==\n")
        items = [e.text.strip() for e in driver.find_elements(By.CSS_SELECTOR, "div.shortmenumeals, div.shortmenurecipes") if e.text.strip()]  #"div.shortmenurecipes span") if e.text.strip()]
        print(" | ".join(items))
        print("\n")
        i += 1
        time.sleep(1)

finally:
    driver.quit()