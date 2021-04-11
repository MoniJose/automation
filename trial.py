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
regg_no.send_keys('2276430')
search = driver.find_element_by_xpath('//*[@id="registeredCases"]/div/div[4]/button[1]')
search.click()
regno = driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr/td[2]').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id("middleFrame"))
sleep(2)
sleep(2)
# close_b = driver.find_element_by_xpath('/html/body/div[18]/div/div/div[3]/button')
# close_b.click()
# sleep(2)


sleep(3)

ip_no = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')
ip_no.send_keys(83886)

admission_type = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/select')
drop = Select(admission_type)
drop.select_by_visible_text('Planned')
diagnosed_by = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[4]/select')
drop = Select(diagnosed_by)
drop.select_by_visible_text('Others')
doctor_name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/input')
doctor_name.send_keys('DR PRADEEP K J')
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[3]/input').click()
a_date = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table/tbody/tr[2]/td[6]')
a_date.click()
procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
procedure_con.click()

MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
MLC.click()

sleep(3)

gen_f = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
gen_f.click()
sleep(30)
temperature = driver.find_element_by_name('examinationFnd')
sleep(2)
temperature.click()
sleep(2)
f = driver.find_element_by_name('temp')
f.click()
sleep(5)
tmp = driver.find_element_by_name('GE11')
tmp.send_keys(str(98.6))
sleep(3)
pulse = driver.find_element_by_name('examinationFnd')
pulse.click()
sleep(2)
pulse_r = driver.find_element_by_name('GE12')
pulse_r.send_keys(78)
sleep(1)
bp = driver.find_element_by_name('examinationFnd')
bp.click()
sleep(2)
driver.find_element_by_name('GE14').send_keys(150)
sleep(2)
bp_h = driver.find_element_by_name('BP1')
bp_h.send_keys(90)
sleep(5)
save_k = driver.find_element_by_class_name('btn btn-success')
save_k.click()
sleep(5)
save_ok = driver.find_element_by_class_name('btn btn-primary bootbox-accept')
save_ok.click()
sleep(2)

close_save = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/button')
close_save.click()
sleep(2)
r = input("enter your photo")
photo = driver.find_element_by_xpath('/html/body/form/div/div/div/label').click()
photo.send_keys(r'C:\Users\PC\Desktop\automation\PREDIALYSISxPHOTO_VASU_P3SD07INJ_99_50_22385_20210329_110252_34.jpeg')
photo.s


ad_v = driver.find_element_by_id('btnattach')
ad_v.click()
sleep(3)
add_vi = driver.find_element_by_xpath('//*[@id="uploadBPM"]').click()
# add_vi.send_keys(r'C:\Users\PC\Desktop\automation\PREDIALYSISxPHOTO_VASU_P3SD07INJ_99_50_22385_20210329_110252_34.jpeg')













