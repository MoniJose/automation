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

# view = driver.find_element_by_xpath('//*(@id="out-table"])/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]')
#//*[@id="out-table"]/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]/div/button[1]/i
# view_list = driver.find_element_by_xpath('//*[@id="out-table"]/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]/div/button[1]')
# view_list.click()
# sleep(1)


preauth = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div/div[1]/div/div[2]/div/p[1]').click()
sleep(10)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div/div/div/input').send_keys('DIALYSIS')
sleep(10)
# view_profile = driver.find_element_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/i')
# view_profile.click()
# card_id = driver.find_element_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div/div[3]/table/tbody/tr/td[4]/div')
# ele = card_id.get_attribute('innerHTML')
# sleep(5)

# driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe",options=options)
# driver.maximize_window()
driver.get('http://tms.pmjay.gov.in/')
sleep(3)
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('KER002197')
pas = driver.find_element_by_xpath('//*[@id="password"]')
pas.send_keys('Automate@1')
# driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('KERALA')
sleep(1)
driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
captcha = input("enter captcha here")
captcha_text = driver.find_element_by_xpath('//*[@id="reqCaptcha"]')
captcha_text.send_keys(captcha)
driver.find_element_by_id('checkSubmit').click()
login = driver.find_element_by_xpath('//*[@id="login-submit"]')
login.click()
sleep(2)
close = driver.find_element_by_xpath('//*[@id="notificationModal"]/div/div/div[1]/button')
close.click()
sleep(5)

# preauth = driver.find_element_by_link_text("Preauth")
# preauth.click()
sleep(3)
preauth = driver.find_element_by_link_text('Preauth')
preauth.click()
preauth_ins = driver.find_element_by_xpath('//*[@id="childmenu3"]/li[1]/a/span[1]')
actions = ActionChains(driver)
actions.move_to_element(preauth_ins).click().perform()









# https://www.perfecto.io/blog/xpath-in-selenium






