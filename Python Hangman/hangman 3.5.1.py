HANGMAN_ASCII_ART = ("""Welcome to the game Hangman
...   _    _
...  | |  | |
...  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
...  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
...  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
...  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
...                       __/ |
...                      |___/
														""")
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print("Tries: ", MAX_TRIES)

player_letter_choice = input("Guess a letter: ")
print(player_letter_choice.lower())