letters =[]
for i in range(97,123):
    letters+=chr(i)
    
def caesar_cipher(original_text, shift_length, encode_or_decode):
    output_msg =""
    
    if encode_or_decode == "decode":
        shift_length*=-1
        
    for char in original_text:
        
        if char not in letters:
            output_msg+=char
        
        else:
            new_position=letters.index(char)+shift_length
            new_position%=len(letters)
            output_msg+=letters[new_position]
        
    print(f"Here's your {encode_or_decode}d message: {output_msg.lower()}")
    
choice = "yes"
while choice == "yes":
    mode = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    msg = input("Enter your message:\n").lower()
    shift= int(input("Enter the shifting length: \n"))
    caesar_cipher(msg,shift,mode)
    choice = input("Type 'yes' if you want to continue, 'no' to stop.\n").lower()