#!/usr/bin/python
# The below snippet retuns max number of times repeated number in a given list.
l = [1, 2, 3, 3, 2, 1, 2, 5]
print max(set(l), key=l.count)