from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# linux default path /usr/local/bin
# but path we set in codespaces while installing chromedriver following
# setup.md
driver = webdriver.Chrome("/usr/bin/chromedriver")

url = "http://the-internet.herokuapp.com/login"

driver.get(url=url)





driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element_by_xpath('//*[@id="login"]/button').click()

driver.quit()
