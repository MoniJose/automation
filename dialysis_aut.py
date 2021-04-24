import os
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

import urllib
import urllib.request
# functions

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True



options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.maximize_window()

driver.implicitly_wait(10)
w = WebDriverWait(driver,8)


# user = input('enter email or phone no')
# pswd = input('enter password')

driver.get('https://pmjaylive.sevensigma.in/home')

user_name = driver.find_element_by_name('User Name')
user_name.send_keys(8590050640)
password = driver.find_element_by_name('Password')
password.send_keys(50640)
driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/form/div/div[3]/button').click()
sleep(3)

view_list = driver.find_element_by_xpath('//*[@id="out-table"]/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]/div/button[1]')
view_list.click()
sleep(3)


preauth = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div/div[1]/div/div[2]/div/p[1]').click()
sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div/div/div/input').send_keys('DIALYSIS')
sleep(10)
dialysis = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
dialysis.click()
sleep(3)

number_of_rows= len(driver.find_elements_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div'))

print(number_of_rows)

id_list=[]# list creation
for i in range(1,number_of_rows+1):
    u=driver.find_elements_by_xpath("//*[@id='out-table']/div[1]/div/div[4]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[3]")[0].text
    print(u)
    id_list.append(u)
    sleep(1)
    # reg_no = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[3]/div')
    # reg = reg_no.get_attribute('innerHTML')

    ip_number = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[7]/div')
    ip_num = ip_number.get_attribute('innerHTML')
    print("ip_num", ip_num)
    view_profile = driver.find_element_by_xpath(
        '//*[@id="out-table"]/div[1]/div/div[4]/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/i')
    view_profile.click()

    treat_date = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div/div[3]/table/tbody/tr/td[9]/div')
    treatment_d = treat_date.get_attribute('innerHTML')
    print("treatment_d", treatment_d)
    card_id = driver.find_element_by_xpath(
        '//*[@id="out-table"]/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[4]/div')
    card = card_id.get_attribute('innerHTML')
    print(card)
    patient_name = driver.find_element_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[5]/div')
    p_name = patient_name.get_attribute('innerHTML')
    print(p_name)
    # dep = driver.find_element_by_xpath('')
    # treat_photo = dep.get_attribute('innerHTML')

    pulse_rate = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/p[2]')
    pulse = pulse_rate.get_attribute('innerHTML')
    print(pulse)
    x = pulse[:3]
    print(x)
    y = pulse[4:6]
    print(y)

    # p_p = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/img')
    # action = ActionChains(driver)
    # action.context_click(p_p).key_down (Keys.SHIFT).perform()
    p_chart1 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/img')
    src1 = p_chart1.get_attribute('src')
    print(src1)

    p_chart2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/img')
    src2 = p_chart2.get_attribute('src')
    print(src2)

    p_patient = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/div/div/div[4]/div/div/div/div[1]/div/div/div/img')
    src3 = p_patient.get_attribute('src')
    print(src3)

    def dl_img(url, file_path, file_name):
        filename = file_name+".jpeg"
        fullfilename = os.path.join(file_path, filename)
        # urllib.urlretrieve(url, fullfilename)
        urllib.request.urlretrieve(url, fullfilename)

    url = src1

    file_name = card

    dl_img(url, r'C:\Users\PC\Desktop\auto', file_name)


    # def dl_img(url, file_path, file_name):
    #     full_path = file_path + file_name + '.jpg'
    #     urllib.request.urlretrieve(url, full_path)


    url = src2

    file_name = p_name

    dl_img(url, r'C:\Users\PC\Desktop\certificate', file_name)
    sleep(2)

    url = src3

    file_name = ip_num

    dl_img(url, r'C:\Users\PC\Desktop\chart', file_name)
    sleep(3)


driver.get('http://tms.pmjay.gov.in/')
sleep(5)


def login_tms():
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
    sleep(15)
    captcha_text.send_keys(Keys.ENTER)
    driver.find_element_by_id('checkSubmit').click()
    login = driver.find_element_by_xpath('//*[@id="login-submit"]')
    login.click()
    sleep(2)



login_tms()


# to click on close session if it shows up
if (check_exists_by_xpath('/html/body/div[10]/div/div/div[3]/button[2]')):
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button').click()
    sleep(2)
    login_tms()


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
regg_no.send_keys(id_list)

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
    ok = driver.find_element_by_xpath('/html/body/div[26]/div/div/div[2]/button[2]')
    ok.click()
    sleep(5)
    print('try')
except:
    sleep(5)
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

    ok = w.until(
        expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[26]/div/div/div[2]/button')))
    ok.click()
    sleep(2)

except:
    pass

close_b = w.until(
          expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="notify"]/div/div/div[3]/button')))

close_b.click()
sleep(3)
seq = driver.find_elements_by_tag_name('iframe')

for num, frame in enumerate(seq):
    print(num, frame.get_attribute("id"))

print("No of frames present in the web page are: ", len(seq))
driver.switch_to.default_content()
sleep(5)
driver.switch_to.frame(driver.find_element_by_id('middleFrame'))
sleep(5)


try:
         driver.find_element_by_xpath('/html/body/div[26]/div/div/div[2]/button').click()
except:
    pass
driver.switch_to.default_content()
sleep(1)
driver.switch_to.frame(driver.find_element_by_id('middleFrame'))
sleep(2)
# driver.switch_to.frame(driver.find_element_by_id('iframe1'))
if check_exists_by_id("iframe1") and check_exists_by_id("iframe2"):
    # driver.switch_to.frame(driver.find_element_by_id('iframe1'))
    # upload_p = driver.find_element_by_id('invattachButton')
    # upload_p.send_keys(r'C:\Users\PC\Desktop\certificate\MUHAMMED ASHRAF .jpeg')
    driver.switch_to.frame(driver.find_element_by_id('iframe1'))
    upload = driver.find_element_by_xpath('//*[@id="invAttach"]')
    file_path = r'C:\Users\PC\Desktop\chart'
    filename = ip_num + ".jpeg"
    fullfilename = os.path.join(file_path, filename)
    upload.send_keys(fullfilename)
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_id('iframe2'))
    upload_p = driver.find_element_by_xpath('//*[@id="invAttach"]')
    file_path = r'C:\Users\PC\Desktop\certificate'
    filename = p_name + ".jpeg"
    fullfilename = os.path.join(file_path, filename)
    upload_p.send_keys(fullfilename)


elif check_exists_by_id("iframe0") and check_exists_by_id("iframe1"):
    driver.switch_to.frame(driver.find_element_by_id('iframe0'))
    upload = driver.find_element_by_xpath('//*[@id="invAttach"]')
    file_path = r'C:\Users\PC\Desktop\chart'
    filename = ip_num + ".jpeg"
    fullfilename = os.path.join(file_path, filename)
    upload.send_keys(fullfilename)
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_id('iframe1'))
    upload_p = driver.find_element_by_xpath('//*[@id="invAttach"]')
    file_path = r'C:\Users\PC\Desktop\certificate'
    filename = p_name + ".jpeg"
    fullfilename = os.path.join(file_path, filename)
    upload_p.send_keys(fullfilename)

    # # upload on iframe0 and then iframe1
    # print("uploaded")
