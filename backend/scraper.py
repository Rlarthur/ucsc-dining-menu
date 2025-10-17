#Scrapes UCSC dining data and updates JSON file
# Main job is to fetch menu data from UCSC dining website and save it in a structured JSON format
# This data is then served by the Flask app in app.py
# Need to implement automatic updates (e.g. via cron job) to keep data fresh

#=======// UCSC MENU LINKS //=======#
#  John R. Lewis & Colleger Nine:   https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=John+R.+Lewis+%26+College+Nine+Dining+Hall&naFlag=1
#  Cowell & Stevenson:   https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=05&locationName=Cowell+%26+Stevenson+Dining+Hall&naFlag=1
#  Crown & Merrill and Banana Joe's:   https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=20&locationName=Crown+%26+Merrill+Dining+Hall+and+Banana+Joe%27s&naFlag=1
#  Porter & Kresge:   https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=25&locationName=Porter+%26+Kresge+Dining+Hall&naFlag=1
#  Rachel Carson & Oakes:   https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=30&locationName=Rachel+Carson+%26+Oakes+Dining+Hall&naFlag=1
#=======// UCSC MENU LINKS //=======#

#source = requests.get('https://nutrition.sa.ucsc.edu/').text 
#soup = BeautifulSoup(source, 'html.parser')  ## stores the html in soup
# print(soup.prettify())
#all_menus = soup.find_all('a', limit = 5)  ## We only need the first 5 menus, the rest are the stores & cafes
#menus = {}  ## key is location and val is the link to menu
#for m in all_menus:
#    menus[m.get_text(strip=True)] = 'https://nutrition.sa.ucsc.edu/' + m['href']
#for (key, val) in menus.items():
#    print('College Name:', key)
#    print('Link to Menu:', val, '\n')

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=25&locationName=Porter+%26+Kresge+Dining+Hall&naFlag=1"

driver.get(url)
time.sleep(5)
soup2 = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

print(soup2) #Gives the ASP.NET runtime error in the form of html
