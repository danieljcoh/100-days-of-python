def prime_checker(number):
    is_prime = True
    
    if number == 1:
        is_prime = False
        
    for num in range (2, number):
        if number % num == 0:
            is_prime = False
            
    if is_prime == True:
        print("It's a prime number!")
    else:
        print("It's not a prime number!")

n = int(input("Check this number: "))
prime_checker(number=n)