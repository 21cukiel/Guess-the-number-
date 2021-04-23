import random


def guess_the_number():
    try:
        """function checks if the given number is equal
        to the drawn number and displays an appropriate message"""
        user_number = int(input("Guess the number: "))
        index = 0
        while user_number != random_number:
            if user_number < random_number:
                print("Too small!")
                user_number = int(input("Guess the number: "))
                index += 1
            else:
                print("Too big!")
                user_number = int(input("Guess the number: "))
                index += 1
        print(f"You win in {index + 1} steps")

    except ValueError:
        """when given value is not a number function print message
        "It's not a number" """
        print("It's not a number!")


if __name__ == '__main__':
    random_number = random.randint(1, 100)
    print(guess_the_number())
