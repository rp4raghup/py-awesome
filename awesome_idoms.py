#!/usr/bin/python

# List comprehension to get the sum of squares of all numbers
l = [1, 2, 3, 4, 5]
print sum([x*x for x in l])

# Few argue that by using map we can achieve the same thing. The only problem here is 
# for every element it calls a function.
print sum(map(lambda x: x*x, l))

# The below snippet retuns max number of times repeated number in a given list
l = [1, 2, 3, 3, 2, 1, 2, 5]
print max(set(l), key=l.count)

# Intersection of two lists l1, l2
list1 = [1, 2, 3]
list2 = [2, 3, 4]
l = list(set(list1).intersection(list2))

# Filter function to filter based on some condition
l = [-5, -3, -1, 1, 3, 5]
print filter(lambda x: x < 0, l)

# Reduce is similar to filter but the final output will be a single number.
# Example to get the sum of all elements of a list.
l = [-5, -3, -1, 1, 3, 5]
print reduce(lambda x, y: x + y, l)
