import os
import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class Soup:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        self.response = requests.get(url=os.environ['ZILLOW_SEARCH_URL'], headers=self.headers).content
        self.soup = BeautifulSoup(self.response, 'html.parser')
        self.prices = []
        self.addresses = []
        self.links = []

    def get_zillow_data(self):
        """
        parse through the data from the zillow website to get the search results
        reference: https://stackoverflow.com/questions/69024599/scraping-data-from-zillow-com-using-beautifulsoup
        :return:
        """
        # use json method and load the soup
        data = json.loads(
            self.soup.select_one("script[data-zrr-shared-data-key]")
                .contents[0]
                .strip("!<>-")
        )
        # grab the search results
        all_data = data['cat1']['searchResults']['listResults']
        # dig into the data to pull out the relevant pieces of information
        for i in range(len(all_data)):
            #some items have the 'price' key nested inside units key, while others have simply inside data key
            try:
                price = all_data[i]['units'][0]['price']
                self.prices.append(price)
            except KeyError:
                price = all_data[i]['price']
                self.prices.append(price)
            address = all_data[i]['address']
            self.addresses.append(address)

            link = all_data[i]['detailUrl']
            # sometimes the link does not contain the starting website url, thats why we are inserting "https://www.zillow.com{link}" at the starting of link
            if 'http' not in link:
                link_to_buy = f"https://www.zillow.com{link}"
                self.links.append(link_to_buy)
            else:
                link_to_buy = link
                self.links.append(link_to_buy)
            print(price)
            print(address)
            print(link_to_buy)
            print("\n")
