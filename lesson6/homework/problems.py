# Problem 1
# Count and print how many times "Alex" appears in the list.
alex = 0
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names)
for i in range(len(names)):
    item = [i]
    if item == "Alex":
        alex = alex + 1
print(alex)
# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
for i in range(len(animals)):
    if animals[i] == "elephant":
        print("elephant found")
        break
    else:
        print("no elephant")
# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
hundreds = 0
for i in range(len(scores)):
    score = hundreds[i]
    if score == 100:
        hundreds = hundreds + 1
print(hundreds)
# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
for i in range(len(colors)):
    if colors[i] == "blue":
        blueindex = i
        print("found blue at index", blueindex)
        break
# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
coldtemps = 0
for i in range(len(temperatures)):
    if temperatures[i] < 0:
        coldtemps = coldtemps + 1
print(coldtemps)