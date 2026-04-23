import random
import ascii_art as aa

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word() -> str:
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_dashes_and_chars(secret_word, correct_guessed_chars) -> bool:
    """
    Displays dashes and character guesses.
    Returns True if the secret word is guessed, False otherwise.
    """
    word_guessed = True
    for char in secret_word:
        if char in correct_guessed_chars:
            print(char, end=" ")
        else:
            print("_", end=" ")
            word_guessed = False
    return word_guessed

def display_game_state(mistakes: int,secret_word: str, correct_guessed_letters: list) -> bool:
    """Displays game state after a new guess"""
    print(aa.STAGES[mistakes])
    return display_dashes_and_chars(secret_word, correct_guessed_letters)

def play_game():
    """ Contains the game logic:
    Stage 0: Welcome the player
    Stage 1: Show the snowman
    Stage 2: Guess a letter
    Stage 3: feedback if the letter was guessed correctly and at what place the letter fits
    Stage 4: verify if the game is finished and if the player won or lost
    Stage 5: Provide the player with an end message

    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    mistakes=0
    correct_guessed_chars=[]
    display_game_state(mistakes, secret_word, correct_guessed_chars)
    game_won=False
    game_iteration=0
    while game_iteration < len(aa.STAGES)-1:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        print(game_iteration)
        if guess in secret_word and guess not in correct_guessed_chars:
            correct_guessed_chars.append(guess)
            print(game_iteration)
        elif guess not in secret_word:
            mistakes += 1
            game_iteration += 1
        print(game_iteration)
        game_won=display_game_state(mistakes,secret_word,correct_guessed_chars)
        if game_won:
            break
    if game_won:
        print("Game Over, you won, you saved the snowman!")
    else:
        print("Game Over, you lost, the snowman melted. He needs a doctor!")
