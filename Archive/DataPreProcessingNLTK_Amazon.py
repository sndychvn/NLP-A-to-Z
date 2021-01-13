### In this document the NLTK package and its capabilities are explored


### NLTK Chapter 1

### Import the dependencies 

import nltk
#nltk.download()
from nltk.book import *

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                                                 #For data analysis and manipulations



# Importing Amazon Food Review data 
data = pd.read_csv(r"/home/amir/amazon_fine_foods-5/fine_foods_eda/dataset1/Reviews.csv")
df = pd.DataFrame(data) 
data_sel = df.head(10000)                                         # Considering only the top 10000 rows
#print(data_sel['Text'])

#3.1 Frequency distribution 
fdist1 = FreqDist(data_sel['Text'])                               # Compute the distribution of the sentences in the Text column (For the words, you need to tokenize them and add them to a set)
#print(fdist1)
#most_common10 = fdist1.most_common(10)                             #Print out the most common 50 text sentences 
#print(most_common10)


txtlen = len = len(data_sel['Text'])                    # Gives the length of text3
print(txtlen)

#txt3srtdtkns = sorted(set(text3))       #sorted list of vocabulary items (distinct tokens)
#print(txt3srtdtkns)

#txt3lentkns = len(set(text3))           #number of distinct tokens (no repetitions) or the word types: A word type is the form or spelling of the word independently of its specific occurrences in a text — that is, the word considered as a unique item of vocabulary.
#print(txt3lentkns)


