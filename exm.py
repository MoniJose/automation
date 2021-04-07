from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver.exe")
driver.get("https://pmjaylive.sevensigma.in/Hospitals")
e1 = driver.find_element_by_name('User Name')
e1.send_keys("8590050640")
e2 = driver.find_element_by_name('Password')
e2.send_keys("50640")
e3 = driver.find_element_by_class_name('btn')
e3.click()
import time
time.sleep(3)
x=driver.find_elements_by_xpath("//html/body/div/div[2]/div/div/div/div/div[3]/div/div/div[4]/div/div[2]/table/thead/tr")[0].text
print(x)
y=driver.find_elements_by_xpath("//*[@id='out-table']/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[5]/div/button[1]")[0].click() #view
print(y)
import time
time.sleep(3)
z=driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div/div[1]").click() #pre
print(z)


time.sleep(3)
number_of_rows= len(driver.find_elements_by_xpath('//*[@id="out-table"]/div[1]/div/div[4]/div'))

print(number_of_rows)

id_list=[]# list creation
for i in range(1,number_of_rows+1):
    u=driver.find_elements_by_xpath("//*[@id='out-table']/div[1]/div/div[4]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[3]")[0].text
    print(u)
    id_list.append(u)

time.sleep(1)
print(id_list) #=>>>> ['2195488', '2195491']





# second page

driver.get("https://tms.pmjay.gov.in/OneTMS/loginAction.do")
Registration_No = []
numberr_of_rows = len(driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr'))

#//*[@id="no-more-tables"]/table/tbody/tr[1]/td[2]/a/b/u
# //*[@id="no-more-tables"]/table/tbody/tr[2]/td[2]/a/b/u
# //*[@id="no-more-tables"]/table/tbody/tr[4]/td[2]/a/b/u
for j in range(1,numberr_of_rows+1):
    ids = driver.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr['+ str(j) +']/td[2]/a/b/u')
    print(ids)
    Registration_No.append(ids)

    from selenium import webdriver

    driver =
    driver.get("")
    element = driver.find_element
    ele = element.get_attribute('innerHTML')
    e = driver.find_element_by_xpath("")
    e.send_keys(ele)



print(Registration_No) #==>>>[1,2,2,4]


for k in range(len(id_list)):
    current_element_from_id_list = id_list[k]
    for l in range(len(Registration_No)):
        if current_element_from_id_list == Registration_No[l]:
            print("Registration_No found :" + list)
            driver.find_element_by_xpath('//*[@id="no-more-tables"]current_element_from_id_/table/tbody/tr[' + str(l+1) + ']/td[]/a').click()
# driver.find_element_by_link_text("Patients").click()
# sleep(8)
# # driver.find_element_by_link_text("Register Patient").click()
# preauth =driver.find_element_by_link_text('Preauth')
# preauth.click()
# sleep(5)
# id_type = driver.find_element_by_xpath('//*[@id="select2-idType-container"]')
# id_type.send_keys('PMJAY ID')
# driver.find_element_by_xpath('//*[@id="idNo"]')