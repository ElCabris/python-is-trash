"""
    Object Oriented Programming
    - University of Medellin - UdeM
    - Students: [Emanuel Cabrera, Miguel Cardenas]
    - Date: 2024-02-14
"""

import os
import consolemenu as cmd
from consolemenu import *
from consolemenu.items import *

# Function to get all subdirectories within a directory
def get_subdirectories(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

# Function to get all script files within a directory
def get_scripts_in_directory(directory):
    return sorted([f for f in os.listdir(directory) if f.endswith('.py')])

# Function to create a submenu for exercises in a directory
def create_submenu(directory):
    submenu = cmd.ConsoleMenu(directory, "Subdirectory of exercises")
    scripts = get_scripts_in_directory(directory)
    for script in scripts:
        script_path = os.path.join(directory, script)
        submenu.append_item(FunctionItem(script, run_script, [script_path]))
    return submenu

# Function to run the selected script
def run_script(script_path):
    try:
        os.system('python {}'.format(script_path))
    except Exception as e:
        print("Error:", e)
    input("Press Enter to return to the menu...")

# Main function to create the menu
def main():
    exercises_path = './exercises/'  # Assuming the main exercises folder is in the same directory as the script
    menu = cmd.ConsoleMenu("Object Oriented Programming", "University of Medellin - UdeM")
    subdirectories = get_subdirectories(exercises_path)
    for subdir in subdirectories:
        submenu = create_submenu(os.path.join(exercises_path, subdir))
        menu.append_item(SubmenuItem(subdir, submenu, menu))
    menu.show()

if __name__ == "__main__":
    main()

