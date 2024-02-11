# number guessing game

winningnumber=10
guess= int(input("Guess winning number:"))
if guess <10:
    print("Your guess is too low")

elif guess >10:
    print("Your guess is too high")

elif guess ==10:
    print("You Win!!!!")