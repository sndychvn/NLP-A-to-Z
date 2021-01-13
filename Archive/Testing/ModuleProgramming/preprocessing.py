# Importing dependencies

import numpy as np
import pandas as pd 
import re
import contractions
from autocorrect import Speller


# internally developed dependencies
from stpwrdsdic import stpwrdsdictionary


class Preprocessing():
    """
            blueprint for preprocessing
    """
    
    def __init__(self):
        # print ("preprocessing instance created!")
        # preprocessin = Preprocessing()
        
        pass

    def remove_puntuation(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame: 
        """ The remove_puntuation method eliminates the punctuations in the text.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """   
        #spec_chars = ["!",'"',"#","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","–"]
        regex_punc = re.compile(r'[^A-Za-z0-9 ]+', re.IGNORECASE|re.UNICODE)       #Regular Expression's Pattern
        df[col_name] = df[col_name].str.replace(regex_punc, '')

        return df


    def remove_casesensitive(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_casesensitive method makes every string to lowercase.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """
        df.loc[:, col_name] = df.loc[:, col_name].str.lower()             # Explore other possibilities replace re

        return df


    def remove_stopwords(self, df: pd.DataFrame, col_name = "Text", stopwordsdic = "stpwrds_nltk_en") -> pd.DataFrame: #try also use of **kwargs to insert the dictionary of stopwords
        """ The remove_stopwords method elimintates the stopwords with some flexibility on removal of negative words.
        The negative words can be filtered alltogether with the other stopwords, the stopwords can be eliminate without 
        the negative words, and finally the negative words can be eliminated keeping the other stopwords. The stopwordsdic
        argument has the following instances, saved in a dictionary in module ""stpwrdsdic.py.

        Arguments  
        ---------  
        df: the dataframe or the text to be evaluated by negation function. \n
        col_name: the name of column with the string for operation. \n
        stpwrdsdic: Choose your stopwords from a variery of stopwords sets w/wo the negative words included in them from
        NLTK, Gensim, Spacy, and all three combined: \n
        stpwrds_nltk_en; \n
        stpwrds_nltk_en_neg; \n
        stpwrds_nltk_en_noneg; \n                                                                      
        stpwrds_gensim_en; \n
        stpwrds_gensim_en_neg; \n
        stpwrds_gensim_en_noneg; \n
        stpwrds_spacy_en; \n
        stpwrds_spacy_en_neg; \n
        stpwrds_spacy_en_noneg; \n
        stpwrds_combined_en; \n
        stpwrds_combined_en_neg; \n
        stpwrds_combined_en_noneg; \n
        """
        df[col_name] = df[col_name].apply(lambda x: [item for item in x.split() if item not in stpwrdsdictionary[stopwordsdic]])
        
        return df   
    
    
    def remove_digits(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_digits method eliminates the digits in the text.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """   
        regex_digits = re.compile(r'[^A-Za-z ]+', re.IGNORECASE|re.UNICODE)       #Regular Expression's Pattern
        df[col_name] = df[col_name].str.replace(regex_digits, '')

        return df


    def remove_htmltags(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_htmltags method eliminates the html tags in the text.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """         
        clean_htmltags = re.compile('<.*?>')
        df[col_name] = df[col_name].str.replace(clean_htmltags, '')

        return df


    def remove_negation(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_negation method eliminates the words combined with "not" in the text by replacing them with their synonyms, for instance "not good" is converted to "bad".

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """
        # The methods works fine, the dictionary will be replaced with the NLTK wordnet dictionary           
        dct = {"not_good": "bad", "not_happy": "sad"}
        regex_pat = re.compile(r'not ', re.IGNORECASE|re.UNICODE)       #Regular Expression's Pattern
        df[col_name] = df[col_name].str.replace(regex_pat, 'not_')
        regex_pat_replace = re.compile(r'\b(' + '|'.join(dct.keys()) + r')\b')
        df[col_name] = [regex_pat_replace.sub(lambda x: dct[x.group()], i) for i in  df[col_name]]
                
        return df


    def remove_abbreviations(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_abbreviations method eliminates the abbreviations in the text and replaces them with expanded words.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """    
        
        return df


    def expand_contractions(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The remove_contractions method eliminates the contractions in the text and replaces them with expanded words.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """
        # Load your favorite semantic vector model in gensim keyedvectors format from disk 
        # or specify any model from the gensim.downloader api https://awesomeopensource.com/project/RaRe-Technologies/gensim-data
        df[col_name] = df[col_name].apply(lambda x: [contractions.fix(word) for word in x.split()])
        
        return df


    def spell_check(self, df: pd.DataFrame, col_name = "Text") -> pd.DataFrame:
        """ The spell_check method corrects wrongly spelled or typed words.

        Arguments  
        ---------  
        df: the dataframe or the text. \n
        col_name: the name of column with the string. \n
        
        """
        spell = Speller(lang='en')
        df[col_name] = [' '.join([spell(i) for i in x.split()]) for x in df[col_name]]
        
        return df