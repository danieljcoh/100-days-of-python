# INSTRUCTIONS: Write a program that takes two name inputs and counts the amount of times the letters of T R U E and L O V E
# appear in their names. Add the scores together and print out an intepretation based on what their True Love score is.


first_name = input("Enter the first Lover's name: ").lower()
second_name = input("Enter the second Lover's name: ").lower()

true_score = 0
love_score = 0

true_score += first_name.count("t")
true_score += first_name.count("r")
true_score += first_name.count("u")
true_score += first_name.count("e")

true_score += second_name.count("t")
true_score += second_name.count("r")
true_score += second_name.count("u")
true_score += second_name.count("e")

love_score += first_name.count("l")
love_score += first_name.count("o")
love_score += first_name.count("v")
love_score += first_name.count("e")

love_score += second_name.count("l")
love_score += second_name.count("o")
love_score += second_name.count("v")
love_score += second_name.count("e")


trueLove_score = str(true_score) + str(love_score)

trueLove_score = int(trueLove_score)


if trueLove_score < 10 or trueLove_score > 90:
    print(f"Your score is {trueLove_score}, you go together like coke and mentos.")
elif trueLove_score >= 40 and trueLove_score <= 50:
    print(f"Your score is {trueLove_score}, you are alright together.")
else:
    print(f"Your score is {trueLove_score}.")