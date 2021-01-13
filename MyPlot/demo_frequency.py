import pandas as pd
from frequency import Frequency as frq




if __name__ == "__main__":
    demo_frq = frq()

    
    #data = pd.read_csv("/home/amir/amazon_fine_foods-5/fine_foods_eda/dataset1/Reviews.csv") 
    #data = pd.read_csv("/home/NLP_admin/amazon_fine_foods/dataset1/Reviews.csv", index_col ="Id")
    data=pd.read_csv("C:\\Users\\amikheir\\OneDrive - Crayon Group\\Projects\\NLP Project\\Data\\Reviews.csv") 


    #df = pd.DataFrame(data) 
    data_sel = data.head(1000)                                          # 568454 Considering only the top 10000 rows
    #print(data_sel.columns)

    # Remobing neutral views (Score = 3)

    data_score_removed = data_sel[data_sel['Score']!=3] 

    # Classifying to positive and negative

    def partition(x):
        if x < 3:
            return 'positive'
        return 'negative'

    score_upd = data_score_removed['Score']
    t = score_upd.map(partition)
    data_score_removed['Score']=t

    # Removing duplicates

    final_data = data_score_removed.drop_duplicates(subset={"UserId", "ProfileName", "Time", "Text"})

    # HelpfulnessNumerator should always be less than or equal to HelpfulnessDenominator

    final = final_data[final_data['HelpfulnessNumerator'] <= final_data['HelpfulnessDenominator']]

    final_X = final['Text']
    sentiment = final['Score']
    #print(final['Score'].value_counts())