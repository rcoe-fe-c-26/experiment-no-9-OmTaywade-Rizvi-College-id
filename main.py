# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
def Factorial(n):
    if(n < 0):
        print(f"Factorial of {-n} is Not Defined")
    
    elif(n == 0 or n == 1):
        print(f"Factorial of {n} is 1")
    
    else:
        fact= 1
        for i in range(1, int(n+1)):
            fact *= i
        print(f"Factorial of {n} is {fact}")

num = int(input("Enter Number: "))
Factorial(num)
