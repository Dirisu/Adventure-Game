import time
import random

weapons = ['sword', 'knife', 'wood']
armour = random.choice(weapons)
enemies = ['Dragon', 'Wolf', 'Thanos']
evil = random.choice(enemies)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# this is the start of the game


def intro(armour, evil):
    print_pause("Hello! Welcome to the world of ADVENTURE!!!")
    print_pause("Pack your bags and lets get started")
    print_pause(".")
    print_pause("...")
    print_pause("You're standing in a field with 2 boxes in front of you")
    print_pause("The first is a red box")
    print_pause("The second is a yellow box")


# the select_card function is called here to validate the player's input


def valid_input(armour, evil):
    while True:
        print_pause("Which of the boxes will you like to pick?")
        response = input("Please pick the red or yellow box\n").lower()
        if response == "red":
            print_pause("You've selected the key to your adventure")
            print_pause("Box opens; now pick a card")
            select_card(armour, evil)
        elif response == "yellow":
            print_pause("Amazing!!! you're now on a rescue mission")
            print_pause(".")
            print_pause("...")
            woman(armour, evil)
        else:
            print("You made an error")
        return valid_input(armour, evil)


# the fight1 and fight2 function are called here


def select_card(armour, evil):
    while True:
        card = input(f"1. Fight with {evil}\n"
                     "2. Scared? Run for your life\n").lower()
        if card == "1":
            fight_1(armour, evil)
        elif card == "2":
            fight_2(armour, evil)
        else:
            print_pause("you made an error")
        return select_card(armour, evil)


# Chance to replay or exit game


def restart_end(armour, evil):
    while True:
        print_pause("would you like to replay or exit")
        restart = input("1. Replay\n"
                        "2. Exit\n")
        if restart == "1":
            print_pause("restarting")
            game(armour, evil)
        elif restart == "2":
            print_pause("Game Over")
            exit(0)
        else:
            break
        restart_end(armour, evil)


# the card function is called here


def fight_1(armour, evil):
    card1(armour, evil)
    restart_end(armour, evil)


def fight_2(armour, evil):
    card2(armour, evil)
    restart_end(armour, evil)


def card1(armour, evil):
    print_pause(f"{evil} attacks you")
    print_pause(f"you only have a {armour} to fight back")
    if "sword" in armour:
        print_pause("you fight tirelessly")
        print_pause(f"Woah! you defeated {evil}")
        print_pause("Congratulations, Your adventure is successful")
    elif "knife" in armour:
        print_pause(f"you try to overpower {evil}")
        print_pause("but your strength is not enough")
        print_pause("you pick up a severe injury")
        print_pause("looks like you cannot continue the adventure")
        print_pause("what would you want to do?")
        print_pause("...")
    elif "wood" in armour:
        print_pause("that is a very weak weapon")
        print_pause(f"{evil} overpowers you")
        print_pause("Sorry, You're defeated")
        print_pause("Here's where your adventure ends")
    return restart_end(armour, evil)


def card2(armour, evil):
    while True:
        print_pause("you walk into the field")
        print_pause("unfortunately, there's no where else to go")
        print_pause("please go back to the entrance and"
                    " pick the right box for your adventure")
        return valid_input(armour, evil)


def action_1(armour, evil):
    print_pause("you just saved a life")
    print_pause("Congratulations, Your adventure is successful")
    print_pause("You can Replay or Exit")
    restart_end(armour, evil)


def action_2(armour, evil):
    print_pause("That's so ruthless")
    print_pause(f"you just got eaten by {evil}")
    print_pause("You failed in your adventure")
    print_pause("You can Replay or Exit")
    restart_end(armour, evil)


# this is executed when player chooses the yellow card option


def woman(armour, evil):
    print_pause("Here's a woman laying lifeless")
    print_pause("What would you want to do?")
    action = input("1. Help the woman\n"
                   "2. Not sympathetic? Walk away\n").lower()
    if action == "1":
        action_1(armour, evil)
        restart_end(armour, evil)
    elif action == "2":
        action_2(armour, evil)
        restart_end(armour, evil)
    else:
        print_pause("Wrong input")
    woman(armour, evil)


def game(armour, evil):
    weapons = ['sword', 'knife', 'wood']
    armour = random.choice(weapons)
    enemies = ['Dragon', 'Wolf', 'Thanos']
    evil = random.choice(enemies)
    intro(armour, evil)
    valid_input(armour, evil)
    select_card(armour, evil)


game(armour, evil)
