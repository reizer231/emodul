from selenium import webdriver
import links


def change_scheme(x):

    username = "username" #Specify your username
    password = "password" #Specify your password

    url = "https://emodul.pl/login"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(links.username_input).send_keys(username)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(links.password_input).send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(links.login_button).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(links.work_scheme).click()

    if x == 1 :
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_boiler_prio).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_click).click()
        print("Done changed to Boiler Prio")
    elif x == 2:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_house_heat).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_click).click()
        print("Done changed to house heating")
    elif x == 3:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_pumps_paral).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_click).click()
        print("Done  changed to parallel pumps")
    elif x == 4:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_summer_sch).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(links.work_scheme_click).click()
        print("Done  changed to summer scheme")
    else:
        print("Please provide correct choice of work scheme!")

change_scheme(1) #Here we are calling function 1-Priorytet boilera 2-Ogrzewanie domu 3-pompy równoległe 4-Tryb letni.