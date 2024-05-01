import random
correct_number = random.choice(range(1, 101))
print("This is the correct number: " + str(correct_number))
print("""Welcome to the guessing number game!
I'm thinking of a number between 1 and 100.""")
difficulty_level = input("What level do you want choose between easy and hard? ")

def difficulty():
    if difficulty_level == "hard":
        attempt = 5
    elif difficulty_level == "easy":
        attempt = 10
    i = 0
    while i < attempt:
        print("You have " + str(attempt) + " attempts.")
        guess = int(input("What is your guess? "))

        if guess > correct_number:
            print("Too high")
            attempt -= 1
            
        elif guess < correct_number:
            print("Too low")
            attempt -= 1
            
        else:
            print("You won!")
            return 0
    print("You lost!")

difficulty()


