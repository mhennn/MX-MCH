import pandas as pd
import string
from utils.initiated import INITIATED

DIGITS = string.digits

class ReadData:
    def __init__(self):
        pass

    def read_file(self, data):
        df = pd.read_excel(data, sheet_name=None)
        combined_df = pd.concat(df.values(), ignore_index=True)
        return combined_df['Data'].tolist()
    
    def store_data_type(self, data_type):
        return [
            ["int" if char in DIGITS else type(char).__name__ for char in str(item)]
            for item in data_type
        ]
    
    def get_user_pattern(self, pttrn):
        user_pattern = ["int" if pattern in DIGITS else type(pattern).__name__ for pattern in pttrn]
        return user_pattern
    
    def compare_match_type(self, user_data, file_pattern):
        user_pattern = self.get_user_pattern(user_data)
        file_data = self.read_file(file_pattern)
        data_pattern = self.store_data_type(self.read_file(file_pattern))

        for idx, ptrn in enumerate(data_pattern):
            if ptrn == user_pattern:
                print(f"\nData match type with {user_data} with {file_data[idx]}")
                print(f"Match type are {user_pattern}")
            else:
                print(f"\n{file_data[idx]} not match with {user_data}")