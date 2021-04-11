import os
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import NoSuchElementException

# functions

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True




options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
driver.maximize_window()

driver.implicitly_wait(10)
w = WebDriverWait(driver,8)


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
sleep(25)


reg_no = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[3]/div')
reg = reg_no.get_attribute('innerHTML')

ip_number = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[7]/div')
ip_num = ip_number.get_attribute('innerHTML')
print("ip_num",ip_num)
view_profile = driver.find_element_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/i')
view_profile.click()

treat_date = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr/td[9]/div')
treatment_d = treat_date.get_attribute('innerHTML')
print("treatment_d",treatment_d)
# tmp_rate = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/p[2]')
# tmp_rt = tmp_rate.get_attribute('innerattribute')
pulse_rate = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[6]/div')
pulse_rt = pulse_rate.get_attribute('innerHTML')
print(pulse_rt)
x = pulse_rt[:3]
print(x)
y = pulse_rt[4:6]
print(y)









driver.get('http://tms.pmjay.gov.in/')
sleep(5)
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('KER002197')
pas = driver.find_element_by_xpath('//*[@id="password"]')
pas.send_keys('Automate@1')
# driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
driver.find_element_by_xpath('//*[@id="select2-userState-container"]').click()
driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('KERALA')
sleep(1)
driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
# captcha = input("enter captcha here")
captcha_text = driver.find_element_by_xpath('//*[@id="reqCaptcha"]')
captcha_text.click()
input('Continue?  (Hit enter)')
driver.find_element_by_id('checkSubmit').click()
login = driver.find_element_by_xpath('//*[@id="login-submit"]')
login.click()
sleep(2)

close = driver.find_element_by_xpath('//*[@id="notificationModal"]/div/div/div[1]/button')
close.click()
sleep(5)

preauth = driver.find_element_by_link_text('Preauth')
preauth.click()
sleep(2)

preauth_ins = driver.find_element_by_xpath('//*[@id="childmenu3"]/li[1]/a/span[1]')
actions = ActionChains(driver)
actions.move_to_element(preauth_ins).click().perform()
sleep(2)

driver.switch_to.frame(0)
regg_no = driver.find_element_by_name('patientNo')
regg_no.send_keys(reg)

search = driver.find_element_by_xpath('//*[@id="registeredCases"]/div/div[4]/button[1]')
search.click()
regno =driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr/td[2]').click()
sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id("middleFrame"))
sleep(2)

try:
    ip = driver.find_element_by_id('patientTypeIP')
    ip.click()
    Ipop = driver.find_element_by_id('submitIpOp')
    Ipop.click()
    sleep(3)
    ok = driver.find_element_by_xpath('/html/body/div[25]/div/div/div[2]/button[2]')
    ok.click()
    sleep(5)
    print('try')
except:
    sleep(3)
    # driver.find_element_by_xpath('html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/span/span[1]/span/span[1]').click()



print('true')
try:
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/span/span[1]/span/span[1]').click()
    print('except')
    driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
    sleep(2)
    sleep(2)
    d_description = driver.find_element_by_xpath('//*[@id="diagDesc"]')
    d_description.send_keys('CKD')
    procedure = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/span/span[1]/span/span[2]')
    procedure.click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('MG072A')
    sleep(1)
    sel_procedure = driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li')
    sel_procedure.click()
    sleep(2)
    speciality = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/span/span[1]/span/span[2]')
    speciality.click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
    doctor = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div[5]/span/span[1]/span/span[2]')
    doctor.click()
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(5697)
    sel_doc = driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
    sleep(5)
    add_pro = driver.find_element_by_id('addSpeciality')
    add_pro.click()
    sleep(2)

    ok = driver.find_element_by_xpath('/html/body/div[25]/div/div/div[2]/button')
    ok.click()
    sleep(2)

except:
    pass



close_b = w.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[18]/div/div/div[3]/button")))
# close_b = driver.find_element_by_xpath('/html/body/div[18]/div/div/div[3]/button')
close_b.click()
sleep(3)
# upload = driver.find_element_by_xpath('/html/body/form/div/div/div/label')
# upload.send_keys(r'C:\Users\PC\Downloads\KASP-PMJAY_files\PREDIALYSISxPHOTO_IBRAHIM_PS8VO3JD0_99_50_23124_20210407_123113_26\JPEG File (.jpeg')

