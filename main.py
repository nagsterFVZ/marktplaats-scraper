import scraper
import threading
import requests
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
listings = []
listingIDs = []

def pushover(title, message):
    print("sending notif")
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": config.get('pushover', 'token'),
        "user":config.get('pushover', 'user'),
        "title": title,
        "message": message,
    })

def scrapeListings():
    threading.Timer(1800.0, scrapeListings).start()
    scrape = scraper.MartplaatsScrapper()
    if not listings:
        pushover("Starting marktplaats scraper", "The scraper will now check for new listings every 30 minutes")
        for listing in scrape:
            listings.append(listing)
            listingIDs.append(listing["mID"])
    else:    
        for listing in scrape:
            if(listing["mID"] not in listingIDs):
                listings.append(listing)
                listingIDs.append(listing["mID"])
                message = (listing["price"] + " - " + listing["title"] + " " + listing["url"])
                pushover("New bike listing", message)
                

scrapeListings()