else:
    print("something went wrong")
    exit()





driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id("middleFrame"))


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





general_find = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[1]')
top = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[1]')
driver.execute_script("return arguments[0].scrollIntoView(true);",top)
sleep(10)
general_find.click()
sleep(20)

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
sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div[14]/div[1]/input').click()
bp = driver.find_element_by_name('GE14')
bp.send_keys(x)
sleep(2)
bp_h = driver.find_element_by_name('BP1')
bp_h.send_keys(y)
sleep(5)
w.until(
        expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div[2]/form/div[2]/div/div/div[2]/div[2]/button'))).click()


sleep(5)
save_ok = w.until(
        expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[27]/div/div/div[2]/button')))
save_ok.click()

sleep(2)
close_save = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/button')
close_save.click()
sleep(2)

sleep(5)
pf_history = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div/div[8]/button[3]')
topp = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div')
driver.execute_script("return arguments[0].scrollIntoView(true);",topp)
sleep(10)
pf_history.click()
sleep(20)
not_applicable = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div[12]/div[1]/input')
not_applicable.click()
save_history = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/form/div[2]/button')
save_history.click()
sleep(3)
ok_history = driver.find_element_by_xpath('/html/body/div[27]/div/div/div[2]/button')
ok_history.click()
sleep(2)
close_history = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[1]/button')
close_history.click()
sleep(3)

action_typ = driver.find_element_by_id('actionType')
drop = Select(action_typ)
drop.select_by_visible_text('Initiate Pre-auth')
sleep(2)

add_view = driver.find_element_by_id('btnattach')
add_view.click()
driver.switch_to.default_content()
sleep(1)
driver.switch_to.frame('middleFrame')
sleep(2)
driver.switch_to.frame(driver.find_element_by_id('modalattDivIframe'))
p_photo = driver.find_element_by_xpath('//*[@id="BPM1"]')
file_path = r'C:\Users\PC\Desktop\auto'
filename = card + ".jpeg"
full_filename = os.path.join(file_path, filename)
p_photo.send_keys(full_filename)
p_ok = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button')
p_ok.click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('middleFrame'))
p_close = driver.find_element_by_xpath('//*[@id="modalattachDiv"]/div/div/div[3]/button')
p_close.click()

# submit = driver.find_element_by_xpath('//*[@id="btnSubmit"]')
# submit.click()
# sleep(2)
# QA_button = driver.find_element_by_xpath('/html/body/div[26]/div/div/div[2]/button[2]')
# QA_button.click()
# sleep(2)
# Q1 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[1]/td[3]/label[1]/span[2]')
# Q1.click()
# Q2 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[2]/td[3]/label[1]/span[2]')
# Q2.click()
# Q3 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[3]/td[3]/label[1]/span[2]')
# Q3.click()
# Q4 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[4]/td[3]/label[1]/span[2]')
# Q4.click()
# Q5 = driver.find_element_by_xpath('//*[@id="triggerDetails"]/div/table/tbody/tr[5]/td[3]/label[1]/span[2]')
# Q5.click()
# sleep(3)
# Q_ok = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button')
# Q_ok.click()
# Q_close = driver.find_element_by_xpath('//*[@id="questionaireModal"]/div/div/div[1]/button')
# Q_close.click()
# sleep(2)
# intiate = driver.find_element_by_xpath('/html/body/div[26]/div/div/div[2]/button[2]')
# intiate.click()
# sleep(5)
# case_id = driver.find_element_by_xpath('/html/body/form[1]/center[1]/font/div/div/div[2]/div/strong/b[2]')
# id_value = case_id.get_attribute('innerHTML')
# sleep(2)
# sub_id = driver.find_element_by_xpath('//*[@id="generateCasePrintPage"]')
# sub_id.click()
# sleep(10)
# case_sd = driver.find_element_by_xpath('//*[@id="childmenu3"]/li[2]/a/span[1]')
# case_sd.click()
# sleep(2)
# case_no = driver.find_element_by_name('caseNo')
# case_no.send_keys(id_value)
# search_no = driver.find_element_by_xpath('//*[@id="preauthForApproval"]/div[3]/button[1]')
# search_no.click()
# sleep(3)
# caseno = driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr/td[2]/b/u/a')
# caseno.click()
# close_n = driver.find_element_by_xpath('//*[@id="notify"]/div/div/div[3]/button')
# close_n.click()
#
# # authonticate
#
# covid_case = driver.find_element_by_xpath('//*[@id="covidNo"]')
# covid_case.click()
# sleep(1)
# t_dr = driver.find_element_by_xpath('//*[@id="collapseTrtDr"]/div[1]/span/span[1]/span/span[2]')
# t_dr.click()
# driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('Specialist')
# specialist = driver.find_element_by_xpath('//*[@id="select2-docType-result-ib3j-D"]')
# specialist.click()