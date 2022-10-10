# FizzBuzz Challenge - Iteration 2
# Task: Improve efficiency of the program.

for n in range(1, 101):
    if n % 3 != 0 and n % 5 != 0:
        print(n)
        continue
    res = ""
    if n % 3 == 0: res += "Fizz"
    if n % 5 == 0: res += "Buzz"
    print(res)
