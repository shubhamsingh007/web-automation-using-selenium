import requests
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\Shubham Singh\PycharmProjects\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3.org/")

links = driver.find_elements_by_xpath('.//a')

print("Broken links W3 website are ==> ")
for link in links:
    r = requests.head(link.get_attribute("href"))
    if(r.status_code>=400): # broken links are above 400 value
        print(link.get_attribute('href'), r.status_code)