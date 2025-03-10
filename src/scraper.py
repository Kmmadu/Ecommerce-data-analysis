from bs4 import BeautifulSoup
import requests


url = 'https://en.wikipedia.org/wiki/List_of_largest_Internet_companies'


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table', {'class': 'wikitable'})


headers = [header.text.strip() for header in table.find_all('th')]


rows = []
for row in table.find_all('tr')[1:]:  
    cells = row.find_all('td')
    if len(cells) == len(headers):  
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)


print("Headers:", headers)
for row in rows:
    print(row)