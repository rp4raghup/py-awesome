# List compression basics

################################################
# Ex1: Square each element of a list.
source_list = [1, 2, 3, 4, 5]

# Traditional way
dest_list = []
for ele in source_list:
  sq = ele * ele
  dest_list.append(sq)

print dest_list

# LC Way
dest_list = [ele*ele for ele in source_list]

###############################################
# Ex2: Filter all odd numbers from list.
source_list = [1, 2, 3, 4, 5, 6]

# Traditional way
dest_list = []
for ele in source_list:
  if ele % 2 != 0:
    dest_list.append(ele)

print dest_list

# LC Way
dest_list = [ele for ele in source_list if ele % 2 != 0]

#################################################
# Ex3: Removing vowels from sentence.
source_str = "this is awesome" # output should be: "ths s wsm"

# Traditional way
dest_str = []
for ele in source_str:
  if ele not in ['a', 'e', 'i', 'o', 'u']:
    dest_str.append(ele)
answer = "".join(dest_str)

# LC Way
dest_list = [ele for ele in source_str if ele not in ['a', 'e', 'i', 'o', 'u']]
answer = "".join(dest_str)

##################################################
# Ex4: Find the sum of all odd numbers in the source_list.
source_list = [11, 21, 2, 4, 24, 13, 6] # Ans: 45

# Traditional way ??

##################################################
# Ex5: replace all the spaces in the string with underscore.
source_str = "this is again awesome" # Ans: "this_is_again_awesome"

# Traditional way ??
# Hint: Use split followed by join.

##################################################
# Ex6: Count number of words (each word is separated by space) in the string.
source_str = "once upon a time" # Ans: 4

# Traditional way ??
# Hint: You may need to use split.

###################################################
# Ex7: Convert words to all caps and all lower alternatively.
source_str = "There Was An Elephant In The Jungle" # Ans: "THERE was AN elephant IN the JUNGLE"

# Traditional way ??
# Hint: "Sample".lower() -> sample ; "Sample".upper() -> "SAMPLE"
# Hint: Use split followed by join and also above functions.

#####################################################
# Ex8: Find maximum number in the source list.
source_list = [10, 2, 89, 44, 12, 73] # Ans: 89

# Traditional way ??
