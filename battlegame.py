def play_game():
    while True:
        print("Game started")
        wizard = "Wizard"
        wizard_hp = 70
        wizard_dmg = 150

        elf = "Elf"
        elf_hp = 100
        elf_dmg = 100

        human = "Human"
        human_hp = 150
        human_dmg = 20

        orc = "Orc"
        orc_hp = 200
        orc_dmg = 30

        dragon = "Dragon"
        dragon_hp = 300
        dragon_dmg = 50

        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("5) Exit")
        choice = input("\nChoose your character ")

        if choice == "1" or choice.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_dmg = wizard_dmg
            break
        if choice == "2" or choice.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_dmg = elf_dmg
            break
        if choice == "3" or choice.lower() == "human":
            character = human
            my_hp = human_hp
            my_dmg = human_dmg
            break
        if choice == "4" or choice.lower() == "orc":
            character = orc
            my_hp = orc_hp
            my_dmg = orc_dmg
            break
        if choice == "5" or choice.lower() == "exit":
            break
        else:
            print("\nUnknown character")    

    if choice == "5" or choice.lower() == "exit":
        print("\nYou have exited the game")

    else:
        print("\nYou have chosen",  character)
        print("Your health is", my_hp)
        print("Your damage is", my_dmg)

        while True:
            dragon_hp = dragon_hp - my_dmg
            print("\nThe", character, "damaged Dragon")
            print("The Dragon's health are now:", dragon_hp)
            if dragon_hp <= 0:
                print("\nThe Dragon lost the battle")
                play_again = input("\nDo you want to play again?\nYes\nNo\n")
                play_again = play_again.lower()
                if play_again == "yes":
                    play_game()
                else:
                    print("\nYou have exited the game")
                break
            my_hp = my_hp - dragon_dmg
            print("\nThe Dragon strikes back at", character)
            print("The", character,"'s health is now", my_hp)
            if my_hp <= 0:
                print("\nThe", character, "has lost the battle")
                play_again = input("\nDo you want to play again?\nYes\nNo\n")
                play_again = play_again.lower()
                if play_again == "yes":
                    play_game()
                else:
                    print("\nYou have exited the game")
                break

play_game()