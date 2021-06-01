
# STEP 1: GET THE URL

# import the required libraries

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

PATH = "/home/sunbeam/selenium/chromedriver"
driver = webdriver.Chrome(PATH)
endgameurl = "https://www.imdb.com/title/tt4154796/reviews?ref_=tt_ov_rt"

driver.get(endgameurl)

html = driver.page_source.encode('utf-8')
page_num = 0

while driver.find_element_by_css_selector('#load-more-trigger'):
    if page_num == 25:
        break
    else:
        driver.find_element_by_css_selector('#load-more-trigger').click()
        page_num += 1
        print("getting page number "+str(page_num))
        time.sleep(5)
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
reviews2 = soup.findAll(class_='title')

for rev1 in reviews1:
    data.append(rev1.text.replace('\n', ' ').replace('\r', ''))
    # df.append(rev.text)
    # print(rev.text)
# print(data)

for rev2 in reviews2:
    # print(rev2.text)
    data.append(rev2.text.replace('\n', ' ').replace('\r', ''))
# print(data)
# df2 = pd.DataFrame(data)
# print(data)

import random
random.shuffle(data)
df = pd.DataFrame(data)
# df = df.sample(frac=1) # to shuffle Dataframe randomly
print(df)
df.to_csv('Avengers.csv', header=False)
driver.close()
# print(myrev)
# print(myrev.__class__)
