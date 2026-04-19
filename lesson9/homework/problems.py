# Problem 1
# Use a while loop to print the word "Python" 4 times.
pythoncount = 1
while pythoncount <= 4:
    print("python")
    pythoncount = pythoncount + 1
# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
evens = 2
while evens <= 12:
    print(evens)
    evens = evens+2
# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
posnum = int(input("positive number"))
currentnum = 0
while currentnum <=posnum:
    print(currentnum)
    currentnum = currentnum + 1
# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
numg10 = int(input("num greater than 10"))
while numg10 > 0:
    print(numg10)
    numg10 = numg10-5
# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals = ["turtle", "bird", "dog"]
animal = 0
while animal < len(animals):
    print(animals[animal])
    animal = animal+1