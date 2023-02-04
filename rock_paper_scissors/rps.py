import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Use to update in the future for multiple rounds #
player_score = 0
ai_score = 0

while player_score <= 1 or ai_score <= 1:

    # question #
    choice = input("Rock, Paper, or Scissors? \n").lower()

    choice_list = [rock, paper, scissors]
    ai_choice = random.randint(0, 2)

    print()
    print()

    # Print player choice #
    if (choice == "rock"):
        print("Player Choice: ")
        print(rock)
    elif (choice == "paper"):
        print("Player Choice: ")
        print(paper)
    elif (choice == "scissors"):
        print("Player Choice: ")
        print(scissors)

    print()
    print()

    # Print AI choice #
    ### 0 Rock, 1 Paper, 2 Scissors for AI ###
    if (ai_choice) == 0:
        print("AI Choice: ")
        print(rock)
    elif (ai_choice == 1):
        print("AI Choice: ")
        print(paper)
    elif (ai_choice == 2):
        print("AI Choice: ")
        print(scissors)

    print()
    print()

    # Find winner #
    if (choice == "rock") and (ai_choice == 0) or (choice == "paper") and (
            ai_choice == 1) or (choice == "scissors") and (ai_choice == 2):
        print()
        print("It's a tie!")
        player_score += 1
        ai_score += 1
        print()
        print()
        print(f"Player score is {player_score}.")
        print(f"AI score is {ai_score}.")
        print()
        print()
    elif (choice == "rock") and (ai_choice == 2) or (choice == "paper") and (
            ai_choice == 0) or (choice == "scissors") and (ai_choice == 1):
        print()
        print("You win!")
        print()
        print("Computer loses!")
        player_score += 1
        print()
        print()
        print(f"Player score is {player_score}.")
        print(f"AI score is {ai_score}.")
        print()
        print()
    elif (choice == "rock") and (ai_choice == 1) or (choice == "paper") and (
            ai_choice == 2) or (choice == "scissors") and (ai_choice == 0):
        print()
        print("Computer win!")
        print()
        print("You lose!")
        ai_score += 1
        print()
        print()
        print(f"Player score is {player_score}.")
        print(f"AI score is {ai_score}.")
        print()
        print()
    else:
        print()
        print("Computer win!")
        print()
        print("You lose!")
        ai_score += 1
        print()
        print()
        print(f"Player score is {player_score}.")
        print(f"AI score is {ai_score}.")
        print()
        print()

    if (player_score == 2):
        break
    elif (ai_score == 2):
        break

print()
print()

if (player_score == 2):
    print('''
  ██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ ''')
elif (ai_score == 2):
    print('''
   ██████  ██████  ███    ███ ██████  ██    ██ ████████ ███████ ██████      ██     ██ ██ ███    ██ ███████ ██ 
██      ██    ██ ████  ████ ██   ██ ██    ██    ██    ██      ██   ██     ██     ██ ██ ████   ██ ██      ██ 
██      ██    ██ ██ ████ ██ ██████  ██    ██    ██    █████   ██████      ██  █  ██ ██ ██ ██  ██ ███████ ██ 
██      ██    ██ ██  ██  ██ ██      ██    ██    ██    ██      ██   ██     ██ ███ ██ ██ ██  ██ ██      ██    
 ██████  ██████  ██      ██ ██       ██████     ██    ███████ ██   ██      ███ ███  ██ ██   ████ ███████ ██ 
                                                                                                            '''
          )
