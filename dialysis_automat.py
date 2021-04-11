# import unittest
# import time
# from selenium import webdriver
#
# target_year = " "
# target_month =" "
# target_date = " "
# space = " "
#
#
# driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
# driver.get('http://jqueryui.com/resources/demos/datepicker/other-months.html')
# datepicker_val = driver.find_element_by_id('datepicker')
# datepicker_val.click()
#
# target_month_year_string = target_month + space + target_year
#
# elem_selected_year = driver.find_element_by_class_name("ui-datepicker-year")
# selected_year_string = elem_selected_year.get_attribute("innerHTML")
#
# elem_selected_month = driver.find_element_by_class_name("ui-datepicker-month")
# selected_month_string = elem_selected_month.get_attribute("innerHTML")
#
# # Concatenate selected month and year strings
# selected_month_year_string = selected_month_string + selected_year_string
#
# previous_button_xpath = "//*[@id='ui-datepicker-div']/div/a[1]"
# next_button_xpath = "//*[@id='ui-datepicker-div']/div/a[2]"
#
# # Navigate through the calendar to go to the required year
# # and than the required month
#
# while (selected_month_year_string != target_month_year_string):
#     if (((int(target_year)) < int(selected_year_string))):
#         # Click the next button
#         previous_click = driver.find_element_by_xpath(previous_button_xpath)
#         previous_click.click()
#     else:
#         next_click = driver.find_element_by_xpath(next_button_xpath)
#         next_click.click()
#
#     elem_selected_year = driver.find_element_by_class_name("ui-datepicker-year")
#     selected_year_string = elem_selected_year.get_attribute("innerHTML")
#
#     elem_selected_month = driver.find_element_by_class_name("ui-datepicker-month")
#     selected_month_string = elem_selected_month.get_attribute("innerHTML")
#
#     # Compute the final day-month-year string
#     selected_month_year_string = selected_month_string + space + selected_year_string
#
# elem_date = driver.find_element_by_xpath(
#     "//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='" + target_date + "']")
# elem_date.click()
#
# time.sleep(10)
#
# # Check the selected month, date, and year from the Calendar
# selected_month_year_val = datepicker_val.get_attribute('value')
# print(selected_month_year_val)
#
#
#
# print("Unit Test of jQuery Calendar passed")

# import os
# import time
#
# import selenium
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# # Variables
# # TODO: change this back to non-webdriver variable
# driver = 0
#
#
# def enter_something(xpath, value):
#     driver.find_element_by_xpath(xpath).send_keys(value)



# def check_exists_by_xpath(xpath):
#     try:
#         driver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True


# def check_exists_by_xpath2(xpath):
#     try:
#         driver2.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True
#
#
# def driver_init():
#     global driver
#
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
# check_values = {}
# required_values = {}
#
#
# # TODO: listening part

def gather_check_values():
    global check_values, username, password, serviceNo
    driver2 = webdriver.Chrome()
    driver2.get('http://sevensigmahealthcaresolutions.com/esi.php?user=auto')
    driver2.switch_to.frame('mt')
    driver2.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td/a').click()
    time.sleep(2.5)
    username = driver2.find_element_by_name('huser').get_attribute('value')
    password = driver2.find_element_by_name('hpassword').get_attribute('value')
    check_values['Dispensary'] = driver2.find_element_by_name('referredby').get_attribute('value')
    check_values['referralNo'] = driver2.find_element_by_name('refno').get_attribute('value')
    serviceNo = driver2.find_element_by_name('serviceno').get_attribute('value')
    print(f'Details entered are stored successfully')


claim_present_refrlItem = {
    'serviceNo':      '//*[@id="ccd"]/table/tbody/tr[5]/td[2]',
    'referralNo':     '//*[@id="referral"][2]/td[2]',
}
claim_absent_rfrlItem = {
    'referralNo':       '//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td[2]',
    'Dispensary':       '//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td[4]',
}

def click_on_item(xpath):
    WebDriverWait(driver,100).until(EC.visibility_of_element_located((By.XPATH,xpath)))
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)


   # driver.find_element_by_xpath('//*[@id="txtCaptcha"]').send_keys(driver.find_element_by_id('chkcaptcha').get_attribute('value'))
   # time.sleep(5)
   #driver.find_element_by_xpath('//*[@id="remember_password"]/td/input').click()

    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[3]/table/tbody/tr[9]/td/input').click()
    click_on_item('//*[@id="ihaveseennmi"]')

