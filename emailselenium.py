from selenium import webdriver
import time

#from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome("C:\\Users\Shubham Singh\PycharmProjects\Selenium\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.com/gmail/")
time.sleep(1)

email_name = driver.find_element_by_id("identifierId")
email_name.clear()
email_name.send_keys("1rn16cs128.shubham@gmail.com")
email_button = driver.find_element_by_id("identifierNext")
email_button.click()
time.sleep(1)

email_password = driver.find_element_by_name("password")
email_password.clear()
email_password.send_keys("shubham_12345")
email_password_button = driver.find_element_by_id("passwordNext")
email_password_button.click()
time.sleep(5)

email_compose = driver.find_element_by_css_selector(".aic .z0 div")
email_compose.click()
time.sleep(1)

send_mail = driver.find_element_by_css_selector(".oj div textarea")
send_mail.send_keys("shubham.1rn16cs128@gmail.com")
#time.sleep(1)

subject = driver.find_element_by_name("subjectbox")
subject.send_keys("selenium practicle example")
#time.sleep(1)

mess = driver.find_element_by_xpath("//div[@id=':do']")
mess.send_keys("this is message")


#message = driver.find_element_by_css_selector("#:hs")
#message.clear()
#message.send_keys("this is example text from selenium to future")
#time.sleep(1)

send_email = driver.find_element_by_css_selector(".T-I.J-J5-Ji.ao0.v7.T-I-atl.L3")
send_email.click()
#time.sleep(2)

'''log_out = driver.find_element_by_css_selector(".gb_x.gb_Ea.gb_f")
log_out.click()
time.sleep(1)
signout = driver.find_element_by_css_selector("#gb_71.gb_0.gb_Lf.gb_Sf.gb_se.gb_kb")
signout.click()
time.sleep(5)
'''





'''
driver.find_element_by_xpath("//ul[@class='h-c-header__cta-list header__nav--ltr']//a[contains(@class,'h-c-header__nav-li-link')][contains(text(),'Sign in')]").click()
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("1rn16cs128.shubham@gmail.com")
time.sleep(1)
driver.find_element_by_xpath("//span[@class='CwaK9']").click()
'''


#driver.quit()

