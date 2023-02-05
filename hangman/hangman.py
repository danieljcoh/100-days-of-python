import random

### THE INFAMOUS HANGMAN GAME ###



#psuedo-code
#### #### #### ####

# generate a word, either using a pre-loaded array of words or || by asking for input for the word || (Hard version)
# then we need to turn that word into a list[]
# then get the len(list) and show it to the guests
# allow the user to input a letter and check it against the indexes of the list[item] using a for loop
# if those items match, replace the item at index in the list with the input
# otherwise, take away a life // or add more ascii art to the drawing of the hanging man
# then finally check to see if they either completed the word or if they ran out of lives, 
# in both cases a change in game state

# instantiate a word list and choose a random word
word_list = ["ardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

# change word into a string of chars
chosen_word_list = []
for char in chosen_word:
    chosen_word_list += char

print(chosen_word_list)

# take the user input for their guess and compare to chosen_word
guess = input("Guess a letter: ").lower()
lives_count = 0

for char in chosen_word_list:
    if guess == char:
        print("TRUE")
    else:
        print("FALSE")


