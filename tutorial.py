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

# LC Way??
