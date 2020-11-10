from selenium import webdriver  #import webdriver
from selenium.webdriver.common.keys import Keys #import keys
from time import sleep
import random
import pyautogui


acess = pyautogui.password("Enter Password")
if(acess != "indev"):
    pyautogui.alert("Acces Denied")
    quit()


amount = 12         #number of posts to like
hashtag = ("")





#get path
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#get webpage

def main():
    driver.get("https://www.instagram.com")
    sleep(5)

    #get element
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")


    # enter username and password
    name.send_keys("")
    password.send_keys("")


    #click login
    login.click()


    #after log in
    sleep(2)
    notnow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()

    sleep(2)
    no_notification = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()



    #HASHTAG

    driver.get("https://www.instagram.com/explore/tags/"+random.choice(hashtag)+"/")
    sleep(1)

       
    #LIKE POSTS

    click_photo = driver.find_element_by_class_name("v1Nh3").click()

    i = 1
    while i <= amount:
        sleep(2)
        heart = driver.find_element_by_class_name("fr66n").click()
        sleep(1)
        arrow_button = driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        i +=1

    driver.quit()


if(acess == "indev"):
    main()








#DONE




