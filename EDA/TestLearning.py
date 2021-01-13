import pandas as pd 
import re

#from EDA.preprocessing.preprocessing import remove_puntuation

data_full = pd.read_csv("Reviews.csv", index_col= 'Id')
data_new = data_full.head(100)

for i in data_new.columns:
    for j in data_new[i]:
        print(j)



#for i, j in data_new.iterrows():
#    print(j)

spec_chars = ["!",'"',"#","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","–"]
col_ind2 = data_new.columns.values

#for i in col_ind2:
    #for char in spec_chars:
        #print(i)
        
        #data_new[i] = data_new[i].str.replace(char, '')

#print(data_new)
