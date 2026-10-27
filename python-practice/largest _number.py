numbers = [12, 5, 28, 9, 16]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)
