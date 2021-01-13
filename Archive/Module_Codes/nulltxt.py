# nulltxt function: it shows the number of null values and to drop the null values, if any!

import numpy as np
import pandas as pd

# Prepare the dataset

# Importing dataset
df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 
#print("Shape of data=>",df.shape)


# Function shownulltxt

def shownulltxt(dataframe = 'df', ):
    ''' The shownulltxt function is used to show the number of null values in the dataframe, if any.


      Parameters
        ----------
        dataframe: takes the value of the dataframe, if not given, it will take the default value of df. 

    '''
    return df.isnull().sum()


#print(df.isnull().sum())


# Function dropnulltxt

def dropnulltxt(dataframe = 'df', ):
    ''' The dropnulltxt function is used to drop the null values in the dataframe, if any.

      Parameters
        ----------
        dataframe: takes the value of the dataframe, if not given, it will take the default value of df. 


    '''
    return df.dropna(inplace=True)


#print(df.dropna().isnull().sum())

