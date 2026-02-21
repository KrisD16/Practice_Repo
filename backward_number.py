n = int(input("Enter a number: "))
digit = 0
m = 0

while n > 0:
    digit = n % 10
    m = m * 10 + digit
    n = n // 10

print(m)
