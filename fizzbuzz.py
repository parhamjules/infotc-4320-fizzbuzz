# FizzBuzz Challenge - Iteration 3
# Task: Ensure program is readable, understandable, and clean.

for n in range(1, 101):
    div_by_3 = n % 3 == 0
    div_by_5 = n % 5 == 0
    if not div_by_3 and not div_by_5:
        print(n)
        continue
    res = ""
    if div_by_3: res += "Fizz"
    if div_by_5: res += "Buzz"
    print(res)
