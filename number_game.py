# Number Guessing game in Python
import random

win_num = random.randint(1, 100)
attempts = 0

while True:
    try:
        guessed_num = int(input("Enter any number between 1 to 100: "))
    except ValueError:
        print("❌ Invalid input! Numbers only, please.")
        continue  # Ask again!

    attempts += 1

    if guessed_num == win_num:
        print(f"🎉 You Win! in {attempts} attempts")
        break
    elif guessed_num < 1 or guessed_num > 100:
        print("Not a valid Number, please enter number between 1 to 100")
    elif guessed_num > win_num:
        print("Too High! Try lower number")
    elif guessed_num < win_num:
        print("Too Low! Try higher number")
