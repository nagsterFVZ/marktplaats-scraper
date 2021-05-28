# Marktplaats listing scanner
This is a simple python script that will scan a provided marktplaats page at time intervals and send you a push notification using [pushover](https://pushover.net/). Yes I know marktplaats has a notify button to notify you about new listings, but as far as I can tell that's a day overview, so this is more useful for sniping deals.

### Dependecies
- BeautifulSoup4 `pip install beautifulsoup4`
- selenium `pip install selenium`
- requests `pip install requests`
- chrome webdriver [download](https://chromedriver.chromium.org/downloads)
- [pushover](https://pushover.net/) account

### Setup
You will need to make some minor changes to the config.ini file in order for the script to work. 
- In the config file you need to set the pushover token and user key. These can both be gotten from pushovers site (the app token is registered [here](https://pushover.net/apps/build))
- Then set the path to where you keep the chrome webdriver
- Finally provide the marktplaats page that you want to scan (I recommend sorting on newest listings first)

### Notifications
When creating your app on pushover you can upload an image, I chose to upload the marktplaats icon for aesthetics (This image is property of Marktplaats B.V.)

<img src="https://i.imgur.com/IWzaqID.jpg" width="300"/>
<img src="https://i.imgur.com/WBNssoA.jpg" width="300"/>

#### Notice
In no way is this script linked to Marktplaats B.V. It has been made as a fun project, the script only crawls one page every 30 minutes as in to no way cause strain on servers. The script should not  be modified (besides the needed variables in the config.ini file)