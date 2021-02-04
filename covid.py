from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
soup = bs(r.content, features = 'html.parser')

country = input("\nEnter a country: ")
country = country.capitalize()

head = soup.find("tr")
titles = head.find_all("th")
menu = []

for title in titles:
    menu.append(title.text)

table = soup.find("table")
rows = table.find_all("tr")

for row in rows:
    names = row.find_all(attrs = {'style': 'font-weight: bold; font-size:16px; text-align:left; padding-left:5px; padding-top:10px; padding-bottom:10px'})
    
    for name in names:
        if country in name.text:
            print(f'\n{menu[0]}: {name.text}')
            print(f'Active Covid {menu[1]}: {name.find_next_sibling("td").text}')
            print(f'{menu[2]} due to Covid: {name.find_next_sibling("td").find_next_sibling("td").text}')
            print(f'{menu[3]} of the world: {name.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").text}')
