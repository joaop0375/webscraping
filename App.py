import requests
from bs4 import BeautifulSoup
import csv

url = 'https://exemplo.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find_all('h2', class_='title')

with open('dados.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in titles:
        writer.writerow([title.get_text()])
