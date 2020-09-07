numbers = []
with open("numbers.txt") as n:
    for line in n:
        my_numbers = line.strip().split()
        for number in my_numbers:
            numbers.append(int(number))
print(numbers)
