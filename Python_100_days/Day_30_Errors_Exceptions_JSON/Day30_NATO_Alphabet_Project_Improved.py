import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("Python_100_days/Day_26_NATO_Alphabet_Project/nato_phonetic_alphabet.csv")
# print(nato_data)
nato_dict ={row.letter:row.code for index,row in nato_data.iterrows()}
# print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_alphabet():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry. Only letters in the alphabet please.")
        nato_alphabet()
    else:
        print(nato_list)
        
if __name__ == "__main__":
    nato_alphabet()