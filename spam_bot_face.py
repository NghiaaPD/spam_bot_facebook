from selenium import webdriver
from time import*
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get("https://www.facebook.com/")

User = browser.find_element("name", "email")
User.send_keys("Username")

Passwd = browser.find_element("id", "pass")
Passwd.send_keys("Password")

Passwd.send_keys(Keys.ENTER)

sleep(5)

browser.get("facebook_account")

sleep(3)

Nt = browser.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div")
Nt.click()
sleep(5)
while True:
    Nt = browser.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")
    Nt.send_keys("thứ muốn nói nhập ở đây nha :))))")
    sleep(5)
    #Nt = browser.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div/div")
    Nt.send_keys(Keys.ENTER)

    sleep(2)