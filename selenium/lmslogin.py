import imp
from nturl2path import url2pathname
from selenium import webdriver

url = 'https://eclass.donga.ac.kr/'
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url) 

driver.find_element_by_xpath('//*[@id="visual"]/div/div[2]/div[2]/a').click()

driver.find_element_by_xpath('//*[@id="login_user_id"]').send_keys('2036847')
driver.find_element_by_xpath('//*[@id="login_user_password"]').send_keys('lee866177!')
driver.find_element_by_xpath('//*[@id="form1"]/div[4]/a/span').click()

print("0")
