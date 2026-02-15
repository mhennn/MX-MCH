import pandas as pd
from utils.logo import logo
from utils.initiated import INITIATED
import string

print(logo)

DIGITS = string.digits

user_input = input("Input text you want to pattern analyze: ")
user_path = input("Input the file you want to compare: ")

print(INITIATED)

def get_user_pattern(pttrn):
    user_pattern = ["int" if pattern in DIGITS else type(pattern).__name__ for pattern in pttrn]
    return user_pattern

def read_file(data):
    df = pd.read_excel(data, sheet_name=None)
    combined_df = pd.concat(df.values(), ignore_index=True)
    return combined_df['Data'].tolist()

def store_data_type(data_type):
    return [
        ["int" if char in DIGITS else type(char).__name__ for char in str(item)]
        for item in data_type
    ]

def compare_match_type(user_data, file_pattern):
    user_pattern = get_user_pattern(user_data)
    file_data = read_file(file_pattern)
    data_pattern = store_data_type(read_file(file_pattern))

    for idx, ptrn in enumerate(data_pattern):
        if ptrn == user_pattern:
            print(f"\nData match type with {user_data} with {file_data[idx]}")
            print(f"Match type are {user_pattern}")
        else:
            print(f"\n{file_data[idx]} not match with {user_data}")

if __name__ == "__main__":
    compare_match_type(user_input, user_path)