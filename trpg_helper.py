import character as oc
import dice_rolling as dice

def main_menu():
    """
    Display the main menu and handle user input.
    """
    print("Welcome to the TRPG Helper!\n")
    oc.Character = oc.initialize_character()
    while True:
        print("1. My Character")
        print("2. Check!")
        print("3. Quick Dice")
        print("4. Manage Characters")
        choice = input("Choose an option: ")
        if choice == "1":
            oc.print_character(oc.Character)
        if choice == "2":
            dice.check_resuilt(oc.Character)
        elif choice == "3":
            dice.roll_dice()
        elif choice == "4":
            oc.modify_character()
        elif choice == "24":
            print("Battle tool not implemented yet, sorry.\n")

        else:
            print("Invalid option. Please try again\n.")
        oc.end_card_check(oc.Character)
            

if __name__ == "__main__":
    main_menu()
