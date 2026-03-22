numbers = [14, 4, 25, 64389, 10, 1]

counter = 0 #keeps count of how many numbers greater than 5

for i in range(len(numbers)):
    item = numbers[i]
    if item > 5:
        counter = counter + 1
print("there are", counter, "numbers greater than 5 in our list")

animals = ["cat", "dog", "cat", "porcupine", "humpback whale", "adelaide penguin"]

counter2 = 0 #keeps count of how many times cat appears

for i in range(len(animals)):
    item2 = animals[i]
    if item2 == "cat":
        counter2 = counter2 + 1
print("there are", counter2, "cats in our list")
numcats = animals.count("cat")