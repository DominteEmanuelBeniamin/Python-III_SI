# Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Introduceți n: "))
rezultat_fibonacci = fibonacci(n)
print(f"Primii {n} termeni din șirul Fibonacci sunt: {rezultat_fibonacci}")
