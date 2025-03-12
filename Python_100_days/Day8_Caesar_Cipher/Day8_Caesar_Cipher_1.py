letters =[]
for i in range(97,123):
    letters+=chr(i)
for i in range(65,91):
    letters+=chr(i)
    
# print(letters)
    
def caeser_cipher(text,shift_length,mode):
    result =""
    if mode == "decode":
        text = text.upper()
        shift_length*=-1
    else:
        text = text.lower()
    
    for char in text:
        if char not in letters:
            result+=char
        else:
            result+=letters[letters.index(char)+shift_length]
    
    print(f"Here's your {mode}d message: {result.lower()}")

choice = "yes"
while choice == "yes":
    mode = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    msg = input("Enter your message:\n")
    shift= int(input("Enter the shifting length: \n"))
    caeser_cipher(msg,shift,mode)
    choice = input("Type 'yes' if you want to continue, 'no' to stop.\n").lower()