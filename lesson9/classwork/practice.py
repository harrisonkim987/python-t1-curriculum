# Problem 1
# Use a while loop to print the numbers from 1 to 7 (inclusive).
x = 1
while x <= 7:
    print(x)
    x = x+1
# Problem 2
# Use a while loop to count down from 3 to -3 (inclusive), printing each number.
x = 3
while x >= -3:
    print(x)
    x = x-1
# Problem 3
# Ask the user to input a number less than 50.
# Use a while loop to print numbers starting from that number, going up by 2 each time, until you reach 50 (inclusive).
numl50 = int(input("num from 1-50"))
while numl50 <=50:
    print(numl50)
    numl50 = numl50+2
# Problem 4
# Ask the user to input a number.
# Use a while loop to count down by 3 each time until you reach 0 or less (inclusive).
num2 = int(input("another num"))
while num2 >= 0:
    print(num2)
    num2 = num2-3

# Problem 5
# Use a while loop to print each element in the list.
items = ["chair", "table", "desk"]
itemnum = 0
while itemnum < len(items):
    print(items[itemnum])
    itemnum = itemnum + 1