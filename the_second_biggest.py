n = int(input("Enter the number of numbers: "))
numbers = []
second_max = 0

for i in range(0, n):
    number = int(input("Enter a number: "))
    numbers.append(number)

for i in range(0, n):
    for j in range(0, n - 1):
        if numbers[j] > numbers[j + 1]:
            x = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = x

second_max = numbers[-2]
print(second_max)
