import snowman
import pytest

from game_logic import display_game_state, display_dashes_and_chars, get_random_word

#display_game_state(mistakes: int,secret_word: str, correct_guessed_letters: list) -> bool:
def test_display_game_state_TRUE_1():
    assert display_game_state(3,"python",['p','y','t','h','o','n']) == True

def test_display_game_state_TRUE_2():
    assert display_game_state(3,"pytho",['p','y','t','h','o','n']) == True

def test_display_game_state_TRUE_3():
    assert display_game_state(3,"pythop",['p','y','t','h','o']) == True

def test_display_game_state_FALSE_1():
    assert display_game_state(3,"pythons",['p','y','t','h','o','n']) == False

def test_display_game_state_FALSE_2():
    assert display_game_state(3,"pythons",[]) == False

# display_dashes_and_chars(secret_word, correct_guessed_chars) -> bool:
def test_display_dashes_and_chars_FALSE_1():
    assert display_dashes_and_chars("pythons",[]) == False

def test_display_dashes_and_chars_FALSE_2():
    assert display_dashes_and_chars("p",[' ']) == False

def test_display_dashes_and_chars_TRUE_1():
    assert display_dashes_and_chars("python",['p','y','t','h','o','n']) == True

def test_display_dashes_and_chars_TRUE_2():
    assert display_dashes_and_chars(" ",[' ']) == True

def test_get_random_word_OK():
    assert type(get_random_word()) == str

if __name__ == '__main__':
    pytest.main()
