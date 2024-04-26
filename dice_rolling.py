# Dice Functions

import random
import text as text
import character as oc

def roll_dice():
    """
    Roll dice based on a dice expression (e.g., '3d6' for 3 rolls of a 6-sided dice).
    Allows both lowercase 'd' and uppercase 'D' in the format.
    Defaults to '1d100' if no input is given or input is empty.
    """
    # Ask the user to input the dice roll expression
    expression = input("Enter the dice roll expression (e.g., '3d6'): ").strip()
    
    # Default to '1d100' if no input is provided
    if not expression:
        print("1d100:")
        expression = '1d100'
    
    # Parse the input to extract the number of dice and the number of sides per dice
    try:
        # Split the input on 'd' or 'D' and convert parts to integers
        parts = expression.lower().split('d')
        num_dice, dice_sides = map(int, parts)
    except ValueError:
        # Handle cases where the input is not correctly formatted
        print("Invalid format. Please use the format XdY, where X is the number of dice and Y is the number of sides.")
        return 0
    
    # Roll the dice and collect results
    results = [random.randint(1, dice_sides) for _ in range(num_dice)]
    total = sum(results)
    
    # Display all dice results and the sum
    print(f"Dice rolls: {results}")
    print(f"Sum of rolls: {total}")

    return total


def check_result(character):
    """
    Compare the dice result with a character's stat (e.g., agility, strength).
    """
    skill = input("Enter an item to check (e.g., 力量, 敏捷): ")
    skill = text.translate_key(skill)
    
    if skill not in character.keys():
        print("Error: Skill or attribute not found.\n")
        return

    dice_result = roll_dice()
    if dice_result != 0:
        skill_value = character[skill]
        hard = skill_value // 2
        extreme = skill_value // 5
        critical = 1  # Always 1 for the critical success check
        
        # Determine the success level
        if skill_value >= 50 and dice_result >= 96 or skill_value < 50 and dice_result >= 100:
            result = "大失败"
        elif dice_result <= skill_value:
            if dice_result <= extreme:
                result = "极难"
            elif dice_result <= hard:
                result = "困难"
            elif dice_result == critical:
                result = "大成功"
            else:
                result = "成功"
        else:
            result = "失败"
        
        print(f"Dice roll: {dice_result}")
        print(f"{skill} value: {skill_value}")
        print(f"Result: {result}")
    
    else: print("Error: no dice result.")