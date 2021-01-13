import pandas as pd
import re

import nltk                                                     # Only used for tokenization
from nltk.corpus import wordnet                                 # Wrodnet used to find antonyms and synonyms 

df = pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv", skipinitialspace=True, dtype={"Text": str}, index_col="Id")
df = df.head(100) 
df = df["Text"]
print(df)
#print().head(10)

#def not2not_(df: pd.DataFrame, text_colname: object = 'Text') -> pd.DataFrame:
def not2not_(df): #-> pd.DataFrame:
    ''' The not2not_ function replaces "not" with "not_", to use in the dictionary! 
        (Example: Not sad = Not_sad, not happy = not_happy)

        Arguments
        ---------
        dataframe: df, type= DataFrame: the dataframe or the text to be evaluated by negation function
        text_colname: Text, str:
    '''
    regex_pat = re.compile(r'not ', re.IGNORECASE|re.UNICODE)   #Regular Expression's Pattern
    print(type(regex_pat))
    #print(regex_pat)
    #df = df.set_index("Text")
    #df = df.set_index(['Text', 'Id'])  # Move 1 columns into the index.
    #df["Text"] = df["Text"].replace(regex_pat, "Not_")          #Replace regex_pat with desired replacement
    df['Text'] = regex_pat.sub(lambda x: "Not_", df['Text'])
    #df = df.reset_index()
    return df

df_not_ = df.apply(not2not_)
df_not_.to_csv('output_df_not2not_.csv')

