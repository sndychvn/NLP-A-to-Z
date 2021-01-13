import pandas as pd
import re

import nltk                                                     # Only used for tokenization
from nltk.corpus import wordnet                                 # Wrodnet used to find antonyms and synonyms 


def not2not_(df: pd.DataFrame, text_colname: str = 'Text') -> pd.DataFrame:
    ''' The not2not_ function replaces "not" with "not_", to use in the dictionary! 
        (Example: Not sad = Not_sad, not happy = not_happy)

        Arguments
        ---------
        dataframe: df, type= XYZ: the dataframe or the text to be evaluated by negation function
        text_colname: Text, str:
    '''
    regex_pat = re.compile(r'not ', re.IGNORECASE|re.UNICODE)       #Regular Expression's Pattern
    df['Text'] = df['Text'].str.replace(regex_pat, 'not_')         #Replace regex_pat with desired replacement
    #text_colname = text_colname.str.replace(regex_pat, 'not_')     #Replace regex_pat with desired replacement
    return df


def replace_sent(df: pd.DataFrame, text_colname: str = "Text") -> pd.DataFrame:
    ''' The negation function is used to replace negated words with "not" 
        with their antonyms, if any! (Example: Not sad = happy, Not Happy = Sad)

        Arguments
        ---------
        dataframe: df, type= XYZ: the dataframe or the text to be evaluated by negation function
        text_colname: Text, str:
    '''
    dct = {"not_sad": "happy", "not_happy": "sad"}                  #the dictionary should be replaced with NLTK wordnet

    pattern = re.compile(r'\b(' + '|'.join(dct.keys()) + r')\b')
    df['Text'] =  pattern.sub(lambda x: dct[x.group()], df['Text'])
    return df


if __name__ == "__main__":
    dfcsv = pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
    df = pd.DataFrame(data=dfcsv)  
    df['Text'] = df.Text.astype(str)
    print(df.dtypes)
    print(str(df.head(5)))
    #print("Shape of data=>",df.shape)
    # Select the top N number of rows in the dataframe
    df = df.head(1000)  
    #print("Shape of data=>",df.shape)
    #df["Text_neg"] = df["Text"].apply(replace_sent)
    #df["Text_neg"].to_csv('output_negatemodu.csv')
    df = df.apply(not2not_)
    df_neg = df.apply(replace_sent)
    df_neg.to_csv('output_df_negatemodu.csv')
    
#df["text_neg"] = df["text"].apply(replace_sent)
#print(df["text_neg"] )
#df["text_neg"] = df["text_neg"].replace({'not_': 'not '}, regex=True)
#print(df["text_neg"] )


"""
from nltk.corpus import wordnet
class AntonymReplacer(object):
  def replace(self, word, pos=None):
    antonyms = set()
    for syn in wordnet.synsets(word, pos=pos):
      for lemma in syn.lemmas:
        for antonym in lemma.antonyms():
          antonyms.add(antonym.name)
    if len(antonyms) == 1:
		return antonyms.pop()
	else:
		return None
"""