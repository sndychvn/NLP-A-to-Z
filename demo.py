import pandas as pd 
from preprocessing import Preprocessing as ppc
#import stpwrdsdic



if __name__ == "__main__":
    demo_prep = ppc()
    
    data_complete = pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv", index_col= 'Id')
    data_trim = data_complete.head(100) 
    #result = demo_prep.remove_stopwords(data_trim)
    #demo_prep.remove_stopwords(data_trim)
    print(data_trim.head(100))
    


    #demo_prep.remove_stopwords(data_trim)
    #print("Stopwords removed:" + " " + str(data_trim.head(100)))
    
    #df_casesen_removed = demo_prep.remove_casesensitive(data_trim)
    #print("Converted to lower case:" + " " + str(df_casesen_removed.head(100)))

    #df_expanded_contractions = demo_prep.expand_contractions(data_trim)
    #print("Contractions expanded:" + " " + str(df_expanded_contractions.head(100)))

    #df_spellcheck = demo_prep.spell_check(data_trim)
    #print("Spell ckecking:" + "\n" + " " + str(df_spellcheck.head(100)))

    df_remove_negation = demo_prep.remove_negation(data_trim)
    print("Negations eliminated:" + "\n" + " " + str(df_remove_negation.head(100)))
