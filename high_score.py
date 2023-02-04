## You are going to write a program that calculates the highest score from a List of scores.
## Important you are not allowed to use the max or min functions. The output words must match the example.

# input: 78 65 89 86 55 91 64 89 100

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Don't change the code above

current_highest_score = 0
current_lowest_score = 100

for score in student_scores:
    if (score > current_highest_score):
        current_highest_score = score

    if (score < current_lowest_score):
       current_lowest_score = score

print(current_highest_score)
print(current_lowest_score)