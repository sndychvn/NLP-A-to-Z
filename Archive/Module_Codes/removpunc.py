# removpunc function: it removes the punctuations in the text, if any!

import numpy as np
import pandas as pd
import re                                                           #Regular expression operations (https://docs.python.org/3/library/re.html)


# Prepare the dataset

# Importing dataset
df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
#print("Shape of data=>",df.shape)

x = df['Text'].head(1000)    


# Function rempunc

def removpunc(x):
    ''' The rempunc function is used to remove punctuations in the dataframe, if any.

      Parameters
        ----------
        dataframe: takes the value of the dataframe, if not given, it will take the default value of df. 


    '''
    return re.sub(r'[.|,|)|(|\|/]',r' ',x)


x = x.apply(removpunc)
x.to_csv('output_removpunc.csv')

#print(data_sel)
