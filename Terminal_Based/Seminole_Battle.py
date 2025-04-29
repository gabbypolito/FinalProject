from classes import *
import random

crossbow = Weapon("crossbow", 10, 8, 15)
sword = Weapon("sword", 15, 10, 5)
shield = Weapon("shield", 7, 15, 10)

while True:
    difficulty = input("1. Easy\n2. Medium\n3. Hard\n\nChoose a Difficulty: ")

    if difficulty == "1" or "Easy" or "easy":
        player = Character(60)
        seminole = Enemy(50, 1)
        break

    elif difficulty == "2" or "Medium" or "medium":
        player = Character(50)
        seminole = Enemy(55, 15)
        break

    elif difficulty == "3" or "Hard" or "hard":
        player = Character(40)
        seminole = Enemy(60, 20)
        break

    else:
        print("Not a valid option.")
        print()

print()
print("OH NO, Alberta was kidnapped by the Seminoles. Albert has hired you to save her.")

while True:
    print()
    weapon_choice = input("1. crossbow\n2. sword\n3. shield\n\nChoose a Weapon for Your Battle: ")

    if weapon_choice == "1" or "crossbow":
        weapon = crossbow
        break

    elif weapon_choice == "2" or "sword":
        weapon = sword
        break

    elif weapon_choice == "3" or "shield":
        weapon = shield
        break

    else:
        print("Not a valid option.(No capitals)")

print()
print(
    "You and Albert have reached the Seminole hide out and you must fight off the THE(singular) Seminole Indian while Albert frees Alberta.")
print()
print(f"THE Seminole Indian has {seminole.health} health.")
print(f"You have {player.health} health.")
while (seminole.health > 0) and (player.health > 0):
    print()
    attack = input("Do you wish to attack?(Y/N) ")
    print()

    if attack == "y" or "Y":
        damage_to_player = random.choice(range(seminole.attack)) + (seminole.attack - weapon.defense)
        damage_to_enemy = random.choice(range(weapon.attack)) + weapon.attack

        possible_miss = random.choice(range(weapon.speed + 1))
        if possible_miss == 0:
            damage_to_enemy = 0
            print("Uh oh, you missed")
        player.take_damage(damage_to_player)
        seminole.take_damage(damage_to_enemy)
        player.set_health(player.health)
        seminole.set_health(seminole.health)

        print(f"THE Seminole Indian dealt {damage_to_player} damage, so you now have {player.health} health.")
        print(f"You dealt {damage_to_enemy} damage with your {weapon}, so THE Seminole Indian now has {seminole.health} health.")

    elif attack == "n" or "N":
        print("You do nothing. But why? Why would you do that?")
        damage_to_player = random.choice(range(seminole.attack)) + (seminole.attack - weapon.defense)
        player.take_damage(damage_to_player)
        player.set_health(player.health)

        print(f"You took {damage_to_player} damage, so you now have {player.health} health. Not the smartest decision.")

    else:
        print("""Just say "Y" or "N".""")
        continue

    if seminole.health <= 0:
        if player.health <= 0:
            print()
            print(
                "Well, Albert has saved Alberta. And You will be remembered as a legend of the University of Florida.")
            print("\nThe Warrior's Ending")
            break
        print()
        print("""GOOD JOB, YOU DID IT, YOU'RE AWESOME. Albert has saved Alberta.
But QUICK, you guys have been find out. Find you're way out of the hideout.""")     # This leads into the pygame

    elif player.health <= 15:
        if player.health <= 0:
            print()
            print("Well, did Albert save Alberta? Probably, but you will never know. An early end has come for you.")
            print("\nThe Bad Ending")

        else:
            print()
            run = input("Your health is getting low. Do you wish to run?(Y/N) ")
            print()

            if run == "y" or "Y":
                print("Wow. Pretty messed up. I know you only had " + str(player.health), "health, but still.")
                print("Well, you run away and never see Albert and Alberta again. UF has deemed you a traitor.")
                print("\nThe Unsatisfying Ending")
                break

            elif run == "n" or "N":
                print("Very brave. Very admirable. You keep on fighting.")