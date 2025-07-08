"""Recreating Wordle Using Code!"""

__author__: str = "730766142"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:  # < OR = because you can use all 6 of the turns.
        print("=== Turn " + str(turn) + "/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # assigning a variable to the user's guess
        if guess == secret:
            print(emojified(guess, secret))
            print("You won in " + str(turn) + "/6 turns!")
            return
        else:
            print(emojified(guess, secret))
            turn += 1  # only adds a turn if the user didn't guess the secret word...
            # b/c if not, they would've won (if statement)!
    print(
        "X/6 - Sorry, try again tomorrow!"
    )  # only prints when while loop is False (all 6 turns are over)


def contains_char(word: str, letter: str) -> bool:
    """Determines if a certain letter is found in a word."""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0  # used to iterate over first parameter
    while i < len(word):
        if letter == word[i]:
            return True
        i += 1
    return False  # returns False only after checking every single letter of the word


def emojified(guess: str, secret: str) -> str:
    """Returns string of color-coded emojis representing the results of the guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    i: int = 0  # used to compare character "i" of guess to secret
    emojis: str = ""
    while i < len(guess):
        if (
            guess[i] == secret[i]
        ):  # if letter and position match between guess and secret word
            emojis += GREEN_BOX
        elif contains_char(
            secret, guess[i]
        ):  # if letter is in the secret word but not in correct position
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess(length: int) -> str:
    """Prompts user for a guess of the expected length"""
    prompt: str = input("Enter a " + str(length) + " character word:")
    while len(prompt) != length:
        prompt = input(
            "That wasn't " + str(length) + " chars! Try again:"
        )  # updates prompt to continue displaying this msg if condition is False
    return (
        prompt  # return the final input the user gives (occurs if while loop is False)
    )


if __name__ == "__main__":
    main(secret="codes")
