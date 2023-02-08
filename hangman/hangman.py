import random
import hangman_art
import hangman_words

# VARS
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
display = []
word_length = len(chosen_word)
lives = 6

# To see the word that's displayed for debugging
print(f'Pssst, the solution is {chosen_word}.')

# create the list that shows the empty, length of the chosen word for the player
for _ in chosen_word:
  display += "_"
  
print()
print()

# Introduction
print("Welcome to...")
print(hangman_art.logo)
print()
print("...try to guess the word below.")
print("You have six lives. Only input one letter at a time.")
print("Enjoy!")
print()
print()
print("#### ####")
print()
print()
print(hangman_art.stages[lives])
print()

# Game Loop
while not end_of_game:

    print()
    print(display)
    print()
    guess = input("Guess a letter: ").lower()
    print()

    if guess in display:
      print()
      print(f"You've already guessed {guess}.")
      print()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print()
        print(f"Your guess of: {guess}, is not in the word. You lose a life!")
        print()
        lives -= 1
        if lives == 0:
            print(hangman_art.you_lose)
            end_of_game = True
            break 

    if "_" not in display:
        end_of_game = True
        print(hangman_art.you_win)
        print()
        print(chosen_word)
          
    print()
    print()
    print("---- ---- ----")
    print(f"You have {lives} lives left.")
    print("---- ---- ----")
    print(hangman_art.stages[lives])

