import re
import pandas as pd 


class example:

    def data_cleaning(self, data):
        
        print("data cleaning in process")
        data_cleaned = data.drop_duplicates(subset={"UserId", "Summary", "Time", "Text"})

        print("data is cleaned")
        return data_cleaned




    def remove_example(self, df: pd.DataFrame) -> pd.DataFrame:
        spec_chars = ["!",'"',"#","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","–"]
        #col_ind = df.columns.values
        for col in (df.columns.values):
        #for row in range(0, len(data_new)):
            for char in spec_chars:
                df[col] = df[col].astype(str).str.replace(char, '')
        #for i in col_ind:
         #   for char in spec_chars:
          #      df[i] = df[i].str.replace(char, '')
        #df["Summary"] = df.apply(lambda x: x['Summary']+100, axis=1)
        #for i, j in data.iterrows():
        return df



if __name__ == "__main__":
    data_text = "My data is in the file"
    print(data_text)
    data_full9 = pd.read_csv("Reviews.csv", index_col= 'Id')
    data = data_full9.head(100)
    col_name = data.columns.values
    data1 = example()    
    
    #datax = data1.remove_example(data)
    #print(datax.head())
    #cleaned_data = data_cleaning(data)
    #print(cleaned_data.head())
    #print(col_name)
    print(data_full9.head(4))