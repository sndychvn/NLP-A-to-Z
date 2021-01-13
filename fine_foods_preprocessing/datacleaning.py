import re
import pandas as pd

class cleaningprocess:

    def remove_null(self,df: pd.DataFrame) -> pd.DataFrame:

        df = df.dropna(subset={"UserId", "Summary", "Time", "Text"})

        return df


    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.drop_duplicates(subset={"UserId", "Summary", "Time", "Text"})

        return df

    def remove_rows(self, df: pd.DataFrame) -> pd.DataFrame:

        #df = df.drop('Row1', 'Row2', 'Row3', 'Row4')

        return df

    def remove_columns(self, df: pd.DataFrame) -> pd.DataFrame:

        #df = df[df.Row3! = 'Crayon']

        return df
    
    