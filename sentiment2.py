# importing the required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import spacy

nlp = spacy.load('en_core_web_sm')  # python3 -m spacy download en # spacy library for English language

# mydata = pd.read_csv('')
for dirname, _, filenames in os.walk('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

mydata = pd.read_csv('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/kaggle/input/imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv')
# mydata = mydata.sample(1000)
mydata['sentiment'].replace({'positive': 1, 'negative': 0}, inplace=True)

# taking sample  testing
# mydata = mydata.sample(1000)

print()
print('head of training data: \n')
print(mydata.head)

# check distribution of sentiments
print()
print('check distribution of sentiments')
print(mydata['sentiment'].value_counts())

# CHECK ALL NULL VALUES
print()
print('check all null values')
print(mydata.isnull().sum())

x = mydata['review']
y = mydata['sentiment']

# DATA CLEANING

print()
print('Started data cleaning process')
print('...')
print('removing stopwords, punctuation and applying lemmatization')

# CREATE A FUNCTION TO CLEAN THE DATA
import string
punct = string.punctuation
print('punct : \n', punct)
from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS) # list of stopwords

# creating a function for data cleaning

def text_data_cleaning(sentence):
    doc = nlp(sentence)
    tokens = []     # list of tokens
    for token in doc:
        if token.lemma_ != "-PRON-":
            temp = token.lemma_.lower().strip()
        else:
            temp = token.lower_
        tokens.append(temp)
    cleaned_tokens = []
    for token in tokens:
        if token not in stopwords and token not in punct:
            cleaned_tokens.append(token)
    return  cleaned_tokens

print()
print('removed stopwords, punctuation, converted to lowercase and lemmatized')

# TESTING THE FUNCTION ON SAMPLE DATA
print('Testing the data cleaning function with sample sentence/review :')
print(text_data_cleaning("Hello analysis, this is a good practice and it feels wonderful.!"))

# VECTORIZATION FEATURE ENGINEERING (TF-IDF)

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

tfidf = TfidfVectorizer(tokenizer=text_data_cleaning)    # (, decode_error='replace', encoding='utf=8')
# print(tfidf)
# exit()
# tfidf2 = TfidfVectorizer(tokenizer=text_data_cleaning, decode_error='replace', encoding='utf=8')
# xx = tfidf2.fit_transform(xdata[1].values.astype('U'))

classifier = LinearSVC()

# TRAIN THE MODEL

# splitting the dataset into Train and Test set

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print('train shape, test shape: \n', x_train.shape, x_test.shape)

print('\ntrain head\n', x_train.head())

# Fit the x_train and y_train

clf = Pipeline([('tfidf', tfidf), ('clf', classifier)])
# this will do vectorization and then it will do classification

clf.fit(x_train, y_train)
print('\nPipeline :\n', clf.fit(x_train, y_train))
# We don't need to prepare dataset for testing(x_test) for now

# PREDICT THE TEST SET RESULTS

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_pred = clf.predict(x_test)

# confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('\nConfusion Matrix : \n', cm)

# classification report
print("\n Classification Report : \n", classification_report(y_test, y_pred))
# check the accuracy here

acc = accuracy_score(y_test, y_pred)
print('\nAccuracy score : \n', (acc * 100), '%')

# r1 = clf.predict([35.45])
# print('\nReview1 sentiment : ', r1[0])
# exit()

# IMPORT THE SCRAPED IMDB REVIEWS INTO A PANDAS DATAFRAME

xdata = pd.read_csv('Avengers.csv', header=None)
elist = []
for i in range((xdata[1]).count()):
    # print(i, " ", xdata[1][i])
    elist.append(xdata[1][i])
# print(elist)

# xdata1 = xdata.dropna()
# xdata1[1] = label_encoder.fit_transform(xdata1[1])
# xdata = pd.read_csv('Avengers.csv', header=None)

# x = tfidf.fit_transform(xdata[1].values.astype('U'))
# xdata = xdata.dropna()
# print(xdata.isna().sum())

xlist = {'reviews': [], 'sentiment': []}
# CREATE A DATAFRAME TO APPEND THE REVIEWS AND SENTIMENT

# for i in range(len(xdata)):
#     if type(xdata[1][i]) == str:
#         pass
#     else:
#         xdata.drop(i)

for elem in elist:
    if type(elem) != str:
        pass
    else:
        revx = elem
        xlist['reviews'].append(revx)
        sent = clf.predict([revx])
        xlist['sentiment'].append(sent[0])
outdf = pd.DataFrame.from_dict(xlist)

print(outdf)
outdf.to_csv('outAvengersSentiment.csv')
# check distribution of sentiments
print()
print('check distribution of sentiments of outdata')
print(outdf['sentiment'].value_counts())

exit()

# i in range(1000):
#     # print(xdata[1][i], 1)
#     revx = xdata1[1][i]
#     xlist['reviews'].append(revx)
#     sent = clf.predict([revx])
#     xlist['sentiment'].append(sent[0])
# print(xlist)
# outdf.append(xlist)
# print(outdf)