import pandas as pd
import re
import nltk
from nltk.stem.snowball import SnowballStemmer

#English stemmer.
stemmer = SnowballStemmer("english")
lemmatizer = nltk.stem.WordNetLemmatizer()


class premodelling:

    def __init__(self):
         
        pass

    def tokenization(self, df: pd.DataFrame, col_name: "Text") -> pd.DataFrame:

        df[col_name] = df[col_name].str.split()

        return df


    #def delimit(self, df: pd.DataFrame, col_name: "Text") -> pd.DataFrame:

     #   df[col_name] = df[col_name].str.replace(","," ")

      #  return df

    def stemming(self, df: pd.DataFrame, col_name: "Text") -> pd.DataFrame:

        df[col_name] = df[col_name].apply(lambda x: [stemmer.stem(y) for y in x])

        return df


    def lemmatizing(self, df: pd.DataFrame, col_name: "Text") -> pd.DataFrame:

        df[col_name] = df[col_name].apply(lambda x: [lemmatizer.lemmatize(y) for y in x])

        return df
    
