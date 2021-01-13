import pandas as pd
import re

import nltk                                                 # Only used for tokenization
from nltk.corpus import wordnet                             # Wrodnet used to find antonyms and synonyms 

d = {"number" : [0, 1, 2, 3],
"text" : ["I'm not happy", "I am not sad", "Not in my name", "Not for sale"]}
print("The data is: " + '\n' + str(d))                      #Print out the data (list)

df = pd.DataFrame.from_dict(data=d)                     

print("The dataframe is:" + '\n' + str(df.head()))          #Print out the dataframe 

regex_pat = re.compile(r'not ', re.IGNORECASE|re.UNICODE)   #Regular Expression's Pattern
df["text"] = df["text"].str.replace(regex_pat, 'not_')      #Replace regex_pat with desired replacement


def replace_sent(text):
    dct = {"not_sad": "happy", "not_happy": "sad"}          #the dictionary should be replaced with NLTK wordnet

    pattern = re.compile(r'\b(' + '|'.join(dct.keys()) + r')\b')
    text = pattern.sub(lambda x: dct[x.group()], text)
    return text

df["text_neg"] = df["text"].apply(replace_sent)
print(df["text_neg"] )
df["text_neg"] = df["text_neg"].replace({'not_': 'not '}, regex=True)
print(df["text_neg"] )