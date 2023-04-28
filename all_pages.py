import requests
from bs4 import BeautifulSoup
import csv
import datetime

file = open('all_pages.txt', 'r')

for line in file.readlines():
    response = requests.get(line)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    try:
        title = soup.find('h1').get_text()
        print(title)
        good_soup = soup.find_all('div', {'class': 'buysell-details-column'})[1].contents
        views = int(good_soup[-5].strip().replace(",",""))
        watches = int(good_soup[-1].strip())
        try:
            price = soup.find('div', {'class': 'buysell-container buysell-price'}).get_text().strip()

            price = price.replace(',','').replace('$','').replace('USD','')
            price = int(price)
        except ValueError:
            continue
        print(price)
        datetime_object = datetime.datetime.strptime(good_soup[2].strip(), '%b-%d-%Y %H:%M:%S')
        diff = datetime.datetime.now()-datetime_object
        with open('all_pages.csv', 'a+', newline='', errors="ignore") as csv_file:
            write = csv.DictWriter(csv_file, fieldnames=['Title', 'Price', 'Views', 'Watches', 'Views/Watches', 'Link'])
            write.writerow({'Title': title, 'Price': price, 'Views': views, 'Watches': watches, 'Link': line.strip()})
    except AttributeError:
        continue


file.close()
