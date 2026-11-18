# Number Guessing game in Python
win_num = 9

while True:
    try:
        guessed_num = int(input("Enter any number between 1 to 100: "))
    except ValueError:
        print("❌ Invalid input! Numbers only, please.")
        continue  # Ask again!

    if guessed_num == win_num:
        print("You Win!")
        break
    elif guessed_num < 1 or guessed_num > 100:
        print("Not a valid Number, please enter number between 1 to 100")
    else:
        print("Wrong Guess! Try Again")
