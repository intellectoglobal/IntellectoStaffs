numbers = (2, 3, 2, 3, 5, 6, 5, 7, 6)
uniques = []
for numbers in numbers:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)