fruits = ["apple", "banana", "orange"] #must have [] brackets
y = len(fruits) #len = # of items in list
print(y) 
print(fruits)#prints whole list

print(fruits(0))#for computers 0 is first item would print apple

vegetable = ["cucumber", "eggplant", "bell pepper"]

vegetable.append("mushroom")# append adds thing to end
print(vegetable)

vegetable.sort()#sorts items alphabetically

vegetable.insert(2, "carrot") # insert inserts thing into designated
print(vegetable)

vegetable.remove("eggplant")#removes designated item

c = vegetable.pop()# prints last thing and moves it to other list
#you can assign  ^ number to decide what item to move

n = vegetable.index("carrot")#finds position of thing
print(n)
g = vegetable.count("mushroom") #counts number of occurences of thing
