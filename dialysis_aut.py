from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
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

view_list = driver.find_element_by_xpath('//*[@id="out-table"]/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]/div/button[1]')
view_list.click()
sleep(3)


preauth = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div/div[1]/div/div[2]/div/p[1]').click()
sleep(10)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div/div/div/input').send_keys('DIALYSIS')
sleep(10)
reg_no = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[3]/div')
reg = reg_no.get_attribute('innerHTML')

ip_number = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[7]/div')
ip_num = ip_number.get_attribute('innerHTML')
view_profile = driver.find_element_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/i')
view_profile.click()

treat_date = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[5]/div/div/div[8]/p[2]')
treatment_d = treat_date.get_attribute('innerHTML')
# tmp_rate = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/p[2]')
# tmp_rt = tmp_rate.get_attribute('innerattribute')
pulse_rate = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/p[2]')
pulse_rt = pulse_rate.get_attribute('innerHTML')
print(pulse_rt)
start = 3
stop = 17
if len(str(pulse_rt)) > stop :
    pulse_rt = pulse_rt[0: start:] + pulse_rt[stop + 1::]
print('Modified String : ',pulse_rt)

# number_of_rows = len(driver.find_elements_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div'))
# print(number_of_rows)


# driver.get('http://tms.pmjay.gov.in/')
# sleep(2)
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys('KER002197')
# pas = driver.find_element_by_xpath('//*[@id="password"]')
# pas.send_keys('Automate@1')
# # driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
# driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
# driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('KERALA')
# sleep(1)
# driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
# captcha = input("enter captcha here")
# captcha_text = driver.find_element_by_xpath('//*[@id="reqCaptcha"]')
# captcha_text.send_keys(captcha)
# driver.find_element_by_id('checkSubmit').click()
# login = driver.find_element_by_xpath('//*[@id="login-submit"]')
# login.click()
# sleep(2)
#
# close = driver.find_element_by_xpath('//*[@id="notificationModal"]/div/div/div[1]/button')
# close.click()
# sleep(5)
#
# preauth = driver.find_element_by_link_text('Preauth')
# preauth.click()
# sleep(2)
#
# preauth_ins = driver.find_element_by_xpath('//*[@id="childmenu3"]/li[1]/a/span[1]')
# actions = ActionChains(driver)
# actions.move_to_element(preauth_ins).click().perform()
# sleep(2)
#
# driver.switch_to.frame(0)
# regg_no = driver.find_element_by_name('patientNo')
# regg_no.send_keys(reg)
#
# search = driver.find_element_by_xpath('//*[@id="registeredCases"]/div/div[4]/button[1]')
# search.click()
# regno =driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr/td[2]').click()
# driver.switch_to.default_content()
# sleep(3)
#
#
# driver.switch_to.frame(driver.find_element_by_id("middleFrame"))
# # ip = driver.find_element_by_id('patientTypeIP')
# # ip.click()
# # Ipop = driver.find_element_by_id('submitIpOp')
# # Ipop.click()
# # sleep(3)
#
# # ok = driver.find_element_by_xpath('/html/body/div[25]/div/div/div[2]/button[2]')
# # ok.click()
# # sleep(2)
#
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
# doctor = driver.find_element_by_xpath('//*[@id="collapse6"]/div[1]/div[5]/span/span[1]/span/span[2]/b')
# doctor.click()
# sleep(2)
#
# # add_procedure = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/input')
# # add_procedure.click()
# # sleep(2)
# ip_no = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')
# ip_no.send_keys(ip_num)
#
# admission_type = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/select')
# drop = Select(admission_type)
# drop.select_by_visible_text('Planned')
# # treatment_date = driver.find_element_by_xpath()
#
# diagnosed_by = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[4]/select')
# drop = Select(diagnosed_by)
# drop.select_by_visible_text('Others')
# doctor_name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/input')
# doctor_name.send_keys('DR PRADEEP K J')
# procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
# procedure_con.click()
# MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
# MLC.click()
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[3]/input').click()
# # alldate = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table')
# # alldate.click()
# # alldate.send_keys(treatment_d)
# # ad_date = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table/tbody/tr[1]/td[5]')
# # ad_date.click()
# # for dates in alldate:
# #         if(dates.is_enabled() and dates.is_displayed() and str('treatment_d') == date):
# #             dates.click()
#
# alldate = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table')
# ad_date = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table/tbody/tr[2]/td[2]')
# ad_date.click()
# sleep(2)
# procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
# procedure_con.click()
# MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
# MLC.click()
# sleep(2)
# # add_view = driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]')
# # add_view.click()
# # photo = input('enter  path of the photo')
# # upload_photo = driver.find_element_by_id('uploadBPM')
# # upload_photo.send_keys('photo')
# sleep(2)
# general_find = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
# general_find.click()
# temperature = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[1]/input')
# temperature.click()
# sleep(2)
# f = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[2]/input[2]')
# f.click()
# sleep(1)
# tmp = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[2]/input[3]')
# tmp.send_keys(98.6)
# pulse = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[1]/input')
# pulse.click()
# sleep(1)
# pulse_r = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[2]/input')
# pulse_r.send_keys(pulse_rt)
# sleep(1)
# bp = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input')
# bp.click()
# sleep(1)
# # bp_mm = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[2]/input[1]')
# # bp_mm.send_keys()
# # bp_hg = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[2]/input[2]')
# # bp.send_keys()
# save_d = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[2]/button')
# save_d.click()
# general_find = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
# general_find.click()
# sleep(30)
# temperature = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[1]/input')
# sleep(2)
# temperature.click()
# sleep(2)
# f = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[11]/div[2]/input[2]')
# f.click()
# sleep(5)
# tmp = driver.find_element_by_name('GE11')
# tmp.send_keys(str(98.6))
# sleep(3)
# pulse = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[1]/input')
# pulse.click()
# sleep(2)
# pulse_r = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[2]/input')
# pulse_r.send_keys(76)
# sleep(1)
# bp = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input')
# bp.click()
# sleep(2)
# driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[2]/input[1]').send_keys(160)
# sleep(2)
# bp_h = driver.find_element_by_name('BP1')
# bp_h.send_keys(80)
# sleep(5)
# save = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[2]/button')
# save.click()
# sleep(5)
# save_k = driver.find_element_by_xpath('')
#
#
#























