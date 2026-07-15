name = input("Enter your name: ")

print("Welcome", name, "to the Treasure Hunt Adventure!")

choice = input("You are at a crossroads. Do you go left or right? ").lower()

if choice == "left":
    choice = input("You see a river. Do you swim or build a boat? ").lower()

    if choice == "swim":
        print("A crocodile catches you. You lose!")

    elif choice == "build":
        print("You safely cross the river.")
        choice = input("You find a treasure chest. Open it? (yes/no): ").lower()

        if choice == "yes":
            print("Congratulations! You found gold. You WIN!")
        elif choice == "no":
            print("You walk away and miss the treasure. You lose!")
        else:
            print("Invalid choice. Game Over!")

    else:
        print("Invalid choice. Game Over!")

elif choice == "right":
    choice = input("You enter a cave and see a sleeping dragon. Run or fight? ").lower()

    if choice == "run":
        print("You escaped safely but found no treasure.")

    elif choice == "fight":
        choice = input("You find a magic sword. Pick it up? (yes/no): ").lower()

        if choice == "yes":
            print("You defeated the dragon and found the treasure!")
            print("YOU WIN!")
        elif choice == "no":
            print("Without the sword, the dragon defeats you.")
            print("You lose!")
        else:
            print("Invalid choice. Game Over!")

    else:
        print("Invalid choice. Game Over!")

else:
    print("Invalid choice. Game Over!")

print("Thanks for playing,", name)