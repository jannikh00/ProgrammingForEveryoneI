# This program asks the user to pick a player out of the given soccer-GOAT-discussion list.
# Depending on the choice it says whether the choice is right or wrong. Please take it with humor if you don't agree :)

import sys

football_players = ["Lionel Messi (1)", "Cristiano Ronaldo (2)", "Pele (3)", "Diego Maradona (4)"]

goats= {
    1 : "Lionel Messi",
    2 : "Cristiano Ronaldo",
    3 : "Pele",
    4 : "Diego Maradona"
}

print("What is your name?\n")
name = input()

print("\nHello " + name + "! I think we all agree that the GOAT talks in soccer are limited to the following players.\n")
print(football_players)
print("\n")

print("Who is the one and only GOAT in your opinion? Please put in the number.\n")

x = input()
if int(x) >= 5 or int(x) <= 0:
    print("\nPlease restart the program and choose a number between 1-4.")
    sys.exit()
y = goats[int(x)]

if int(x) == 1:
    print("\nYou're right!  " + y + " is the one and only GOAT. Congratulations on knowing ball!")
else:
    print("\nI'm sorry. Unfortunately you're wrong. " + y + " is not the GOAT.")
    print("The one and only GOAT is " + goats[1] + "! I hope you learned something out of using this program.")