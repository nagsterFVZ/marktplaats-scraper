from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(config.get('scraper', 'driver'), chrome_options=options)
delay = 3

def MartplaatsScrapper():
    listings = []
    listingsJSON = []
    url = (config.get('scraper', 'webPage'))
    driver.get(url)
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "mp-Listing")))
    except TimeoutException:
        print("Loading took too much time!")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    listings = soup.find_all('li', attrs={'class':'mp-Listing'})
    for listing in listings:
        link = listing.find('a', attrs={'class':'mp-Listing-coverLink'}).get('href')
        mIDpos = link.find('/m')
        if(mIDpos > 0):
            mID = link[mIDpos+1:mIDpos+12]
            url = ("https://link.marktplaats.nl/" + mID)
            title = listing.find('h3', attrs={'class':'mp-Listing-title'}).text
            price = listing.find('span', attrs={'class':'mp-Listing-price'}).text
            placed = listing.find('span', attrs={'class':'mp-Listing-date'}).text
            listingJSON = {
                "mID" : mID,
                "title" : title,
                "price" : price,
                "url" : url,
                "placed" : placed,
            }
            listingsJSON.append(listingJSON)
    return listingsJSON