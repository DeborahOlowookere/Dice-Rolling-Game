import random

counter = 0

while True:
    choice = input("Roll the dice? (y/n:) ").lower()
    if choice == "y":
        try:
            num_roll = int(input("How many dice do you want to roll?: "))
            if num_roll < 1:
                print("Please enter a positive number.")
                continue
            for i in range(num_roll):
                counter += 1
                dice = random.randint(1, 6)
                print(f"You rolled a {dice}!")
                print(f"You have rolled the dice {counter} time(s) so far.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "n":
        print(
            f"Thanks for playing!. You rolled the dice {counter} time(s) in total.")
        break
    else:
        print("Invalid choice. Please try again.")
