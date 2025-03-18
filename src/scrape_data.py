from bs4 import BeautifulSoup
import requests
import pandas as pd

# Wikipedia URL
url = 'https://en.wikipedia.org/wiki/List_of_largest_Internet_companies'

# Send a GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the table with class 'wikitable'
table = soup.find('table', {'class': 'wikitable'})

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip header row
    cells = row.find_all('td')
    if len(cells) == len(headers):  # Ensure row has correct number of columns
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
df.to_csv(r'C:\Users\Kmmadu\ecommerce-data-analysis\data\raw_internet_companies.csv', index=False)

