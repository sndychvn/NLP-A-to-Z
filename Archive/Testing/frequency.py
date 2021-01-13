import numpy as np
import pandas as pd
import re


data = pd.read_csv('/home/NLP_admin/amazon_fine_foods/dataset1/Reviews.csv', index_col ="Id")


data_part = data.head(1000)
data_pp = data_part.drop_duplicates(subset={"UserId", "ProfileName", "Time", "Text"})

n = 1000

for i in 0 , n:
    for sentence in data_pp:
        sentence = sentence.lower()
        cleanr = re.compile('<.*?>')
        sentence = re.sub(cleanr, ' ', sentence)
        sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
        sentence = re.sub(r'[.|,|)|(|\|/]',r' ',sentence)
        #print(sentence)





#print(data_part.count())
#print(data_pp.count())
print(data_pp.iloc[[1]])