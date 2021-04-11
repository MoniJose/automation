from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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
sleep(25)


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




close_b = driver.find_element_by_xpath('/html/body/div[18]/div/div/div[3]/button')
close_b.click()
sleep(3)
# upload = driver.find_element_by_xpath('/html/body/form/div/div/div/label')
# upload.send_keys(r'C:\Users\PC\Downloads\KASP-PMJAY_files\PREDIALYSISxPHOTO_IBRAHIM_PS8VO3JD0_99_50_23124_20210407_123113_26\JPEG File (.jpeg')
# photo = driver.find_element_by_id('invAttach')
# driver.execute_script('arguments[0].style.display="block";',photo)
# sleep(3)

# upload = driver.find_element_by_xpath('//*[@id="invAttach"]')
# upload.send_keys(r'C:\Users\PC\Downloads\KASP-PMJAY_files\PREDIALYSISxPHOTO_IBRAHIM_PS8VO3JD0_99_50_23124_20210407_123113_26\JPEG File (.jpeg)')
ip_no = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/input')
ip_no.send_keys(ip_num)

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

alldate = driver.find_element_by_xpath('/html/body/div[25]/div[1]/table')
alldate.send_keys(treatment_d)
sleep(2)
procedure_con = driver.find_element_by_xpath('//*[@id="procedureConsent"]')
procedure_con.click()
MLC = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/input[2]')
MLC.click()
sleep(10)



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
pulse_r.send_keys(78)
sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input').click()
bp = driver.find_element_by_name('GE14')
bp.send_keys(x)
sleep(2)
bp_h = driver.find_element_by_name('BP1')
bp_h.send_keys(y)
sleep(5)
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
sleep(3)
add_vi = driver.find_element_by_xpath('//*[@id="uploadBPM"]').click()





# sub

queries = driver.find_element_by_xpath('/html/body/div[25]/div/div/div[2]/button[2]')
queries.click()
sleep(2)
q1 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[1]/td[3]/label[1]/span[2]').click()
q2 = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div/table/tbody/tr[2]/td[3]/label[1]/span[2]').click()
q3 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[3]/td[3]/label[1]/span[2]').click()
q4 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[4]/td[3]/label[1]/span[2]').click()
q5 = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div/table/tbody/tr[5]/td[3]/label[1]/span[2]').click()
submit_q = driver.find_element_by_id('btnSubmit')
submit_q.click()
q_ok = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button').click()