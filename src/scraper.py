from bs4 import BeautifulSoup
import requests

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_Internet_companies'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the class 'wikitable'
table = soup.find('table', {'class': 'wikitable'})

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    if len(cells) == len(headers):  # Ensure the row has the correct number of columns
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)

# Print the headers and rows
print("Headers:", headers)
for row in rows:
    print(row)