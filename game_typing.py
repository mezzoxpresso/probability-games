import random
import time

class gameTyping(object):
    def __init__(self):
        pass

    @classmethod    
    def typing_game(self):
        test_words = ["Pseudopseudohypoparathyroidism", "Incomprehensibilities", "Honorificabilitudinitatibus", "subdermatoglyphic", "Sesquipedalianism"]
        word = random.choice(test_words)
        print(f"Please type {word} correctly")
        player_word = input()
        while word != player_word:
            print(f"Wrong! Type {word} correctly!")
            player_word = input()
        print("You are correct!")

    @staticmethod
    def calculate_time():
        start_time = time.time()
        gameTyping.typing_game()
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"You took about {time_taken} seconds to type the word")
