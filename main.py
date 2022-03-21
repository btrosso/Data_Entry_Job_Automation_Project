from soup import Soup
from formbot import Formbot

soup = Soup()
formbot = Formbot(soup)

soup.get_zillow_data()

formbot.fill_out_forms()
