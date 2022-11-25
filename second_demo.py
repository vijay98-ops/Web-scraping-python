from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/chromedriver.exe"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s) # exec path has been depreciated

url = "https://the-internet.herokuapp.com/dynamic_loading/2"

driver.get(url=url)
driver.find_element_by_xpath('//*[@id="start"]/button')
driver.implicitly_wait(10)

text = driver.find_element_by_xpath('//*[@id="finish"]/h4')

print(text)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\path\to\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")
driver.quit()