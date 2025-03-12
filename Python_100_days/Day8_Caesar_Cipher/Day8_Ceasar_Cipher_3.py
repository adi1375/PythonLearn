def caesarCipher(text, shift, mode):
    output =""
    
    if mode == "decode":
        shift*=-1
    
    for i in range(len(text)):
        char = text[i]
        
        if(char.isupper()):
            output+= chr((ord(char)+shift-65)% 26 + 65)
    
        elif(char.islower()):
            output+= chr((ord(char)+shift-97)% 26 + 97)
            
        else:
            output+=char

    print(f"Originial text: {text}")
    print(f"{mode}d text: {output}")

# msg = "Hello Coders? How is 8th day?"
# shift = 9
# mode = "encode"
# caesarCipher(msg, shift, mode)
# print("=====================================")
# print("=====================================")
# msg = "Qnuux Lxmnab? Qxf rb 8cq mjh?"
# shift = 9
# mode = "decode"
# caesarCipher(msg, shift, mode)

choice = "yes"
while choice == "yes":
    mode = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    msg = input("Enter your message:\n")
    shift= int(input("Enter the shifting length: \n"))
    caesarCipher(msg,shift,mode)
    choice = input("Type 'yes' if you want to continue, 'no' to stop.\n").lower()