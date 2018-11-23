from itertools import permutations
# taking string inputs from user
count=0
str=input("enter any string:")
print("")
print("you entered : {}".format(str))
print("")

# performming permutations
perm=permutations(str)
for i in perm:
    print(i)
    count +=1

#counting number of permuatations
print("")
print("total number of permuatations for {} are : {}".format(str,count))
