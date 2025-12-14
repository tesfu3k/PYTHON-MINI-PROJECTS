name = input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input("You are in a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. Game Over!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game. Game Over!")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they got offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
print("Thank you for trying", name) 