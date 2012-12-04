from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re
import yaml
from bm_dal import BMDAL

class BMScraper(object):
	def __init__(self):
		self.driver = webdriver.Firefox()
		with open('./config/config.yml', 'r') as config_file:
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
		nav_bar_search_div = self.driver.find_element_by_id("overbg2")
		nav_bar_search_div.find_element_by_xpath("./a[2]").click()
		search_div = self.driver.find_element_by_id("div_search")
		search_div.find_element_by_xpath("./div[2]/a[1]").click()
		time.sleep(10)
		print "Trying to find dyn_pages"
		profiles_div = self.driver.find_element_by_id("dyn_pages")
		i = 1
		dal = BMDAL()
		while True:
			print 'loop counter = ' + str(i)
			div_path = "./div[@id=\"res_pg_" + str(i) + "\"]/div[@class=\"srhlist-bg width774 pntr\"]"
			print div_path
			profile_divs = profiles_div.find_elements_by_xpath(div_path)
			for profile_div in profile_divs:
				profile_url = profile_div.find_element_by_xpath('./div/div[1]/div[1]/div[1]/a')
				dal.insert_id(profile_url.text)
			print 'done with page ' + str(i)
			pagination_div = self.driver.find_element_by_id('pagination')
			print 'Found pagination div, moving on to the next page' + pagination_div.text
			if i == 1:
				pagination_div.find_element_by_xpath('./li[6]/a').click()
			else:
				pagination_div.find_element_by_xpath('./li[7]/a').click()
			i = i + 1
			print "done with this loop. sleeping for 5"
			time.sleep(5)
	
	
	def stop(self):
		self.driver.close()
	
if __name__ == '__main__':
	BMScraper().downloadBMData()
	