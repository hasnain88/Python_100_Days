print("Welcome to Treasure Island.")
print("Your mission is to find the treasure....")


cross_road = input("You're at a cross road. Were do you go?\n \t type 'left' or 'right' ").lower()
if cross_road =='left':
    swim_wait = input("You have come to a lake. There is an Island in the middle of the lake. \n \t Type 'wait' to wait for a boat. Type 'swim' to swim across ").lower()
    if swim_wait =='wait':
        door_color = input("You arrived at the island unharmed. There is a house with 3 doors. \n \t One red, One yellow, and one blue. Which color do you choose?").lower()
        if door_color == 'yellow':
            print("You win!")
        elif door_color == 'red':
            print("Burned by fire. Game Over.")
        elif door_color == 'Blue':
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")


    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole Game Over.")

