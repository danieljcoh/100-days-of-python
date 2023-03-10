#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

print()
print()

#EASY LEVEL - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter_list = []
letter_string = ""
symbol_string = ""
number_string = ""

incr = 0
while incr < nr_letters:
    letter_string += letters[random.randint(0, len(letters) - 1)]
    incr += 1


incr = 0
while incr < nr_symbols:
    symbol_string += symbols[random.randint(0, len(symbols) - 1)]
    incr += 1


incr = 0
while incr < nr_numbers:
    number_string += numbers[random.randint(0, len(numbers) - 1)]
    incr += 1

easy_password = letter_string + symbol_string + number_string

print(f"Your weak-ish password is: {easy_password}")


#HARD LEVEL - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password_list = []
hard_password = ""

for character in easy_password:
    hard_password_list.append(character)
    random.shuffle(hard_password_list)

for i in hard_password_list:
    hard_password += i

print(f"Your strong password is: {hard_password}")