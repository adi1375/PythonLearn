import secrets
import string

class Password:
    def __init__(self, length: int = 12,uppercase: bool = True, symbols: bool = True ) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols
        
        
        # Get characters from string module
        self.base_characters: str = string.ascii_lowercase + string.digits
       
        if self.use_uppercase == True:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols == True:
            self.base_characters += string.punctuation
        

    def generate(self) -> str:
        password: list[str] = []
        
        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))
        
        return ''.join(password)

    def check_strength(self, passowrd: str) -> None:
        
        has_upper = any(i.isupper() for i in passowrd)
        has_symbols = any(not i.isalnum() for i in passowrd)
        
        if len(passowrd) > 16 and has_upper and has_symbols:
            print("Strong password.")
        else:
            print("Weak Password.")


def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    random_password = password.generate()
    print(random_password)
    password.check_strength(random_password)


if __name__ == '__main__':
    main()