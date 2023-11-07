# Web-Scraper for Comparing Product
# Prices on Flipkart and Amazon
This is a Python script that allows you to compare prices of a product on Flipkart and Amazon 
by scraping the product pages. It retrieves the prices of the product from both 
websites and provides a comparison of the prices.

### How it works
1. The script uses the BeautifulSoup library to parse HTML content from the provided Flipkart and Amazon product URLs.
2. It sends HTTP requests to the URLs, retrieves the HTML content, and extracts the product prices.
3. The extracted prices are then compared, and the script informs you which website offers the lower price or if the prices are the same.

### Prerequisites
Before using this script, make sure you have the following prerequisites installed:

1. Python 3.x
2. BeautifulSoup (bs4)
3. Requests (requests)
   
  You can install the required Python packages using pip:
        pip install bs4
        pip install requests

###Usage
1. Run the script and provide the URLs of the product pages on Flipkart and Amazon when prompted.

2. The script will scrape the product prices and provide you with a price comparison.

3. You'll receive one of the following outcomes:
    1. Amazon price is lower.
    2. Flipkart price is lower.
    3. Both prices are the same.

###License
This project is licensed under the MIT License.

###Disclaimer
Please note that web scraping may be subject to the terms of use and policies of the 
websites being scraped. Ensure that you have the necessary permissions and adhere to 
legal and ethical guidelines when using this script.






