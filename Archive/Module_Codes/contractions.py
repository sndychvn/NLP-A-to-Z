### contractions.py expands the contractions in the text. Specially important to do it before applying the negation handling function. 


### Importing dependencies

import numpy as np
import pandas as pd

import pycontractions                                 # importing the pycontractions-2.0.1 package
from pycontractions import Contractions

import gensim.downloader as api

from tqdm import tqdm

### Prepare the dataset

# Importing dataset
df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
#print("Shape of data=>",df.shape)

x = df['Text'].head(1000)   

# The model accordingly for contractions function
model = api.load("glove-twitter-25")                 # https://awesomeopensource.com/project/RaRe-Technologies/gensim-data
# Importing the model for contractions
cont = Contractions(kv_model=model)
tqdm(cont.load_models())


# Function

def expand_contractions(x, ):
    ''' The negation function is used to ... .

        Arguments
        ---------
        x = the dataframe or the text to be evaluated by negation function

    '''
    """expand shortened words, e.g. don't to do not"""
    x = list(tqdm(cont.expand_texts([x], precise=True),  desc='Loading'))[0]
    return x
    


# Apply the function to the data and write it back into the file
x = x.apply(expand_contractions)
x.to_csv('output_contractions.csv')