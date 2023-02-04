## You are going to write a program that calculates the average student height from a List of heights. ##
## e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
## The average height can be calculated by adding all the heights together and dividing by the total number of heights.
## e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
## Important You should not use the sum() or len() functions in your answer. 
## You should try to replicate their functionality using what you have learnt about for loops.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Write your code below this row

print(student_heights)

count = 0
total_heights = 0

for height in student_heights:
    print(height)
    total_heights += height
    count += 1

average_height = total_heights // count

print(average_height)