import sys, random
def main():
    mainMenu()
print('Greetings, Dungeon Master, this is my D&D script made for aiding in combat and rolls in general.')
print('Use me wisely and report any bugs to Pedro')
print('So, let\'s get started. shall we?')
def mainMenu():
    print('What would you like me to do?')
    print('For combat type 1, for saving throws type 2, to shut me down type 3')
    gMasterMenu = input()
    if gMasterMenu == '3':
        print('See you later, Dungeon Master!')
        sys.exit() # This ends the program
    if gMasterMenu == '1':
        print('Sharp your blade and get your scrolls, combat to death shall it be!')
        while True:  # This is the main loop of the attacking action
            print('What is the target Armor Class?')
            a_c = int(input())
            print('What is the to hit bonus from the attacker?')
            attack_roll = random.randint(1, 20)
            to_hit_value = int(input())
            if attack_roll + to_hit_value > a_c: # This compares the roll and bonus value to the AC of the target
                print('Target hit!')
            elif attack_roll + to_hit_value < a_c:
                print('The attack missed the mark!')
            print('Type 1 to attack again, type 2 to go back to the main menu')
            if input() == '2':
                main()  # This takes the user back to the main options
    if gMasterMenu == '2':
        print('Uh uh, hope you\'re not doing a CON save with 1 HP already.')
        while True:
            saving_roll = random.randint(1, 20)
            print('What is the saving throw DC?')
            saving_roll_dc = int(input())
            print('What is the saving roll bonus?')
            saving_roll_bonus = int(input())
            if saving_roll + saving_roll_bonus > saving_roll_dc:
                print('The character succeeded the saving throw!')
            elif saving_roll + saving_roll_bonus < saving_roll_dc:
                print('The character failed the saving roll!')
            print('Type 1 to roll again or 2 to go back to the main menu')
            if input() == '2':
                main()  # This takes the user back to the main options
        mainMenu()
main()
