list1 = [1, 2, 3]
list2 = [4, 5, 6]
parallel_lists = zip(list1, list2)
sum = [x + y for (x, y) in parallel_lists]
print(sum)