def login():
    global username, password
    driver.get('https://www.echsbpa.utiitsl.com/ECHS/')
    click_on_item('//*[@id="messagetable"]/tbody/tr[4]/td/input')
    element2 = driver.find_element_by_name('username')
    element3 = driver.find_element_by_name('password')
    element2.send_keys(username)
    element3.send_keys(password)

    driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[3]/table/tbody/tr[9]/td/input').click()
    click_on_item('//*[@id="ihaveseennmi"]')


# def selectOption(Option):


def goto(site):
    driver.get(site)



def value(xpath):
    return driver.find_element_by_xpath(xpath).text.strip()


def acceptReferral(referralDict,xlDict,clmIdPresence):
    global clmId
    if clmIdPresence:
        driver.find_element_by_xpath('//*[@id="tr_bpa"]/td[2]/input').send_keys(referralDict.claimId)
        click_on_item('//*[@id="tbl_main"]/tbody/tr[7]/td/input')
    else:
        click_on_item('//*[@id="li_0"]')
        click_on_item('//*[@id="0"]/li[6]/a')
        click_on_item('//*[@id="referralFrom"]')
        click_on_item('//*[@id="referralFrom"]/option[2]')
        click_on_item('//*[@id="referredDispensary"]')
        found = False
        for opt in range(len(driver.find_elements_by_xpath('//*[@id="referredDispensary"]/option'))):
            if xlDict['Dispensary'].lower() in driver.find_element_by_xpath(f'//*[@id="referredDispensary"]/option[{opt+1}]').text.lower():
                click_on_item(f'//*[@id="referredDispensary"]/option[{opt+1}]')
                found = True
        if found == False:
            errorMessage('Couldn\'nt find dispensary')
            driver_close()
            return 0
        rfrlNo2 = xlDict['referralNo'].replace(driver.find_element_by_xpath('//*[@id="tr_sinfo"]/td[2]/input[1]').get_attribute('value'),'')
        driver.find_element_by_xpath('//*[@id="tr_sinfo"]/td[2]/input[2]').send_keys(rfrlNo2)
        click_on_item('//*[@id="tbl_main"]/tbody/tr[7]/td/input')
        if check_exists_by_xpath('//*[@id="popup2"]') :
            if 'claim' in driver.find_element_by_xpath('//*[@id="messagetable"]/tbody/tr[2]/td').text:
                split1 = driver.find_element_by_xpath('//*[@id="messagetable"]/tbody/tr[2]/td').text.split(' - ')
                clmId = split1[1].split(' ')[0]
                errorMessage(f'{clmId} alrdy made')
                driver_close()
                return 0
            elif 'server' in driver.find_element_by_xpath('//*[@id="messagetable"]/tbody/tr[2]/td').lower():
                errorMessage('server issue')
                driver_close()
            else:
                errorMessage('Please Reenter and try again')
                driver_close()
                return 0
        else:
            if checkFields2(referralDict,xlDict) == 'Matching' and serviceNo in value('//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[6]/td[4]'):
                print('It is working')
                click_on_item('//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[18]/td/input')
                click_on_item('//*[@id="submit_save"]/td/input')
                clmId = value('//*[@id="messagetable"]/tbody/tr[2]/td').split(' - ')[1][0:-1]
                print(f'{clmId} is now generated. ')
            else:
                print(f'Referral No. {xlDict["referralNo"]} is not matching')
                errorMessage('Not Generated')
        return 1


def get_required_values():
    global required_values, clmId
    click_on_item('//*[@id="messagetable"]/tbody/tr[4]/td/input')
    click_on_item('//*[@id="li_6"]')
    click_on_item('//*[@id="6"]/li[2]/a')
    enter_something('//*[@id="searchValue"]', str(clmId))
    click_on_item('//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[5]/td/input')
    click_on_item('//*[@id="name"]/table/tbody/tr/td[1]/a')
    required_values['name'] = value('//*[@id="ccd"]/table/tbody/tr[8]/td[2]')
    required_values['age'] = value('//*[@id="ccd"]/table/tbody/tr[7]/td[4]')
    required_values['gender'] = value('//*[@id="ccd"]/table/tbody/tr[8]/td[4]')
    required_values['cardNo'] = value('/html/body/table/tbody/tr[2]/td[2]/form/table[1]/tbody/tr[5]/td/div/div[1]/table/tbody/tr[2]/td[2]')
    required_values['claimId'] = clmId
    click_on_item('/html/body/table/tbody/tr[2]/td[2]/form/table[1]/tbody/tr[5]/td/div/ul/li[2]/a')
    required_values['doi'] = value('/html/body/table/tbody/tr[2]/td[2]/form/table[1]/tbody/tr[5]/td/div/div[2]/table[2]/tbody/tr[6]/td[2]')
    required_values['valUpto'] = value('/html/body/table/tbody/tr[2]/td[2]/form/table[1]/tbody/tr[5]/td/div/div[2]/table[2]/tbody/tr[6]/td[4]')
    required_values['remarks'] = value('/html/body/table/tbody/tr[2]/td[2]/form/table[2]/tbody/tr[2]/td[2]')



