from itertools import permutations

count=0
print("enter list of numbers:")
l=[int(x) for x in input().split()]
print("")
print("permutations of entered numbers are:")
perm=permutations(l)
for i in perm:
    print(i)
    count +=1

print("")
print("number of loops repeated are {}".format(count))
