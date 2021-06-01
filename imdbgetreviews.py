# IMPORT THE REQUIRED LIBRARIES
from selenium import webdriver
import time
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

PATH = "/home/sunbeam/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

toptho = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
driver.get(toptho)
movielinks = []

condition = True
while condition:
    print(driver.title)
    for header in driver.find_elements_by_class_name('lister-item-content'):
        print(header.find_element_by_tag_name('a').text)
        mName = header.find_element_by_tag_name('a').text
        print(header.find_element_by_tag_name('a').get_property('href'))
        movielinks.append(header.find_element_by_tag_name('a').get_property('href'))
        # time.sleep(5)
    try:
        if driver.find_element_by_css_selector('#main > div > div.desc > a.lister-page-next.next-page'):
            driver.find_element_by_css_selector('#main > div > div.desc > a.lister-page-next.next-page').click()
        else:
            driver.find_element_by_css_selector('#main > div > div.desc > a').click()

        time.sleep(10)
    except:
        condition = False
        print('you are at the end of the page')
for link in movielinks:
    driver.get(link)
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[3]/div[3]/div[2]/span/a[1]').click()
    except NoSuchElementException:
        print('element not found')
        continue
    time.sleep(3)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.findAll("code"):
        print(i.text)
    print()
    title = soup.title
    print('Title : ', title.text)

    # STEP 1: GET THE URL

    # import the required libraries
    page_num = 0

    while driver.find_element_by_css_selector('#load-more-trigger'):
        if page_num == 25:
            break
        else:
            try:
                driver.find_element_by_css_selector('#load-more-trigger').click()
                page_num += 1
                print("getting page number " + str(page_num))
                time.sleep(5)
            except ElementNotInteractableException:
                print('element not clickable')
                page_num = 25
                continue
    html = driver.page_source.encode('utf-8')

    # r1 = requests.get(endgameurl)
    # htmlContent = r1.content
    # print(htmlContent) # prints the html content / source code
    # soup1 = BeautifulSoup(r1.content, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')  # html.parser
    # print(soup.prettify())

    for i in soup.findAll("code"):
        print(i.text)

    title = soup.title
    # print(title.text)
    # print(soup.findAll('div'))

    # tag = BeautifulSoup('<div class="text show-more__control">', 'html.parser')
    # print(tag)
    # print(soup.get_text)
    import pandas as pd

    data = []
    # print(df)
    reviews1 = soup.findAll(class_='text show-more__control')
    # reviews2 = soup.findAll(class_='title')

    for rev1 in reviews1:
        data.append(rev1.text.replace('\n', ' ').replace('\r', ''))
        # df.append(rev.text)
        # print(rev.text)
    # print(data)

    # for rev2 in reviews2:
    #     # print(rev2.text)
    #     data.append(rev2.text.replace('\n', ' ').replace('\r', ''))
    # print(data)
    # df2 = pd.DataFrame(data)
    # print(data)

    import random

    random.shuffle(data)
    df = pd.DataFrame(data)
    df2 = df.iloc[:, 0]
    # df = df.sample(frac=1) # to shuffle Dataframe randomly
    print(df)
    moviename = driver.find_element_by_xpath('//*[@id="main"]/section/div[1]/div/div/h3/a').text
    df2.to_csv(os.path.join('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/inreviews/', moviename + '.csv'))

driver.close()
# print(myrev)
# print(myrev.__class__)