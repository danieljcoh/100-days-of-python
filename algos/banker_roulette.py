### You are going to write a program that will select a random name from a list of names. 
###The person selected will have to pay for everybody's food bill.

import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#len(array) gives me the length
print(len(names))
random_num = random.randint(0, len(names) - 1)
print(random_num)

print(f"{names[random_num]} is going to buy the meal today!")