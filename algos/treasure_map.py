# INSTRUCTIONS #
## Your job is to write a program that allows you to mark a square on the map using a two-digit system.  ##
## The first digit in the input will specify the column (the position on the horizontal axis). ##
## The second digit in the input will specify the row number (the position on the vertical axis). ##

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
first_num = position // 10
second_num = position % 10

print(first_num)
print(second_num)

map[second_num - 1][first_num - 1] = "X"

print(map)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
