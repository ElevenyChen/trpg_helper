# Character Management Functions

import re
import dice_rolling as dice
import text as text

class Character:
    def __init__(self, attributes):
        for key, value in attributes.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key, None)  # Return None if the attribute doesn't exist

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def keys(self):
        return set(self.__dict__.keys())

    def __str__(self):
        return '\n'.join(f"{key}: {value}" for key, value in self.__dict__.items())
    

import re

def initialize_character():
    """
    Prompt the user continuously until character data is provided correctly and return a populated dictionary.
    """
    # Start with an empty dictionary
    character_dict = {}

    print("Please paste the character data string [带有调查员姓名的全导入]:")
    
    while True:
        data_str = input().strip()
        if not data_str:
            print("\nNo input provided. Please provide character data.")
            continue  # Keep prompting if no input is provided

        # Regex to extract the name directly after '.st' and a possible space, until the first dash '-'
        name_pattern = r'^\.st\s*(.+?)\s*-\s*'
        name_match = re.search(name_pattern, data_str)
        if name_match:
            character_dict["姓名"] = name_match.group(1).strip()  # Update the name and remove any extra whitespace

            # Remove the name part and process attributes
            attribute_data = re.sub(name_pattern, '', data_str)
            attr_pattern = r"(\D+?)(\d+)"
            attr_matches = re.findall(attr_pattern, attribute_data)

            for key, value in attr_matches:
                key = key.strip()  # Trim whitespace from the attribute name
                if key:  # Check if the key is not empty after trimming
                    character_dict[key] = int(value)
            
            character_dict["hp_og"] = character_dict["体力"]
            character_dict["san_og"] = character_dict["理智"]
            character_dict["mp_og"] = character_dict["魔法"]

            print(f"\nWelcome, {character_dict['姓名']}!")
            break  # Exit loop if input is successfully processed
        else:
            print("\nName format incorrect. Please ensure the format is correct and try again.")
    
    return Character(character_dict)


def check_dic(string, character):
    character


def modify_character(character):
    """
    Modify and update character details during the game.
    Return the modified value!
    """
    # Ask the user for an attribute key they want to modify
    attribute_key = input("Enter the attribute you want to modify: ")
    attribute_key = text.translate_key(attribute_key)

    # Check if the attribute key exists in the character dictionary
    if attribute_key not in character.keys():
        print(f"Error: The attribute '{attribute_key}' does not exist.\n")
        return 0

    # If the attribute exists, offer options for how to modify it
    print("Choose an option for modifying the attribute:")
    print("1. Dice roll")
    print("2. Manually enter a value (e.g., +5 or -3)")
    print("3. Return")

    # Take user input for choice
    choice = input("Enter your choice: ")

    if choice == '1':
        calcutation = input("+ or -?")
        if calcutation != '-' and calcutation != '+':
            print("Invalid input: please enter + or -.")
            return 0
        else:
            # dice roll function
            dice_value = dice.roll_dice()
            character[attribute_key] += dice_value
            print(f"{attribute_key} has been modified by {dice_value} by dice roll: new value is {character[attribute_key]}\n")
            return dice_value
    
    elif choice == '2':
        # Take manual modification input
        modification = input("Enter your modification (+/- number): ")
        try:
            # Convert the string modification into an integer and apply it
            modification_value = int(modification)
            character[attribute_key] += modification_value
            print(f"{attribute_key} has been manually modified by {modification_value}: new value is {character[attribute_key]}\n")
            return modification_value
        except ValueError:
            print("Invalid input: please enter a valid number with + or -.")
            return 0
        

def end_card_check(character):
    """
    Checking character survival.
    """
    # HP check
    if character["体力"] == 0:
        print("该角色目前昏迷/濒死！")
    elif character["体力"] <= (character["hp_og"]/2):
        print("该角色目前重伤")
    
    # MP check
    if character["理智"] == 0:
        print("该角色彻底疯狂！")
    elif character["理智"] < (character["san_og"] - 5) | character["理智"] < (character["san_og"]/5):
        print("该角色可能进入疯狂状态")
    
    print("\n")
    

def print_character(character):
    """
    Nicely format and print a character's details.
    """
    describ = text.description(character)

    # List of attributes to print with their English and Chinese descriptions
    attributes = [
        ("力量 (STR)", describ["力量"]),
        ("体质 (CON)", describ["体质"]),
        ("体型 (SIZ)", describ["体型"]),
        ("敏捷 (DEX)", describ["敏捷"]),
        ("外貌 (APP)", describ["外貌"]),
        ("智力 (INT)", describ["智力"]),
        ("意志 (POW)", describ["意志"]),
        ("教育 (EDU)", describ["教育"]),
        ("幸运 (Luck)", describ["幸运"]),
        ("体力 (HP)", character["hp_og"]),
        ("理智 (San)", character["san_og"]),
        ("魔法 (MP)", character["mp_og"])
    ]

    # Print header
    print("{:<15} | {:<9}| {:<15}".format("属性", "数值", "描述"))
    print("-" * 47)

    # Print each attribute, its English equivalent, and value from the character dictionary
    for attr, des in attributes:
        if character[attr.split()[0]] != None:
            value = character[attr.split()[0]] # Fetch value using the first part of the Chinese key
        else: 
            value = "Error"
        
        print("{:<15} | {:<10} | {:<15}".format(attr, value, des))
