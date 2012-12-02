from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re
import yaml

class BMScraper(object):
	def __init__(self):
		self.driver = webdriver.Firefox()
		with open('./config.yml', 'r') as config_file:
			self.config = yaml.load(config_file.read())
		if self.config == None:
			raise Exception('Config', 'File Not Found')
	
	def downloadBMData(self):
		self.driver.get("http://www.bharatmatrimony.com/")
		self.login()
		self.search()
	
	def login(self):
		# login_txt = self.driver.find_elements_by_xpath("//div[@id='topnav']")
		login_btn = self.driver.find_element_by_id("logindiv")
		login_txt = self.driver.find_element_by_id("ID")
		pwd_txt = self.driver.find_element_by_id("PASSWORD")
		login_btn.click()
		login_txt.send_keys(self.config["email"])
		pwd_txt.click()
		pwd_txt.send_keys(self.config["password"])
		login_txt.submit()
	
	def search(self):
		if self.driver.title == "The Only Matrimony Site in the World with 100% Verified Mobile Numbers":
			skip_to_home = self.driver.find_element_by_xpath("//html/body/div[1]/div[1]/div[4]/a")
			skip_to_home.click()
		search_div = self.driver.find_element_by_id("overbg2")
		search_button = search_div.find_element_by_xpath("./a[1]").click()
		# Liberal filters
		self.driver.find_element_by_id("ENDAGE").send_keys("40") # Max Age = 40
		self.driver.find_element_by_id("MARITAL_STATUS0").click() # Marital Status = Any
		self.driver.find_element_by_id("MOTHERTONGUE_IN").send_keys("Any") # Mother Tongue = Any
		self.driver.find_element_by_id("EDUCATION_IN").send_keys("Any")
		self.driver.find_element_by_id("ENDAGE").submit()
	
	
	def stop(self):
		self.driver.close()
	
if __name__ == '__main__':
	BMScraper().downloadBMData()
	