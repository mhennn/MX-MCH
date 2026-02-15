from utils.logo import logo
from utils.initiated import INITIATED
from core.data_handling import ReadData

print(logo)

user_input = input("Input text you want to pattern analyze: ")
user_path = input("Input the file you want to compare: ")

print(INITIATED)

read_data = ReadData()

if __name__ == "__main__":
    read_data.compare_match_type(user_input, user_path)