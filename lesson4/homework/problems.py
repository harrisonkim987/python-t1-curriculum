# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = int(input("gimmie score"))
score2 = int(input("gimmie another score"))
if score1 >= 50 and score2 >= 50:
    print("you passed both")
else:
    print("you failure")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = int(input("lunch?"))
water = int(input("water?"))
if lunch == "yes" and water == "yes":
    print("youre ready")
elif lunch == "yes" or water == "yes":
    print("youre kinda ready")
else:
    print("youre doomed")
# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("gimmie number"))
if num < 1 or num > 10:
    print("out")
else:
    print("in")
# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num2 = random.randint(1, 10)
guess = input("gimmie number")
if guess == num2 and guess % 2 == 0:
    print("even match")
elif guess == num2 or guess == 5:
    print("nice try")
else:
    print("nope")
# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
number1 = input("gimmie number")
number2 = input("gimmie another number")
if number1 % 5 == 0 and number2 % 2 == 1 or number2 % 5 == 0 and number1 % 2 == 1:
    print("interesting pair")
else:
    print("plain pair")