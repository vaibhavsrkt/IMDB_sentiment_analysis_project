import numpy as np
import pandas as pd

import os

print()
print('importing the datasets.....')
for dirname, _, filenames in os.walk('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/kaggle/input/imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv')
# print(df.head())
# print(df['review'][0])

# CLEANING DATA
#     TEXT CLEANING
#     REMOVE HTML TAGS
#     REMOVE HTML CHARACTERS
#     CONVERTING TO LOWER
#     REMOVE STOP WORDS
#     STEMMING

print('took sample for testing.....')
df = df.sample(10000)
# print(df.shape)
# print(df.info)

df['sentiment'].replace({'positive': 1, 'negative': 0}, inplace=True)

# print(df.head())

# FOR TESTING REMOVAL OF HTML TAGS
import re

clean = re.compile('<.*?>')  # REMOVE THE HTML TAGS
re.sub(clean, '', df.iloc[2].review)

print('Started cleaning process....')

# F TO CLEAN HTML TAGS
def clean_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


df['review'] = df['review'].apply(clean_html)
print('removed html tags')


# CONVERTING TO LOWERCASE

def convert_lower(text):
    return text.lower()


df['review'] = df['review'].apply(convert_lower)
print('converted to lowercase')


# REMOVING SPECIAL CHARACTERS

def remove_special(text):
    x = ''
    for i in text:
        if i.isalnum():
            x = x + i
        else:
            x = x + ' '
    return x


# run on sample text
# print(remove_special('Thi*s i.s my sa@mpl#e review'))

df['review'] = df['review'].apply(remove_special)
print('removed special characters')

# REMOVE STOP WORDS
import nltk
from nltk.corpus import stopwords


def remove_stopwords(text):
    x = []
    for i in text.split():
        if i not in stopwords.words('english'):
            x.append(i)
    y = x[:]
    x.clear()
    return y


df['review'] = df['review'].apply(remove_stopwords)

print('removed stop words')
print()
print('The clean data is : ')
print(df)
print()

print('Started stemming process')
# stemming

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

y = []


def stem_words(text):
    for i in text:
        y.append(ps.stem(i))
    z = y[:]
    y.clear()
    return z


# TEST STEMMING FUNCTION
# print(stem_words(['I', 'played', 'playing', 'plays', 'player']))

df['review'] = df['review'].apply(stem_words)
print('stemming function applied')

# JOIN BACK FUNCTION TO GET THE COMBINED DF AFTER CLEANING

def join_back(list_input):
    return " ".join(list_input)


df['review'] = df['review'].apply(join_back)
print('joined back the clean data in the dataframe')
X = df.iloc[:,0:1].values
# X.shape

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1000)

X = cv.fit_transform(df['review']).toarray()
# print(X.shape)

y = df.iloc[:, -1].values

# SPLIT MY X,y DATA INTO TWO PARTS IE TEST AND TRAIN

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print()
print('splitted the data into train and test using sklearn.model_selection')
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

clf1 = GaussianNB()
clf2 = MultinomialNB()
clf3 = BernoulliNB()

clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)
clf3.fit(X_train, y_train)

y_pred1 = clf1.predict(X_test)
y_pred2 = clf2.predict(X_test)
y_pred3 = clf3.predict(X_test)

# y_test.shape
# y_pred1.shape

from sklearn.metrics import accuracy_score

print()
print('THE ACCURACY SCORES OF THE APPLIED MODELS ARE : ')
print('Gaussian', accuracy_score(y_test, y_pred1))
print('Multinomial', accuracy_score(y_test, y_pred2))
print('Bernoulli', accuracy_score(y_test, y_pred3))
print()

print(clf3.predict(['this was a really good movie']))
