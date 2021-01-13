# html removing functions: these functions remove HTML tags using different packages.


import os
import re
import html as ihtml

import pandas as pd
from bs4 import BeautifulSoup

 
# Importing data_sample and convert it to dataframee
df=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv", index_col ="Id") 
#print("Shape of data=>",df.shape)

#data_sel = df.head(10)                                           # Considering only the top 10000 rows
#print(data_sel)

#check_row = df.loc["delmartian"]                                      # Check the individual rows of the dataframe
#chech_cell = df.loc[[10],['Text']].head()                             # Check the individual cells of the dataframe


# Function to remove_htmltags

def remove_htmltag(dataframe = 'df',):
    ''' The remove_htmltag function is used to remove all the html tags in the text, if any.


      Parameters
        ----------
        dataframe: takes the value of the dataframe, if not given, it will take the default value of df. 

    '''
    global df
    df = BeautifulSoup(ihtml.unescape(df), features="html.parser").df
    df = re.sub(r"http[s]?://\S+", "", df)
    df = re.sub(r"\s+", " ", df)
    return df


'''
### Applying the remove_htmltag() function to only one column in the dataframe

modDf = df.apply(lambda x: remove_htmltag(x) if x.name == 'Text' else x, axis=1)
print("Modified Dataframe : Removed HTML tags in the values in column 'Text'", modDf, sep='\n')
'''

'''
### Testing with short sample text
# sample_text = '<p>One way to talk about it is, physical therapists (PTs) work on gross motor issues and occupational therapists (OTs) work with fine motor issues.\n"Gross motor" refers to large body movements such as running, walking, crawling.  "Fine motor" refers usually to the refined movements of our hands.  OTs work with such skills as writing, cooking, dressing, bathing, toileting, feeding, the basics of independence.</p>\n<p>Both OTs and PTs work with people with many and multiple different health problems in such environments as private practice, hospitals, rehabilitation centers, schools, home care, and many others.  In rehabilitation environments, OTs and PTs often work separately with the same person but on different activities.</p>\n<p>OTs receive more training working with people with cognitive (thinking) problems.  Both OTs and PTs work with people who have cognitive issues such as traumatic brain injury, emotional issues, developmental delays - children who learn slowly and differently than the average child.</p>\n<p>Both OTs and PTs do very similar work with infants.  After that they do different but complementary work with people of all ages.</p>\n<p>Here are some generalizations.  Say someone has had a stroke, the PT would work on helping that person relearn to  roll over, sit up, stand up and sit down, walk, reach to pick up something, learn to use a walker, or cane.  The OT would help that person relearn how pick up a fork and bring food to the mouth, and make a splint to keep the hand that doesn\'t move from getting tight and curled up.  </p>\n<p>A weekend athlete would go to a PT for help with a knee or ankle, or shoulder injury.  A person who broke his/her wrist and fingers would go to an OT or to an OT or PT who had a specialty in hand rehabilitation.</p>\n<p>I hope that is helpful.  You can always go to &lt;apta.org&gt; website for the American Physical Therapy Association, to read more about physical therapy and &lt;aota.org&gt; American Occupational Therapy Association website, to read more about occupational therapy.  There are many large differences between the two professions, but there are also some similarities.  This makes your question an important one.</p>'
sample_text = 'This is an html test for myself http://www.ted.com/talks/julie_lythcott_haims_how_to_raise_successful_kids_without_over_parenting?utm_campaign=social&utm_medium=referral&utm_source=facebook.com&utm_content=talk&utm_term=education .'
print(sample_text)


def remove_htmltag(text):
    text = BeautifulSoup(ihtml.unescape(text), features="html.parser").text
    text = re.sub(r"http[s]?://\S+", "", text)
    text = re.sub(r"\s+", " ", text)    
    return text

rmvdtxt = remove_htmltag(sample_text)
print(rmvdtxt)
'''