# ProductTracker

Scrapes popular cycling website for buying and selling used cycling products. 

## How It's Made:

**Tech used:** BeautifulSoup and Pandas libraries in Python, Microsoft Excel, SQL

Compiled script to take only listings meeting certain criteria unable to be filtered for in the website's existing search filtering options. Used BeautifulSoup to scrape site and obtain listing meeting desired criteria. Wrote listing info into a CSV file, each listing comprising one row in the CSV file. 

Used Pandas and SQL to perform data analysis with data in CSV file. For example, a Python script using Pandas showed which keywords and brands saw higher interest and higher prices.

## Results

Wheelsets and Ultimate (brand) bikes were the listings with the most interest and saw some of the highest prices.

## Optimizations

Trigger an alert and a new row to be written into CSV or Google Sheet everytime a product with certain keywords and under a certain price threshold is listed to site. This will aid a small business in purchasing products that would return the highest profit after refurbishing and reselling. 
