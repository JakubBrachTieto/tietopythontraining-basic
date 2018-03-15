def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


while True:
    try:
        n = int(input("Input a int number: "))
        if n < 0:
            print("The number must be non-negative")
            continue
        print("The result is:", fib(n))
        break
    except ValueError:
        print("The number must be an integer")