from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re

class BMScraper(object):
	def __init__(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()

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
		login_txt.send_keys("tejaswi.yvs@gmail.com")
		pwd_txt.click()
		pwd_txt.send_keys("ghottip0")
		print login_txt.text + pwd_txt.text
		login_txt.submit()
	
	def search(self):
		if self.driver.title == "The Only Matrimony Site in the World with 100% Verified Mobile Numbers":
			skip_to_home = self.driver.find_element_by_xpath("//html/body/div[1]/div[1]/div[4]/a")
			skip_to_home.click()
		search_div = self.driver.find_element_by_id("overbg2")
		search_button = search_div.find_element_by_xpath("./a[1]").click()
		age_txt = self.driver.find_element_by_id("STAGE")
		age_txt.submit()
	
	def stop(self):
		self.driver.close()
	
if __name__ == '__main__':
	BMScraper().downloadBMData()
	