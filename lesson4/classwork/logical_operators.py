age = int(input("how old are you"))
hasticket = input("do you have ticket for movie yes/no")

if age >= 13 and hasticket == "yes": #and means if both conditions are true
    print("you can watch pg13 movie")
else:
    print("im calling security")
print("check done")

haspass = input("do you have pass")
hasmoney = input("do you have moolah")

if haspass == "yes" or hasmoney == "yes": #or if at least one conditions are true
    print("you can ride")
else:
    print("im calling security")
print("check complete")

homeworkdone = input(did you do your homework)

if not homeworkdone == "yes":#not toggles boolean
    print("enjoy your life while it lasts")
else:
    print("good job you wont die today")

#you can combine multiple logic operators

israining = input("is it raining")
hasumbrella = input("do you have unbrella")

if israining == "yes" and not hasumbrella == "yes":
    print("well the rain is acid rain, ill come to your funeral")

#pemdas, kinda like that first is not then and then or

elif israining == "yes" and hasumbrella == "yes":
    print("you can go outside")
else
    print("no rain, you can go outside")