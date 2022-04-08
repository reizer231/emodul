from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
import os, signal


username = "usrname" #Specify your username
password = "passwd" #Specify your password
json1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/tile/div"
json2 = "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/button[3]"
username_input = "/html/body/div/div/div[2]/div/div/div[2]/form/input[1]"
password_input = "/html/body/div/div/div[2]/div/div/div[2]/form/input[2]"
login_button = "/html/body/div/div/div[2]/div/div/div[2]/form/input[3]"

url = "https://emodul.pl/login"
driver = webdriver.Firefox(firefox_options=options, executable_path ="/usr/local/bin/geckodriver")
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_xpath(username_input).send_keys(username)
driver.implicitly_wait(10)
driver.find_element_by_xpath(password_input).send_keys(password)
driver.implicitly_wait(10)
driver.find_element_by_xpath(login_button).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(json1).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(json2).click()

#Killing all firefox processes as in my case driver.close() was not working.
name = "firefox"
for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
    fields = line.split()
    # extracting Process ID from the output
    pid = fields[0]
    # terminating process
    os.kill(int(pid), signal.SIGKILL)

print("Done! Toggled firing up/down!") 
