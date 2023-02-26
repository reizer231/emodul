from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, signal

usernameStr = "usrname"  # Specify your username
passwordStr = "passwd"  # Specify your password

browser = webdriver.Firefox(options=opts, executable_path="/usr/local/bin/geckodriver")
browser.get(("https://emodul.pl/login"))

username = browser.find_element(By.NAME, "username")
username.send_keys(usernameStr)
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password.send_keys(passwordStr)
signInButton = browser.find_element(
    By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/form/input[3]"
)
signInButton.click()
fireup_stageone = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/tile/div/div",
        )
    )
)
fireup_stageone.click()
fireup_stagetwo = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/button[3]",
        )
    )
)
fireup_stagetwo.click()

# killing firefox in environment -somehow driver.close() not working
name = "firefox"
for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
    fields = line.split()
    # extracting Process ID from the output
    pid = fields[0]
    # terminating process
    os.kill(int(pid), signal.SIGKILL)


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Done! Toggled firing up/down!"]
