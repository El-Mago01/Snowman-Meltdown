import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_dashes_and_chars(secret_word, correct_guessed_chars) -> bool:
    word_guessed = True
    for char in secret_word:
        if char in correct_guessed_chars:
            print(char, end=" ")
        else:
            print("_", end=" ")
            word_guessed = False
    return word_guessed

def display_game_state(mistakes: int,secret_word: str, correct_guessed_letters: list) -> bool:
    print(STAGES[mistakes])
    return display_dashes_and_chars(secret_word, correct_guessed_letters)

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    mistakes=0
    correct_guessed_chars=[]
    display_game_state(mistakes, secret_word, correct_guessed_chars)
    game_won=False
    game_iteration=0
    while game_iteration < len(STAGES)-1:
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
        print("Game Over, you won!")
    else:
        print("Game Over, you lost!")


if __name__ == "__main__":
    play_game()