def fill_values_app():
    global required_values
    driver2.switch_to.default_content()
    driver2.switch_to.frame('mt')
    driver2.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td/a').click()
    driver2.switch_to.default_content()
    driver2.switch_to.frame('mb')
    time.sleep(2.5)
    driver2.find_element_by_name('patientname').send_keys(required_values['name'])
    driver2.find_element_by_name('age').send_keys(required_values['age'])
    driver2.find_element_by_name('gender').send_keys(required_values['gender'])
    driver2.find_element_by_name('claimid').send_keys(required_values['claimId'])
    driver2.find_element_by_name('dtofissue').send_keys(required_values['doi'])
    driver2.find_element_by_name('validupto').send_keys(required_values['valUpto'])
    driver2.find_element_by_name('remarks').send_keys(required_values['remarks'])
    driver2.find_element_by_name('cardno').send_keys(required_values['cardNo'])
    driver2.find_element_by_name('claimu').click()
    time.sleep(2.5)
    driver2.close()


def errorMessage(msg):
    driver2.switch_to.default_content()
    driver2.switch_to.frame('mb')
    time.sleep(2.5)
    driver2.find_element_by_name('claimid').send_keys(msg)
    driver2.find_element_by_name('claimu').click()
    time.sleep(2.5)
    driver2.close()
# def savePage(id):
#     if checkFields2():
#         page = driver.page_source
#         file_ = open(os.path.join(os.getcwd(),f'{id}.html'),'w',encoding="utf-8")
#         file_.write(page)
#         file_.close()



def checkFields2(xpathDict,xlDict):
    for x in xpathDict:
        if x not in xlDict:
            print(f'{x} not available!')
            return 'Not Matching'
        print(xlDict[x])
        allMatch = True
        # if x == 'referralNo':
        #     click_on_item('//*[@id="mytabber"]/ul/li[2]/a')
        if  value(xpathDict[x]).lower() != xlDict[x].lower():
            print(f'{x}: {value(xpathDict[x])} != {xlDict[x]}')
            allMatch = False
            return 'Not Matching'
    if allMatch == True:
        click_on_item('//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[18]/td/input')
        return 'Matching'



def driver_close():
    driver.close()



def gather_check_values_with_listener():
    global check_values, username, password, serviceNo, driver2
#     driver2 = webdriver.Chrome()
#     driver2.get('http://sevensigmahealthcaresolutions.com/esi.php?user=auto')
#     driver2.switch_to.frame('mt')
#     driver2.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td/a').click()
#     driver2.switch_to.default_content()
#     driver2.switch_to.frame('mb')
#     time.sleep(2.5)
#     while True:
#         driver2.switch_to.default_content()
#         driver2.switch_to.frame('mt')
#         driver2.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td/a').click()
#         driver2.switch_to.default_content()
#         time.sleep(1.5)
#         driver2.switch_to.frame('mb')
#         time.sleep(2.5)
#         if check_exists_by_xpath2('/html/body/form/table[1]/tbody/tr/td[2]/input'):
#             if driver2.find_element_by_class_name('huser').get_attribute('value') != '':
#                 username = driver2.find_element_by_name('huser').get_attribute('value')
#                 password = driver2.find_element_by_name('hpassword').get_attribute('value')
#                 check_values['Dispensary'] = driver2.find_element_by_name('referredby').get_attribute('value')
#                 check_values['referralNo'] = driver2.find_element_by_name('refno').get_attribute('value')
#                 serviceNo = driver2.find_element_by_name('serviceno').get_attribute('value')
#                 print(f'Details entered are stored successfully')
#                 return 1
