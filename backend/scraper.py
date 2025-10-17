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

from bs4 import BeautifulSoup
import requests

source = requests.get('https://nutrition.sa.ucsc.edu/').text 

soup = BeautifulSoup(source, 'html.parser')  ## stores the html in soup
# print(soup.prettify())

all_menus = soup.find_all('a', limit = 5)  ## We only need the first 5 menus, the rest are the stores & cafes

menus = {}  ## key is location and val is the link to menu
for m in all_menus:
    menus[m.get_text(strip=True)] = 'https://nutrition.sa.ucsc.edu/' + m['href']

#for (key, val) in menus.items():
#    print('College Name:', key)
#    print('Link to Menu:', val, '\n')

source2 = requests.get(menus['John R. Lewis & College Nine Dining Hall']).text
###soup2 = BeautifulSoup(source2, 'html.parser')
###target_sections = soup2.find_all('div', class_='shortmenumeals')

###source2 = requests.get('https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=John+R.+Lewis+%26+College+Nine+Dining+Hall&naFlag=1').text
soup2 = BeautifulSoup(source2, 'html.parser')
print(soup2) #Gives the ASP.NET runtime error in the form of html


#for (key, val) in menus.items():
#    source2 = requests.get(val).text
#    soup2 = BeautifulSoup(source2, 'html.parser')
#    target_sections = soup2.find_all('div', class_='shortmenumeals')