# photo = driver.find_element_by_id('invAttach')
# driver.execute_script('arguments[0].style.display="block";',photo)
# sleep(3)
#
# upload = driver.find_element_by_xpath('//*[@id="invAttach"]')

# upload.send_keys(r'C:\Users\PC\Downloads\KASP-PMJAY_files\PREDIALYSISxPHOTO_IBRAHIM_PS8VO3JD0_99_50_23124_20210407_123113_26\JPEG File (.jpeg)')
ip_no = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')
ip_no.send_keys(ip_num)

admission_type = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/select')
drop = Select(admission_type)
drop.select_by_visible_text('Planned')
sleep(2)
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

alldate = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[3]/div[3]/input')
print(treatment_d)
print(alldate)
alldate.send_keys(treatment_d)
sleep(2)
procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
procedure_con.click()
MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
MLC.click()
sleep(5)

# general_find = driver.find_element_by_xpath('//*[@id="ipButtonsDiv"]/button[1]')

general_find = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
top = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[1]')
driver.execute_script("return arguments[0].scrollIntoView(true);",top)
sleep(10)
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
#sleep(3)
pulse = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[1]/input')
pulse.click()
#sleep(2)
pulse_r = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[12]/div[2]/input')
pulse_r.send_keys(78)
#sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input').click()
bp = driver.find_element_by_name('GE14')
bp.send_keys(x)
#sleep(2)
bp_h = driver.find_element_by_name('BP1')
bp_h.send_keys(y)
#sleep(5)
save_k = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[2]/button')
save_k.click()
sleep(5)
save_ok = driver.find_element_by_xpath('/html/body/div[26]/div/div/div[2]/button')
save_ok.click()
sleep(2)
close_save = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/button')
close_save.click()
sleep(2)

ad_v = driver.find_element_by_id('btnattach')
ad_v.click()
sleep(5)
el =  driver.find_element_by_id("addTests")
try: driver.execute_script("return arguments[0].scrollIntoView(true);",el)
except:pass
sleep(3)
txt =driver.find_element_by_xpath('/html/body/div[3]/form/div[4]/div[1]/div[2]/section/table/tbody[6]/tr/td[3]/div/div[2]/input').send_keys("filenamehere")
sleep(5)


# up_load = driver.find_element_by_xpath('/html/body/div[3]/form/div[4]/div[1]/div[2]/section/table/tbody[6]/tr/td[3]/div/div[3]/label/input').click()
x=driver.find_element_by_xpath("/html/body/div[3]/form/div[4]/div[1]/div[2]/section/table/tbody[6]/tr/td[3]/div/div[3]/label/input")
driver.execute_script("arguments[0].style.display = 'block';",x)
sleep(5)
x.send_keys("")

sleep(5)
wok= driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button')
sleep(2)
next=driver.find_element_by_xpath('/html/body/div[3]/form/div[4]/div[2]/a[2]').click()
sleep(2)
next =driver.find_element_by_xpath('/html/body/div[3]/form/div[4]/div[2]/a[2]').click()
sleep(2)
close =driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button').click()

# add_vi = driver.find_element_by_xpath('//*[@id="uploadBPM"]').click()


#
# scroll_btm =driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div[3]/table/thead/tr/th[2]')
#
# driver.execute_script("return arguments[0].scrollIntoView(true);",scroll_btm)
# sleep(10)



#
# try:
#     clk_up_btn = driver.find_element_by_xpath('/html/body/form/div/div/div/label')
#     clk_up_btn.click()
#     # insert_ = driver.find_element_by_id('invAttach')
#     # driver.execute_script("arguments[0].style.display = 'block';",insert_)
#     # sleep(5)
#     # insert_.click().perform()
#     # insert_.send_keys("/path/here")
# except:
#     print("cant'nt upload file by id")
#
# try:
#     clk_up_btn = driver.find_element_by_xpath('/html/body/form/div/div/div/label')
#     clk_up_btn.click().perform()
# except:
#     print("cant'nt click upload")
#
#
#
# try:
#     insrt_file = driver.find_element_by_xpath('/html/body/form/div/div/div/label/input')
#     insrt_file.send_keys("/path/here")
#
# except:
#     print("cant'nt upload file by xpath")


#this code cabe used to enable hidden file field and upload path of file
# x=driver.find_element_by_xpath("/html/body/form/div/div/div/label/input")
# driver.execute_script("arguments[0].style.display = 'block';",x)
# sleep(5)
# x.send_keys("C:/Users/B hghgjgjh.jpg")







#
#
#




