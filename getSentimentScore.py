import pandas as pd
import os

directory = os.fsencode('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/outsentiments/')

outSentScoreDict = {'movie': [], 'sentiment score': []}

for file in os.listdir(directory):
    filenamecsv = os.fsdecode(file)
    filename = filenamecsv.replace('.csv', '')
    sentimentdf = pd.read_csv(os.path.join('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/outsentiments/', filenamecsv))
    sentDist = sentimentdf['sentiment'].value_counts()
    pos = sentDist[1]
    neg = sentDist[0]
    sentScore = (pos/(pos+neg)) * 100
    outSentScoreDict['movie'].append(filename)
    outSentScoreDict['sentiment score'].append(sentScore)
sentScoredf = pd.DataFrame.from_dict(outSentScoreDict)
sentScoredf.to_csv(os.path.join('/home/sunbeam/Documents/forproject/IMDB_SENTIMENT/sentscore/', 'SentimentScoreDistribution.csv'))
