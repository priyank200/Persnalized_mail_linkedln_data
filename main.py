from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import bs4
import logging
from colorlog import ColoredFormatter
import json
import utils
import mail


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


Information = {}

logger.info("DO WE HAVE A NEW LINKEDLN URL?\nPress\n1 for Yes\n0 for No")
permission = input()

if(permission == "1"):
    logger.info("Give URL")
    url = input()
    utils.get_page_source(url)


with open('page_source.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

# print(html_content)
        
soup = bs4.BeautifulSoup(html_content, 'html.parser')


logger.info("COLLECTNG LINKEDLN DATA:")

name = soup.find('h1',{'class' : 'text-heading-xlarge inline t-24 v-align-middle break-words'}).text.strip()
headline = soup.find('div',{'class':'text-body-medium break-words'}).text.strip()

Information["Name"] = name
Information["Headline"] = headline
# print(Information)
print(f"Name = {name}")
print(f"headline = {headline}")
print("##########################################################################")

refer = soup.find_all('section',{'class':'artdeco-card pv-profile-card break-words mt2'})

for e in refer:
    # TO FIND ABOUT SECTION INFORMATION
    if(e.find('div',{'id':'about'})):
        logger.info("Collection About...........")
        about_element = e.find('div',{"class":'display-flex full-width'})
        about_element2 = about_element.find('span',{'class':'visually-hidden'}) if about_element else None
        About = about_element2.text.strip() if about_element2 else None
        print(f'{About = }')
        Information["About"] = About
        print("##########################################################################")
        top_skill_section = e.find('div',{'class':'pvs-list__outer-container'})
        # print(top_skill_section.text.strip())
        if(top_skill_section):
            logger.info("Collection TOP SKILLS.......")
            skills_element1 = top_skill_section.find('div',{'class':'display-flex align-items-center t-14 t-normal'})
            skills = skills_element1.find('span',{'class':'visually-hidden'}).text.strip() if skills_element1 else None
            print(f'{skills = }')
            Information["SKills"] = skills
            print("##########################################################################")

    # TO FIND EDUCATION INFORMATION
    if(e.find('div',{'id':'education'})):
        college_info = {}
        # print(e.find('div',{'class':'pvs-list__outer-container'}).find_all('span',{'class':'visually-hidden'}))
        logger.info('Collection Education Information.........')
        for ele in e.find('div',{'class':'pvs-list__outer-container'}).find_all('div',{"data-view-name":'profile-component-entity'}):
            # print(ele.text.strip())
            college_name_element1 = ele.find('div',{'class':'display-flex full-width'})
            college_name_element2 = college_name_element1.find('span',{'class':'visually-hidden'}) if college_name_element1 else None
            college_name = college_name_element2.text.strip() if college_name_element2 else None

            degree_name_element1 = ele.find('span',{'class':'t-14 t-normal'})
            degree_name_element2 = degree_name_element1.find('span',{'class':'visually-hidden'}) if degree_name_element1 else None
            degree_name = degree_name_element2.text.strip() if degree_name_element2 else None
            # print(f"{college_name = }")
            # print(f"{degree_name = }")
            college_data = {
                            "Name": college_name,
                            "Degree": degree_name
                            }
            college_info[f"College_{len(college_info) + 1}"] = college_data
        Information["College"] = college_info

        print("##########################################################################")
    #TO FIND EXPERIENCE INFORMATION
    if(e.find('div',{'id':'experience'})):
        Exp_info = {}
        logger.info('Collection Work Experience Information.......')
        for ele in e.find('div',{'class':'pvs-list__outer-container'}).find_all('div',{"data-view-name":'profile-component-entity'}):
            # print(ele)
            company_name_element = ele.find('span',{'class':'t-14 t-normal'})
            # print(company_name_element)
            company_name_element2 = company_name_element.find('span',{'class':'visually-hidden'}) if company_name_element else None
            # print(company_name_element2)
            company_name = company_name_element2.text.strip() if company_name_element2 else None

            compnay_url_element = ele.find('a', class_='optional-action-target-wrapper')
            compnay_url =  compnay_url_element['href'] if compnay_url_element else None

            Person_post_element = ele.find('div',{'class':'display-flex full-width'})
            person_post_second_element = Person_post_element.find('span', class_="visually-hidden") if Person_post_element else None
            Person_post = person_post_second_element.text.strip() if person_post_second_element else None

            # print(f"{company_name = }")
            # print(f"{compnay_url = }")
            # print(f"{Person_post = }")
            exp_data = {"Company_name":company_name,
                        "Company_url":compnay_url,
                        "Person Post":Person_post}
            Exp_info[f"Experience_{len(Exp_info)+1}"] = exp_data
        Information["Experience"] = Exp_info
        print("##########################################################################")  

# print(Information)

json_filename = 'information.json'
with open(json_filename, 'w') as json_file:
    json.dump(Information, json_file, indent=4)

mail.Write_Email(json_filename)

