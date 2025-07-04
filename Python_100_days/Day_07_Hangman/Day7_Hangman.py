import random
import hangman_words

print("Welcome to Hangman!")
chosen_word = random.choice(hangman_words.word_list)
lives = len(chosen_word)

blank_space = ""
for i in range(len(chosen_word)):
    blank_space += "_"
print(f"Word to guess: {blank_space}")
print(f"{lives} letter word. {lives} lives remaining.")

game_over = False
correctly_guessed_letters = []
while not game_over:
    answer = ""

    guess = input("\nGuess a letter in the word: ").lower()

    if guess in correctly_guessed_letters:
        print(f"Already guessed the letter '{guess}'.")

    for letter in chosen_word:
        if letter == guess:
            answer += guess
            correctly_guessed_letters.append(guess)
        elif letter in correctly_guessed_letters:
            answer += letter
        else:
            answer += "_"

    if guess not in answer:
        print(f"The letter '{guess}' is not present in the word.")
        print("You've lost a life.")
        lives -= 1
    print(f"Word : {answer}")
    print(f"Remaining lives :{lives}/{len(chosen_word)}")

    if answer == chosen_word:
        print(f"You guessed the word. You win!")
        game_over = True
    elif lives == 0:
        print(f"You've lost all your lives. You lose!")
        game_over = True
