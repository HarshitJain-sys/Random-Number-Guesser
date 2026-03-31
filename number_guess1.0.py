import random
import time

def exit_choice(user_choice):
    if user_choice.upper() in ["Y", "YES"]:
        return True
    elif user_choice.upper() in ["N", "NO"]:
        print("Thank You for Playing!")
        return False
    else:
        print("Invalid choice, exiting...")
        return False


def play(user_name):
    print("\nGenerating a Random Number...")
    time.sleep(2)
    random_number = random.randint(0, 10)

    print("Random Number Generated!")

    for i in range(3):
        try:
            user_input = int(input(f"Enter your Guess {i+1}: "))
        except:
            print("Enter a valid number!")
            continue

        if user_input == random_number:
            if i == 0:
                print("Clutched! First try 🔥")
            elif i == 1:
                print("Nice! Second try 👍")
            else:
                print("Finally! Last chance 😅")

            print("You Win!")
            return

        else:
            print("Wrong guess!")
            print(f"Chances left: {2 - i}")

    print(f"\nYou Lost! The number was {random_number}")

print("*************************************************************")
print("************* Welcome to Number Guessing Game ****************")
print("*************************************************************")

user_name = input("Enter Your Username: ")

print("\nRules:")
print("1. You have 3 chances")
print("2. Number is between 0 and 10")

is_playing = True

while is_playing:
    play(user_name)
    user_choice = input("\nDo you want to play again (Y/N): ")
    is_playing = exit_choice(user_choice)