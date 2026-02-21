number = int(input("Enter a number: "))
digit = 0
m = 0

while number > 0:
    digit = number % 10
    m = m * 10 + digit
    number //= 10

print(m)
