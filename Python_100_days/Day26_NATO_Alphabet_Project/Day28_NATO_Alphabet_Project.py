import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("Python_100_days/Day26_NATO_Alphabet_Project/nato_phonetic_alphabet.csv")
# print(nato_data)
nato_dict ={row.letter:row.code for index,row in nato_data.iterrows()}
# print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in word if letter in nato_dict]
print(nato_list)