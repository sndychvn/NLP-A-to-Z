import nltk                                         # Only used for tokenization
from nltk.corpus import wordnet                     # Wrodnet used to find antonyms and synonyms 

import numpy as np
import pandas as pd

import tqdm as tqdm

def negation(df: pd.DataFrame, text_colname: str = "Text") -> pd.DataFrame:
    ''' The negation function is used to replace negated words with "not" 
    with their antonyms, if any! (Example: Not sad = happy, Not Happy = Sad)

        Arguments
        ---------
        dataframe: df, type= XYZ : the dataframe or the text to be evaluated by negation function

    '''
    regex_pat = re.compile(r'not ', flags=re.IGNORECASE)
        .str.replace(regex_pat, 'not_')
        
    text = ''.join(df[text_colname].values)
    words = nltk.word_tokenize(text)

    new_words = []

    temp_word = ''
    for word in tqdm(words):
        antonyms = []
        if word == 'not':
            temp_word = 'not_' 
        elif temp_word == 'not_':
            for syn in wordnet.synsets(word):
                for s in syn.lemmas():
                    for a in s.antonyms():
                        antonyms.append(a.name())
            if len(antonyms) >= 1:
                word = antonyms[0]
            else:
                word = temp_word + word # when antonym is not found, it will remain not_happy
                                    
            temp_word = ''
        if word != 'not':
            new_words.append(word)

    df = ' '.join(new_words)
    return df

df1 = df.apply(negation)
df1.to_csv('output_negation.csv')


if __name__ == "__main__":

    # Prepare the dataset
    # Importing dataframe as input
    df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
    # print("Shape of data=>",df.shape)
    # Input data as a column
    df = df['Text']

###################################
###################################
#"""
d = {"number" : [0, 1, 2, 3],
"text" : ["I'm not happy", "I am not sad", "Not in my name", "Not for sale"]}

df = pd.DataFrame.from_dict(data=d)

df.head()

regex_pat = re.compile(r'not ', re.IGNORECASE|re.UNICODE)
df["text"] = df["text"].str.replace(regex_pat, 'not_')

def replace_sent(text):
l = {"not_sad": "happy", "not_happy": "sad"}

 pattern = re.compile(r'\b(' + '|'.join(l.keys()) + r')\b')
text = pattern.sub(lambda x: l[x.group()], text)
return text

df["text_neg"] = df["text"].apply(replace_sent)
df["text_neg"] = df["text_neg"].replace({'not_': 'not '}, regex=True)