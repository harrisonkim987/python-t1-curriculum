import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
opsysts = ["dunno", "dunno2", "dunno3"]
print(opsysts.index(len(opsysts)))
print(opsysts(2), opsysts(1), opsysts(0))
# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["history", "math", "ela", "science"]
print(subjects(1))
#teacher said we donot have to this part we dont know how to sort alphabetically
# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errors = [400, 403, 500, 404, 401]
print(len(errors))
print(errors.index(403))
# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
prolang = ["c++", "javascript"]
print(prolang(random.randint(1, 2)))
prolang.append("python")
print(prolang)
# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passcodes = ["password1", "h3ll0", "^_^", "supersecure", "Coo1c@k3", "100%stupid"]
print(passcodes(len(passcodes) / 2))
passcodes.remove(passcodes(1))
print(passcodes)