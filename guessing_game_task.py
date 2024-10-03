"""_summary_
    """
import random
def check_number(random_number , n):
    print("The number is " , random_number )
    if n == random_number:
        return True
    else:
        return False


def game():
    random_number = random.randint(1, 1000)
    # create a random value here
    n = int(input("Enter a random number between 1 and 1000"))

    outcome = check_number(random_number, n)

    if outcome:
        return True
    else:
        return False



print("Welcome to my guessing game. Do you have what it takes to win?")
answer = input("yes or no")
if answer == "yes":
    game_outcome = game()
    if game_outcome:
        print("Yay! , you win")
    else:
        print("Sorry! , you lost")
        print("Would you like to try again!")
        answer = input("yes or no")
        if answer == "yes":
            game_outcome = game()
            if game_outcome:
                print("Yay! , you win")
            else:
                print("Sorry you lost , game over")
else:
    print("So sad , I would have love you to try my game")
