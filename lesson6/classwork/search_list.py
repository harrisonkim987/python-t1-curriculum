fruits = ["apple", "banana", "cherry"]

if "apple" in fruits: #if apple is in list 
    print("found apple")
else:
    print("apple not found")

found = False
index = -1

for i in range(len(fruits)): #looping through list repeat until
    if fruits[i] == "apple":
        found = True 
        index = i
        break
if found == True:
    print("found apple at index", index)
else:
    print("apple not found")

