import random
import hangman_art
import hangman_words

logo = hangman_art.logo
stages = hangman_art.stages
words_list = hangman_words.word_list

print(logo)

chosen_word = random.choice(words_list)
print(chosen_word)

word_length = len(chosen_word)
placeholder = ""
for i in range(0, word_length):
    placeholder += "_"

print(f"Word to guess: {placeholder}")
print()

game_over = False
right_letters = []
lives = 6

while not game_over:
    print(f"{lives}/6 LIVES LEFT")
    print()

    guess = input("Guess a letter: ").lower()
    print()

    display = ""
    print("\n" * 100)

    if guess in right_letters:
        print(f"You've already guessed '{guess.upper()}'")
        print()

    for i in chosen_word:
        if guess == i:
            display += i
            right_letters.append(guess)
        elif i in right_letters:
            display += i
        else:
            display += "_"
    print(display)
    print()

    if guess not in chosen_word:
        lives -= 1
        if lives >= 1:
            print(f"'{guess.upper()}' is not in the word")
            print()

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print(f"You win. The word is '{display}'")

    if lives == 0:
        game_over = True
        print(f"You lose. The word is '{chosen_word}'")
