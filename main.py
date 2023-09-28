import random
import time
from game_typing import gameTyping

def initializer():
    welcome_message()
    #ask_for_bet()
    ask_for_game()

    gameTyping.calculate_time()

def welcome_message():
    print("---------------------------------------------------------")
    casino_names=["Baloney's", "Griselda's", "Chimmney's", "Grave's", "Gravy's"]
    casino_description = ["Cheesy", "Floppy", "Gravy", "Groovy", "Grimy"]
    casino_location = ["Boat", "Mountain", "Dune", "Hidey-Hole"]
    print(f"Welcome to {random.choice(casino_names)} {random.choice(casino_description)} Gaming Den")

def ask_for_bet():
    deposit = input("How much do you want to deposit?")
    print (f"You have successfully deposited ${deposit}")
    return deposit

def ask_for_game():
    game_list = ["Typing Game"]
    input(f"Which game do you want to play? \n We have {game_list} now")






if __name__ == "__main__":
    initializer()