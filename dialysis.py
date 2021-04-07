from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get('http://tms.pmjay.gov.in/')
sleep(5)
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('KER002197')

pas=driver.find_element_by_xpath('//*[@id="password"]')
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


preauth = driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[4]/a/span[1]')
preauth.click()
preauth_ins = driver.find_element_by_xpath('//*[@id="childmenu3"]/li[1]/a/span[1]')
actions = ActionChains(driver)
actions.move_to_element(preauth_ins).click().perform()
sleep(2)

driver.switch_to.frame(0)
regg_no = driver.find_element_by_name('patientNo')
regg_no.send_keys('2250966')
search = driver.find_element_by_xpath('//*[@id="registeredCases"]/div/div[4]/button[1]')
search.click()
regno = driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr/td[2]').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id("middleFrame"))
sleep(2)
sleep(2)
# ip = driver.find_element_by_id('patientTypeIP')
# ip.click()
# Ipop = driver.find_element_by_id('submitIpOp')
# Ipop.click()
# sleep(3)
# ok = driver.find_element_by_xpath('/html/body/div[25]/div/div/div[2]/button[2]')
# ok.click()
sleep(5)

# driver.find_element_by_xpath('html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/span/span[1]/span/span[1]').click()
# # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/span/span[1]/span/span[1]').click()
# driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
# sleep(2)
# d_description = driver.find_element_by_xpath('//*[@id="diagDesc"]')
# d_description.send_keys('CKD')
#
# procedure = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/span/span[1]/span/span[2]')
# procedure.click()
# sleep(2)
# sel_procedure = driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[248]')
# sel_procedure.click()
# sleep(2)
speciality = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/span/span[1]/span/span[2]')
speciality.click()
sleep(2)
driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
doctor = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[5]/span/span[1]/span/span[2]')
doctor.click()
sleep(5)
driver.find_element_by_tag_name('li').click()
sleep(2)
ip_no = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')
ip_no.send_keys(98334)

admission_type = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/select')
drop = Select(admission_type)
drop.select_by_visible_text('Planned')
diagnosed_by = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[4]/select')
drop = Select(diagnosed_by)
drop.select_by_visible_text('Others')
doctor_name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/input')
doctor_name.send_keys('DR PRADEEP K J')
procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
procedure_con.click()
MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
MLC.click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[3]/input').click()
sleep(3)

general_find = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
general_find.click()
sleep(30)
temperature = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[1]/input')
sleep(2)
temperature.click()
sleep(2)
f = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[2]/input[2]')
f.click()
sleep(5)
tmp = driver.find_element_by_name('GE11')
tmp.send_keys(str(98.6))
sleep(3)
pulse = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[1]/input')
pulse.click()
sleep(2)
pulse_r = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[2]/input')
pulse_r.send_keys(76)
sleep(1)
bp = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input')
bp.click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[2]/input[1]').send_keys(160)
sleep(2)
bp_h = driver.find_element_by_name('BP1')
bp_h.send_keys(80)
sleep(5)
save_k = driver.find_element_by_xpath('')
































