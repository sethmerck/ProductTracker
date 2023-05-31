import requests
from bs4 import BeautifulSoup

url = 'https://www.pinkbike.com/buysell/list...'
terms = '...'
# Scraping function
links = []
def scrape(url):
    count = 1
    for i in range(1,350):
        # Get HTML content
        response = requests.get(url + str(i) + terms)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        # Get all listings
        listings = soup.findAll('div', {'class': 'bsitem'})

        # Iterate through listings
        for listing in listings:
            # Get title
            title = listing.find('div', {'class': 'bsitem-title'}).get_text().strip()
            # Get price
            price = int(listing.find('td', {'class': 'bsitem-price'}).get_text().strip().replace('$','').replace('USD',''))
            # Get location
            location = listing.find('td', {'colspan': '2'}).get_text().strip()
            # Get href
            href = listing.find('a').get('href')
            # Print results
            print('Title: ' + title)
            print(price)
            print('Location: ' + location)
            print('Href: ' + href)
            print('\n')
            if price <= 3000:
                links.append(href)
    

# URL of page to scrape
scrape(url)
print(links)
f = open("new_pages.txt", "w")

# write the raw list to the file
for l in links:
    f.write(str(l) + "\n")

# close the file
f.close()
