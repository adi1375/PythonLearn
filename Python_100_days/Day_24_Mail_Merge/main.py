PLACEHOLDER = "[name]"

with open("Python_100_days/Day_24_Mail_Merge/Input/Names/invited_names.txt") as file1:
    invited_names = file1.readlines()

with open("Python_100_days/Day_24_Mail_Merge/Input/Letters/starting_letter.txt") as file2:
    letter = file2.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"Python_100_days/Day_24_Mail_Merge/Output/ReadyToSend/letter_for_{stripped_name}",mode="w") as file3:
            file3.write(new_letter)