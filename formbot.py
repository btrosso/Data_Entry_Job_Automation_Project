import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

class Formbot:
    def __init__(self, soup):
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.prices = soup.prices
        self.addresses = soup.addresses
        self.links = soup.links

    def fill_out_forms(self):
        self.driver.get(os.environ['GOOGLE_FORM_URL'])
        time.sleep(5)

        for i in range(len(self.links)):
            # this block of code is the fill algorithm
            q1_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            q1_address.send_keys(self.addresses[i])
            time.sleep(2)
            q2_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            q2_price.send_keys(self.prices[i])
            time.sleep(2)
            q3_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            q3_link.send_keys(self.links[i])
            time.sleep(2)
            submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.click()
            time.sleep(2)
            submit_another = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another.click()
            time.sleep(2)

