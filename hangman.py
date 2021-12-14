import random
word_list = ["apple", "banana", "car", "cat", "horse", "nowhere", "shut", "up", "you", "nice", "moon", "sun"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("TFCSARSS Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Schreibe einen Buchstaben oder ein ganzes Wort: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Du hast es schon versucht: ", guess, "!")
            elif guess not in word:
                print(guess, "Ist nicht das Wort")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Gut gemacht ,", guess, " ist in dem Wort!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Du hast es schon versucht: ", guess, "!")
            elif guess != word:
                print(guess, " ist nicht das Wort :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Falsches Zeichen, Nur Buchstaben!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Gut gemacht!")
    else:
        print("Endschuldigung deine Züge sind vorbei. Das Wort war: " + word + ". Vielleicht nächstes mal!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Nochmal? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

main()