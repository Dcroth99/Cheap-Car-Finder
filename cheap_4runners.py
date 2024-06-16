from bs4 import BeautifulSoup
import requests


url = 'https://honolulu.craigslist.org/search/sss?query=4x4%20toyota%204runner#search=1~gallery~0~0'


result = requests.get(url)


doc = BeautifulSoup(result.text, 'html.parser')


price = doc.find_all(class_='price')

mycars = []
for i in price:
    price_text = i.string

    if price_text and "$" in price_text:
        value = price_text.split('$')[1].strip()
        value = float(value.replace(',', ''))

        if value < 10000:
            listing = i.find_previous(class_='title')
            if listing and '4runner' in listing.text.lower():
                listing_text = listing.text
                print(f"Title: {listing_text}")

                mycars.append(listing_text)

print('\nCars with price lower than $10,000:')

for j in mycars:
    print(j)
