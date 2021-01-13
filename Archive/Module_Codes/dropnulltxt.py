# Function to drop the null values, if any!

import numpy as np
import pandas as pd

# Prepare the dataset

# Importing dataset
df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
#print("Shape of data=>",df.shape)


# Function

def dropnulltxt(dataframe = 'df', ):
    ''' The dropnulltxt function is used to drop the null values in the text, if any.
       

      Parameters
        ----------
        dataframe: takes the value of the dataframe, if not given, it will take the default value of df. 

    '''
    return df.isnull().sum()

