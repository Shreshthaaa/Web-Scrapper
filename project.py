from bs4 import BeautifulSoup
import requests

flipkartProductURL = input('Enter the flipkart product URL: ')
amazonProductURL = input('Enter the amazon product URL: ')
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

if flipkartProductURL and amazonProductURL:

    flipkartResponse = requests.get(flipkartProductURL,headers=headers)
    amazonResponse = requests.get(amazonProductURL,headers=headers)
    
    flipkartSoup = BeautifulSoup(flipkartResponse.content,'html.parser')
    amazonSoup = BeautifulSoup(amazonResponse.content,'html.parser')
    
    flipkartProductPrice = flipkartSoup.find('div',{'class':'_30jeq3 _16Jk6d'})
    if flipkartProductPrice is not None:
        flipkartProductPrice = flipkartProductPrice.get_text().strip()
        flipkartProductPrice = float(flipkartProductPrice.replace(',','').replace('₹',''))
        print('Flipkart product price is ₹',str(flipkartProductPrice))
    else:
        print('Flipkart product price is not available.')
    
    amazonProductPrice = amazonSoup.find('span',{'class':'a-price-whole'})
    if amazonProductPrice is not None:
        amazonProductPrice = amazonProductPrice.get_text().strip()
        amazonProductPrice = float(amazonProductPrice.replace(',','').replace('₹',''))
        print('Amazon product price is ₹' ,str(amazonProductPrice))
    else:
        print('Amazon product price is not available.')
    
    if None in (flipkartProductPrice, amazonProductPrice):
        print('Inadequate information to compare prices.')
    else:
        

        if (flipkartProductPrice) > (amazonProductPrice):
            print('Amazon price is low.')
            print('Price is  ₹'+ str(amazonProductPrice))   
        elif (flipkartProductPrice) < (amazonProductPrice):
            print('Flipkart price is low.')
            print('Price in ₹'+ str(flipkartProductPrice))
        else:
            print('Both prices are same.')
            print('Price is ₹'+ str(flipkartProductPrice))