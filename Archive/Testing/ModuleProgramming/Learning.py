import re
import pandas as pd 




def data_cleaning(data):
    
    print("data cleaning in process")
    data_cleaned = data.drop_duplicates(subset={"UserId", "Summary", "Time", "Text"})

    print("data is cleaned")
    return data_cleaned








if __name__ == "__main__":
    data_text = "My data is in the file"
    print(data_text)
    data = pd.read_csv("Reviews.csv", index_col= 'Id')
    cleaned_data = data_cleaning(data)
    print(cleaned_data.head())