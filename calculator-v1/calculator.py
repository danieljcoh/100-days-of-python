from replit import clear
from art import logo
def add(n1, n2):
    """Returns the combined sum of both parameters"""
    return n1 + n2


def subtract(n1, n2):
    """Returns the subtracted amount after n1 - n2"""
    return n1 - n2


def multiply(n1, n2):
    """Returns the multiplied sum of the parameters"""
    return n1 * n2


def divide(n1, n2):
    """Returns the divided amount of the parameters"""
    return n1 / n2


mathematical_operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():

  print(logo) 

  
  # First Number
  num1 = float(input("What is the first num: "))
  
  # Operation Choice
  for key in mathematical_operations:
    print(key)
  operation_symbol = input("Pick operation symbol from the line above: ")
  operation_function = mathematical_operations[operation_symbol]
  
  # Second Number
  num2 = float(input("What is the second num: "))
  
  first_answer = operation_function(num1, num2)
  
  # Print
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  to_continue = input("Do you want to continue this operation? Y or N: ").lower()
  if to_continue == "y":
    to_continue = True
  else:
    to_continue == False
    
  while to_continue == True:
    num3 = float(input("Pick a another number: "))
    for key in mathematical_operations:
      print(key)
    operation_symbol = input("Pick operation symbol from the line above: ")
    operation_function = mathematical_operations[operation_symbol]
    second_answer = operation_function(first_answer, num3)
  
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    
    first_answer = second_answer
  
    to_continue = input("Do you want to continue this operation? Y or N: ").lower()
    if to_continue == "y":
      to_continue = True
    else:
      to_continue == False
      calculator()


calculator()
  