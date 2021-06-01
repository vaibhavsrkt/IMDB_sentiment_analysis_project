#IMPORT THE REQUIRED LIBRARIES
from selenium import webdriver
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

PATH = "/home/sunbeam/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

toptho = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
driver.get(toptho)

moviedict = {'movies': [], 'genres': [], 'directors': [], 'writers': [], 'cast': []}
movielinks = []
# for header in driver.find_elements_by_class_name('lister-item-content'):
#     print(header.find_element_by_tag_name('a').text)
#     mName = header.find_element_by_tag_name('a').text
#     moviedict['movies'].append(mName)
#     print(header.find_element_by_tag_name('a').get_property('href'))
#     time.sleep(5)
    # driver.get(toptho)
condition = True
while condition:
    print(driver.title)
    for header in driver.find_elements_by_class_name('lister-item-content'):
        print(header.find_element_by_tag_name('a').text)
        mName = header.find_element_by_tag_name('a').text
        moviedict['movies'].append(mName)
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
        condition=False
        print('you are at the end of the page')
for link in movielinks:
    driver.get(link)
    time.sleep(5)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.findAll("code"):
        print(i.text)
    print()
    title = soup.title
    print('Title : ', title.text)
    print()
    genreList = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                 'Fantasy', 'Game Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
                 'Romance', 'Sci-Fi', 'Sport', 'Superhero', 'Talk Show', 'Thriller', 'War', 'Western']
    ingenres = []
    indirectors = []
    inwriters = []
    incast = []
    # print(soup.findAll('div', attrs={'class':'subtext'}))
    print('\nGenres :')
    for div in soup.findAll('div', attrs={'class': 'subtext'}):
        for genre in div.findAll('a'):
            if genre.contents[0] in genreList:
                print(genre.contents[0])
                ingenres.append(genre.contents[0])
    moviedict['genres'].append(ingenres)

    # for div2 in soup.findAll('div', attrs={'class': 'credit_summary item'}):
    #     print(div2)
    # print('\nDirectors :')
    for info in driver.find_elements_by_class_name('credit_summary_item'):
        for tag in info.find_elements_by_tag_name('h4'):
            if tag.text == 'Directors:' or tag.text == 'Director:':
                print('\nDirectors: ')
                for inf in info.find_elements_by_tag_name('a'):
                    print(inf.text)
                    indirectors.append(inf.text)
            if tag.text == 'Writers:':
                print('\nWriters: ')
                for inf in info.find_elements_by_tag_name('a'):
                    if inf.text != '14 more credits':
                        print(inf.text)
                        inwriters.append(inf.text)
            if tag.text == 'Stars:':
                print('\nStars: ')
                for inf in info.find_elements_by_tag_name('a'):
                    if inf.text != 'See full cast & crew':
                        print(inf.text)
                        incast.append(inf.text)
        moviedict['directors'].append(indirectors)
        moviedict['writers'].append(inwriters)
        moviedict['cast'].append(incast)
        # print(director.text)
print(moviedict)
outcrawler = pd.DataFrame.from_dict(moviedict)
outcrawler.to_csv('outCrawlMovieData.csv')
driver.close()
exit()
#
# //*[@id="main"]/div/div[4]/a[2]
# //*[@id="main"]/div/div[4]/a
# //*[@id="main"]/div/div[4]/a[2]
#
#
#
# previous css #main > div > div.desc > a.lister-page-prev.prev-page
# next css     #main > div > div.desc > a.lister-page-next.next-page
# p1 next      #main > div > div.desc > a



