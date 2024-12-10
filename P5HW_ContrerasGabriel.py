# Gabriel
# 19NOV2024
# P5HW
# Character Creation Game

import random
import time

def create_character():
    character = {
        "name": input("Enter the character's name: "),
        "health": int(input("Enter the character's health: ")),
        "hp": int(input("Set character's starting HP: ")),
        "mushroom": int(input("Enter the number of mushrooms the character has: "))
    }
    return character

def display_menu():
    print("\nChoose an action to keep battle going...")
    print("******************************************")
    print("1. Battle")
    print("2. Display Characters")
    print("3. Exit Game")
    while True:
        try:
            userChoice = int(input("Enter your choice (1-3): "))
            if 1 <= userChoice <= 3:
                return userChoice
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def display_character(character):
    print(f"\nCharacter Status:")
    print("------------------")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

def sim_battle(character1, character2):
    print("\n***********CARNAGE BEGINS****************")
    
    # Randomly assign attacker and victim
    if random.choice([True, False]):
        attacker, victim = character1, character2
    else:
        attacker, victim = character2, character1
    
    # Calculate and apply damage
    damage = random.randint(0, attacker["hp"])
    print(f"\n{attacker['name']} attacks {victim['name']} and deals {damage} damage!")
    victim["health"] = max(0, victim["health"] - damage)  # Ensure health doesn't go below 0
    
    # Add HP to attacker
    hp_increase = random.randint(1, 5)
    attacker['hp'] += hp_increase
    
    print("🧨🧨🧨🧨🧨🧨")
    time.sleep(2)  # Reduced sleep time for better game flow
    print(f"{attacker['name']} gained {hp_increase} HP points")
    print(f"{victim['name']}'s health is now {victim['health']}")
    
    return character1, character2

def main():
    print("Welcome to Battle Royale!")
    print("----------------------------")
    
    # Create initial characters
    print("\nCreate First Character:")
    character1 = create_character()
    print("\nCreate Second Character:")
    character2 = create_character()
    
    # Main game loop
    while character1['health'] > 0 and character2['health'] > 0:
        userChoice = display_menu()
        
        if userChoice == 1:
            character1, character2 = sim_battle(character1, character2)
        elif userChoice == 2:
            display_character(character1)
            display_character(character2)
        elif userChoice == 3:
            print("\nExiting game...")
            break
    
    # Game over sequence
    print("\n🎮 GAME OVER 🎮")
    print("Final Status:")
    display_character(character1)
    display_character(character2)
    
    # Announce winner
    if character1['health'] <= 0:
        print(f"\n🏆 {character2['name']} is victorious! 🏆")
    elif character2['health'] <= 0:
        print(f"\n🏆 {character1['name']} is victorious! 🏆")

if __name__ == "__main__":
    main()
