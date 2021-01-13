# The purpose of this piece of code is to examine the frequency of the stop words in the reviews from the Amazon Food Services 

### Importing dependencies

import numpy as np
import pandas as pd

import nltk                                                         #NLP Toolkit
from nltk import *
import re

from sklearn.feature_extraction.text import CountVectorizer   

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#import tqdm as tqdm
#import gensim
#from tqdm import tqdm_notebook as tqdm


#data = pd.read_csv("/home/amir/amazon_fine_foods-5/fine_foods_eda/dataset1/Reviews.csv") 
#data = pd.read_csv("/home/NLP_admin/amazon_fine_foods/dataset1/Reviews.csv", index_col ="Id")
data=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 


#df = pd.DataFrame(data) 
data_sel = data.head(1000)                                          # 568454 Considering only the top 10000 rows
#print(data_sel.columns)

# Remobing neutral views (Score = 3)

data_score_removed = data_sel[data_sel['Score']!=3] 

# Classifying to positive and negative

def partition(x):
    if x < 3:
        return 'positive'
    return 'negative'

score_upd = data_score_removed['Score']
t = score_upd.map(partition)
data_score_removed['Score']=t

# Removing duplicates

final_data = data_score_removed.drop_duplicates(subset={"UserId", "ProfileName", "Time", "Text"})

# HelpfulnessNumerator should always be less than or equal to HelpfulnessDenominator

final = final_data[final_data['HelpfulnessNumerator'] <= final_data['HelpfulnessDenominator']]

final_X = final['Text']
sentiment = final['Score']
#print(final['Score'].value_counts())


## Convert to lower case, removing HTML tags, and removing punctuations 
# Dependencies: Importing package re

temp =[]
snow = nltk.stem.SnowballStemmer('english')
for sentence in final_X:
    sentence = sentence.lower()                                         #Converting to lower case
    cleanr = re.compile('<.*?>')
    sentence = re.sub(cleanr, ' ', sentence)                            #Removing HTML tags
    sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    sentence = re.sub(r'[.|,|)|(|\|/]',r' ',sentence)                   #Removing punctuations

    words = [word for word in sentence.split()]
    temp.append(words)

final_X = temp
#print(final_X[2])

sent = []
for row in final_X:
    sequ = ''
    for word in row:
        sequ = sequ + ' ' + word
    sent.append(sequ)

final_X = sent
#print(final_X[2])
#print(final_X[2].index('the'))

# Tokenize words 

corpus = ' '.join(final_X)
#print(corpus)

tokens = re.findall(r'\w+', corpus)
#print(tokens)

### All words

text_size = len(tokens)    
print(text_size)                         # Number of words
vocab_size = len(set(tokens))    
print(vocab_size)                        # Number of vocabs

freqDist_all = FreqDist(tokens)
print("The frequency of words are:" + ' ' + str(freqDist_all))

plottingdist = freqDist_all.plot(50)
print(plottingdist)


# Most common 50 words
mostcommon50_all = freqDist_all.most_common(50)
print("The most common 50 words are:" + ' ' + str(mostcommon50_all))

words = freqDist_all.keys()             # produces a list of all the words in the text
print("The words in the text are:" + ' ' + str(type(words)))
print("The number of words in the text is:" + ' ' + str(len(words)))

# The nost common word with a meaning is chips in the first 1000 reviews
print("The frequency of word 'chips' is:" + ' ' + str(freqDist_all["chips"]) + ' ' + 'times')

## Sentiment Frequency





### Only stopwords




### No stopwords





'''
############################

def freq_df(df_value, n_gram=1, n=50, stopwords=[], verbose=True):
    """Create a data frame of frequent word

    Args:
        df_value (pd.Series): Separated by space values
        stopwords (list): A list of words to specify for the stopword
        n_gram (int): N number of N grams
        n (int): How many words should be output
        verbose (bool): Whether or not to output the log by tqdm

    Returns:
            list: List of RGB

    """

    def generate_ngrams(text, n_gram=1):
        """Function to create a list of n-grams"""
        token = [token for token in text.lower().split(" ")
                 if token != "" if token not in stopwords]
        ngrams = zip(*[token[i:] for i in range(n_gram)])
        return [" ".join(ngram) for ngram in ngrams]

    freq_dict = defaultdict(int)
    if verbose:
        for sent in tqdm(df_value):
            for word in generate_ngrams(str(sent), n_gram=n_gram):
                freq_dict[word] += 1
    else:
        for sent in df_value:
            for word in generate_ngrams(str(sent), n_gram=n_gram):
                freq_dict[word] += 1

    fd_sorted = pd.DataFrame(sorted(freq_dict.items(),
                             key=lambda x: x[1])[::-1])
    fd_sorted.columns = ['word', 'word_count']
    return fd_sorted.head(n)

#################################
'''
