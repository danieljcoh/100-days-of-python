#WRITE A PROGRAM USING NESTED IF STATEMENTS TO DETERMINE WHAT THE PRICE OF THE PIZZA DESIRED WOULD BE BASED ON INPUTS

## Pizza Type
small_pizza = 15
medium_pizza = 20
large_pizza = 25

## Toppings
extra_cheese = 1
pepperoni_S = 2
pepperoni_ML = 3

## Final Price
price = 0

## Program Start
pizza_choice = input("What size pizza would you like S, M, or L: ").lower()

if pizza_choice == "s":
    price = small_pizza
elif pizza_choice == "m":
    price = medium_pizza
elif pizza_choice == "l":
    price = large_pizza
else:
    print("Not a valid input.")

#### #### #### #### #### ####

pepperoni = input("Would you like pepperoni or no? Y or N: ").lower()

if pepperoni == "y" and pizza_choice == "m" or pepperoni == "y" and pizza_choice == "l":
    price += pepperoni_ML
elif pepperoni == "y" and pizza_choice == "s":
    price += pepperoni_S

#### #### #### #### #### ####

wants_cheese = input("Do you want extra cheese? Y or N: ").lower()

if wants_cheese == "y":
    price += 1

print(f"Your pizza will cost you ${price}")


