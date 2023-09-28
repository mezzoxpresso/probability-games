import random
import time
from game_typing import gameTyping

def initializer():
    welcome_message()
    #ask_for_bet()
    game_redirector(ask_for_game())

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
    print(f"These are the games we have now!")
    for x in game_list:
        print(f"{game_list.index(x)+1}. {x}\n")
    y = input("Please enter the number of the game you want to play")
    return y

def game_redirector(y):
    if int(y) == 1:
        gameTyping.game_start()
    else:
        print(type(y))
        print("bug")




if __name__ == "__main__":
    initializer()