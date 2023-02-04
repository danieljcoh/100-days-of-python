#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# ## GET NUM OF BILL PAYERS


### OLD CODE STARTS HERE
# num_of_people = int(input("How many people are splitting the bill? "))

# incre_var = 0
# names_of_bill_payers = []

# # while loop increment is less than people because arrays start at 0
# while(incre_var < num_of_people):
#   print("Remember to enter every payers name.")
#   payer_name = input("Enter a payer's name? ")
#   names_of_bill_payers.append(payer_name)
#   incre_var += 1


# print(f"What did {names_of_bill_payers[0]} get? Input true if they got more things.")
# item = input("Does payer have unadded food? Answer 'True' if yes, 'False' if no. Caps matters.")

# payer_item_list = []
# while item == "True":
#   food_item_price = float(input("Add the price of an item the payer got? "))
#   payer_item_list.append(food_item_price)
# # print(names_of_bill_payers)

# bill_before_tax = float(input("What is the bill before the tax or tip is added? "))
# tax = float(input("What is the tax by itself? "))
# tip_percentage = int(input("What percent tip do you want to leave? Answer in whole numbers: "))
# tip_percentage = tip_percentage / 100

# bill_total_before_tip = bill_before_tax + tax
# tip = bill_total_before_tip * tip_percentage

# bill_total = bill_total_before_tip + tip
### OLD CODE ENDS HERE

name = input("What is your name? ")

num_of_items = int(input(f"Hey {name}. How many items did you get while dining today? "))

increment = 0 
# The price before tax and tip
price_before = 0

while increment < num_of_items:
  item_price = float(input("Enter the price of an item you got? Enter them one at a time: $"))
  price_before += item_price
  increment += 1

tax = float(input("What is the tax of the whole bill: $"))
num_of_people_in_party = int(input("How many people were in the party you dined with: "))
payers_tax = tax / num_of_people_in_party
price_before += payers_tax

tip_percentage = int(input("What percentage of tip do you want to leave? Enter in whole numbers: %"))

# This tip is based off the individual's bill but I come from the food industry and it should be based off the entire bill, IMHO
# I will fix this a little later (Said on and by Dan -- Feb 3, 2023)
tip_of_bill = tip_percentage / 100 + 1

price_after = price_before * tip_of_bill
price_after = round(price_after, 2)
price_after = "{:.2f}".format(price_after)

print(f"Well {name}, it seems like you owe ${price_after}.")



