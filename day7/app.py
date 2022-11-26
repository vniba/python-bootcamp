import random
import hangman_art as art
import hangman_words as words

# Hangman
# random words
# choosing one word
chosen_word = random.choice(words.word_list)
display = []

# life of player
lives = 6
print(f"welcome to \n {art.logo}")
# applying _ for all letters
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"

# checking games current state
end_of_game = False

while not end_of_game:
    user_guess = input("Guess a letter: ".lower())
    if user_guess in display:
        print(f"you entered ' {user_guess} ' again, plz select different letter ")

    # check guessed letter
    choice_true = True
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    print(f"' '{display}")
    # guess letter not in chosen word
    if user_guess not in chosen_word:
        lives -= 1
        print(
            f"you Guessed {user_guess}, that's not in the word. You lose a life\n life remaing:{lives}"
        )
        # if no lives
        if lives == 0:
            end_of_game = True
            print("you Loose..")

    # if no _ then win
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # ascii art of stages
    print(art.stages[lives])
