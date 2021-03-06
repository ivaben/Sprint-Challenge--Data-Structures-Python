import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# This code took 5.93 sec (64 duplicates)
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)


root = (names_1[0], len(names_1[0]))
tree = []
for name in names_1[1:]:
    item = (name, len(name))
    tree.insert(0,item)
    
# searching for duplicates
for name in names_2:
    item = (name, len(name))
    if tree == item:
        duplicates.append(name)


# Using map() + lambda + remove  runtime was 0.003
#res = map(lambda x: names_1.remove(x)
#if x in names_1 else None, names_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
