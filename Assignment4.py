# Fibonacci using Dynamic Programming
# Memoization and Tabulation


# Memoization
def fib_memo(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# Tabulation
def fib_dp(n):
    if n <= 1:
        return n

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Main Program
n = int(input("Enter the value of n: "))

# Memoization
memo = {}
result1 = fib_memo(n, memo)

# Tabulation
result2 = fib_dp(n)

print("\nUsing Memoization:")
print("Fibonacci number =", result1)

print("\nUsing Tabulation:")
print("Fibonacci number =", result2)