#IMPORT THE REQUIRED LIBRARIES
import os
import pandas as pd
directory = os.fsencode('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/inreviews/')

for file in os.listdir(directory):
    filenamecsv = os.fsdecode(file)
    filename = filenamecsv.replace('.csv', '')
    print('filename :', filename)
    df = pd.read_csv(os.path.join('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/inreviews/', filenamecsv))


exit()
import pandas as pd
df = pd.read_csv('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/inreviews/12 Angry Men.csv')
df.rename(columns={'Unnamed: 0': 'sr', '0': 'rev'}, inplace=True)
print(df['rev'][1])
# print(df2)
from selenium import webdriver
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

PATH = "/home/sunbeam/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

toptho = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
driver.get(toptho)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')




import pandas as pd

xdata = pd.read_csv('Avengers.csv', header=None)
xlist = []
for i in range(1000):
    # print(i, " ", xdata[1][i])
    xlist.append(xdata[1][i])

for elem in xlist:
    if type(elem) != str:
        print(type(elem))
exit()
xdata1 = xdata.dropna()
# print(xdata1)
xlist = []
for i in range(1000):
    print(i, " ", xdata1[1][i])
#     xlist.append(rev)
# print(xlist)
exit()

print('sum of na : \n', xdata.isna().sum())
# print(xdata)

for i in range(50):
    print(xdata[1][i])

data2 = pd.read_csv(
    '/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/kaggle/input/imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv')
for i in range(len(data)):
    print(data[1][i])
# for i in range(len(data)):
#     if type(data[1][i]) == str:
#         pass
#     else:
#         data.drop(i)
# print(data)
# xlist = {'reviews': [], 'sentiment': []}
# for i in range(11):
#     xlist['reviews'].append(i)
#     xlist['sentiment'].append(i)
# print(xlist)
# print(i)
# while type(data[1][i].str):
#     xlist['reviews'].append(data[1][i])
#     xlist['sentiment'].append(1)
# print(xlist)

# while type(data[1][i]) == str:
#     print(type(data[1][i]))
# print(type(data[1][1]))
# print(type('random text'))
# df1 = pd.DataFrame()
# xlist = {'reviews':[], 'sentiment':[]}
# for i in range(11):
#     xlist['reviews']


#
# from textblob import TextBlob
# import string
# def remove_num_punct(aText):
#     p = string.punctuation
#     d = string.digits
#     j = p + d
#     table = str.maketrans(j, len(j)* ' ')
#     return aText.translate(table)
#
# i = 0
# aList = []
# for txt in xdata[1].isnull():
#     if txt:
#         aList.append(np.nan)
#     else:
#         b = remove_num_punct(xdata[1][i])
#         pol = TextBlob(b).sentiment.polarity
#         aList.append(pol)
#     i+=1
# print(aList)
# exit()
