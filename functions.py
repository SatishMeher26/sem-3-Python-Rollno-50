def get_factorial(n):
    if n < 0:
        print("Factorial is not defined for negative number:")
    else:
        result = 1
        for i in range(1,n + 1):
            result*= i
        return result
    
n= int(input("Enter your number"))
get_factorial(n)