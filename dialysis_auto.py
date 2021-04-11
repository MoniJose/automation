from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
def enter_something(xpath, value):
    driver.find_element_by_xpath(xpath).send_keys(value)



def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe",options=options)
driver.maximize_window()

# user = input('enter email or phone no')
# pswd = input('enter password')

driver.get('https://pmjaylive.sevensigma.in/home')

user_name = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/form/div/div[2]/div[1]/input')
user_name.send_keys(8590050640)
password = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/form/div/div[2]/div[2]/input')
password.send_keys(50640)
driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/form/div/div[3]/button').click()
sleep(3)







