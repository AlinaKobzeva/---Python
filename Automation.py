import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path="./chromedriver"
)
driver.get("https://testrail.osinit.com/index.php?/auth/login")
input_name = driver.find_element_by_xpath('//*[@id="name"]')
input_password = driver.find_element_by_xpath('//*[@id="password"]')
login_button = driver.find_element_by_xpath('//*[@id="button_primary"]')

input_name.send_keys('info@osinit.com')
input_password.send_keys('QA.osinit')
login_button.send_keys(Keys.RETURN)


Стажировка2022Group1 = driver.find_element_by_xpath('//*[@id="project-69"]/div[2]/div[1]/a').click()

TestSuites = driver.find_element_by_xpath('//*[@id="navigation-suites"]').click()

КобзеваАлина = driver.find_element_by_xpath('//*[@id="content-inner"]/div/div[10]/div[2]/div[1]/a').click()

filter:none = driver.find_element_by_xpath('//*[@id="filterBy"]').click()


automated = ('//*[@id="grid-28464"]/tbody/tr[1]/th[5]/a/span').click()


driver.close()


