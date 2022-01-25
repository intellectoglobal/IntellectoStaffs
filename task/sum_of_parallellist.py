x = [1, 2, 3]
y = [4, 5, 6]
parallel_lists = zip(x, y)
sum = [x + y for (x, y) in parallel_lists]
print(sum)