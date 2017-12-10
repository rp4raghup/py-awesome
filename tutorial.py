# List compression basics

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
