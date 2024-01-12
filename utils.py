from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import bs4
import logging
from colorlog import ColoredFormatter
import json
import sys 
import os


# Redirect stderr to a file (replace 'error_log.txt' with your desired file name)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create formatter
formatter = ColoredFormatter(
    "%(log_color)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'red',
        'WARNING': 'yellow',
        'ERROR': 'green',
        'CRITICAL': 'red',
    },
    secondary_log_colors={},
    style='%'
)


handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_page_source(url):
    sys.stderr = open(os.devnull, 'w')
    logger.info("Opening Linkedln")
    chrome_options = Options()
    chrome_options.add_argument("C:\kush\Projects\linkdln_scrapper\chromedriver-win64\chromedriver.exe")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://linkedin.com/uas/login")

    print(f"entering Email")
    time.sleep(random.randint(5,7))

    email = "strawhatluffy0802@gmail.com"
    password = "Luffy0802"
    username = driver.find_element(By.ID, "username")
    username.send_keys(email) 
    time.sleep(random.randint(1,3))

    print("Entering Password")
    pword = driver.find_element(By.ID, "password")
    pword.send_keys(password)	 
    time.sleep(random.randint(1,3))

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    logger.info("Moving to the given URL")
    profile_url = url
    driver.get(profile_url)  
    time.sleep(random.randint(3,5))

    start = time.time()

    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll = finalScroll
        finalScroll += 1000

        time.sleep(3)
        end = time.time()

        if round(end - start) > 10:
            break

    src = driver.page_source
    soup = bs4.BeautifulSoup(src, 'html.parser')
    # print(soup)

    time.sleep(3)
    driver.quit()


    with open('page_source.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())