### NLP Preprocessing: Credit goes to Shashank on Kaggle (https://www.kaggle.com/shashanksai/text-preprocessing-using-python)
### Data sample: Amazon Fine Food Reviews (https://www.kaggle.com/snap/amazon-fine-food-reviews)
### Problem at hand or the question to answer: Whether a review is positive or negative? 

import warnings
warnings.filterwarnings("ignore")                                   #Ignoring unnecessary warnings [https://docs.python.org/3/library/warnings.html]

import numpy as np                                                  #For large and multi-dimensional arrays

import pandas as pd                                                 #For data analysis and manipulations

import nltk                                                         #NLP Toolkit

#from nltk.corpus import stopwords                                  #Stopwords corpus to filterout
#nltk.download()
from nltk.stem import PorterStemmer                                 #Stemmer algorithm (https://tartarus.org/martin/PorterStemmer/)
from nltk.corpus import stopwords
#print(stopwords.words('english'))                                  #Test if you have the stopwords

from sklearn.feature_extraction.text import CountVectorizer         #To convert a collection of text to a matrix of teken counts (https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
from sklearn.feature_extraction.text import TfidfVectorizer         #To convert a collection of raw documents to a matrix of TF-IDF features. (https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)
from gensim.models import Word2Vec                                  #For Word2Vec https://radimrehurek.com/gensim/models/word2vec.html

import re                                                           #Regular expression operations (https://docs.python.org/3/library/re.html)

### Data import
#data_path = "C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv"
data = pd.read_csv(r"C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv")
data_sel = data.head(10000)                                         # Considering only the top 10000 rows


# Look at the shape of the data 
#print(data_sel.columns)                                             #Output: Index(['Id', 'ProductId', 'UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Score', 'Time', 'Summary', 'Text'], dtype='object')
#print(data_sel.head(10))                                            #Outputs the first 10 rows 

### Text Processing 

## Understanding the data

# Positive if score = 4 or 5, Negative if score = 1 or 2, Neutral if score = 3; therefore drop neutrals to determine positives or negatives
data_score_removed = data_sel[data_sel['Score']!=3]                 # Neutral reviews removed

# Converting Score values into class label, Positive or Negative

def partition(x):
    if x>3:
        return 'positive'
    return 'negative'

score_upd = data_score_removed['Score']
t = score_upd.map(partition)
data_score_removed['Score']=t

## Basic Cleaning 
# Deduplication: removing duplicates: It can be done by looking into unique values or to create a unique key, often based on the time. In this case, no user can make more than a review in a given time stamp. 
# The records that have equal UserId, ProfileName, Time, Text will be removed.

final_data = data_score_removed.drop_duplicates(subset={"UserId", "ProfileName", "Time", "Text"})

# By definition, HelpfullnessNumerator should be always less than or equal to HelpfullnessDenominator, therefore drop the ones that violate the definition

final = final_data[final_data['HelpfulnessNumerator'] <= final_data['HelpfulnessDenominator']]

final_X = final['Text']
final_y = final['Score']

#Stopwords removal and stemming (conversion into baseform)

stop = set(stopwords.words('english'))
#print(stop)                                                           #Prints all the stop words

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

    #words = [snow.stem(word) for word in sentence.split() if word not in stopwords.words('english')]
    words = [snow.stem(word) for word in sentence.split() if word not in stopwords.words('english')] #Stemming and removing stopwords
    temp.append(words)

final_X = temp
# print(final_X[1])

# 

sent = []
for row in final_X:
    sequ = ''
    for word in row:
        sequ = sequ + ' ' + word
    sent.append(sequ)

final_X = sent
#print(final_X[1])

### Techniques for encoding 
# BAG OF WORDS BoW
# BINARY BAG OF WORDS (https://www.kaggle.com/shashanksai/text-preprocessing-using-python)

count_vect = CountVectorizer(max_features=5000)                         #Telling that only consider the top 5000 most frequently repeated words
bow_data = count_vect.fit_transform(final_X)
#print(bow_data[1])

# BI-Gram BOW and NGram BOW techniques

final_B_X = final_X

count_vect = CountVectorizer(ngram_range=(1,2))
Bigram_data = count_vect.fit_transform(final_B_X)
#print(Bigram_data[1])

# TF-IDF Term Frequency - Inverse Document Frequency
final_tf = final_X
tf_idf = TfidfVectorizer(max_features=5000)
tf_data = tf_idf.fit_transform(final_tf)
#print(tf_data[1])

## Word2Vec - Average Word2Vec

w2v_data = final_X

splitted =  []
for row in w2v_data:
    splitted.append([word for word in row.split()])                     #Splitting words

train_w2v = Word2Vec(splitted,min_count=5,size=50, workers=4)         #min_count = 5 considers only if word repeats more than 5 times in entire data. size = 50 gives a vector length of size 50 and workers are cores to run this.

avg_data = []
for row in splitted:
    vec = np.zeros(50)
    count = 0
    for word in row: 
        try:
            vec += train_w2v[word]
            count += 1
        except:
            pass
    avg_data.append(vec/count)

#print(avg_data[1])

## TF-IDF WORD2VEC

tf_w_data = final_X
tf_idf = TfidfVectorizer(max_features=5000)
tf_idf_data = tf_idf.fit_transform(tf_w_data)

tf_w_data = []
tf_idf_data = tf_idf_data.toarray()
i = 0
for row in splitted:
    vec = [0 for i in range(50)]

    temp_tfidf = []
    for val in tf_idf_data[i]:
        if val !=0:
            temp_tfidf.append(val)

    count = 0
    tf_idf_sum = 0
    for word in row: 
        try:
            count += 1
            tf_idf_sum = tf_idf_sum + temp_tfidf[count-1]
            vec += (temp_tfidf[count-1] * train_w2v[word])
        except:
            pass
    vec = (float)/(1/tf_idf_sum) * vec
    tf_w_data.append(vec)
    i = i + 1

print(tf_w_data[1])