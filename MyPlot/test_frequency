import pandas as pd
import nltk
import re
from nltk.probability import FreqDist
from nltk.corpus import brown
from nltk.stem.snowball import SnowballStemmer
import numpy as np

# Use English stemmer.
stemmer = SnowballStemmer("english")
lemmatizer = nltk.stem.WordNetLemmatizer()


class Frequency:

    def cleanfreq(self, df, col_name = "Text"):

        data_score_removed = df[df['Score'] != 3]
        data_score_removed[col_name] = data_score_removed[col_name].str.split()
        lists =  data_score_removed[col_name]
        words = []
        for wordList in lists:
            #for words9 in wordList:
            words += wordList
        
        #temp_word = words.sort()
        #print(sorted(words))    
        return words

    def plotfredist(self, df, number):

        #data_score_removed = df[df['Score'] != 3]
        #lists =  data_score_removed['Text']
        #words = []
        #for wordList in lists:
        #    words += wordList
        
        words = self.cleanfreq(df)
        fdist = FreqDist(words) #recheck the code to remove the punctuations
        plot_fig = fdist.plot(number)

        #ConditionalFreqDist((len(word), word) for word in word_tokenize(words))
        
        #mostcommon50_all = fdist.most_common(50)
        #print("The most common 50 words are:" + ' ' + str(mostcommon50_all))

        return plot_fig

    def sentimentfreq(self, df, number):

        df['Sentiment'] = np.where((df['Score'] < 3 ), 'Positive', 'Negative')

        #df['Sentiment'] = ['Positive' if x >= 2 else 'Negative' for x in df['Score']]
        
        words = self.cleanfreq(df)

        fdist = FreqDist(words)
        plot_fig = fdist.plot(number)

        return plot_fig


    def sentimentfreqpos(self, df, number):

        df_temp = df[df['Sentiment'] == 'Positive'] 
        
        words = self.cleanfreq(df_temp)

        fdist = FreqDist(words)
        plot_fig = fdist.plot(number)

        return plot_fig

    
    def sentimentfreqneg(self, df, number):

        df_temp = df[df['Sentiment'] == 'Negative'] 

        words = self.cleanfreq(df_temp)

        fdist = FreqDist(words)
        plot_fig = fdist.plot(number)    

        return plot_fig   
