'''A simple command shell written in Python'''
import os

def confirm_exit():
    while True:
        confirmation = input("Are you sure you want to exit? (Y/N): ")
        if confirmation.upper() == "Y":
            print("Exiting the shell...")
            return True
        elif confirmation.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def main():
    while True:
        command = input("Enter a command (LIST, ADD, HELP, EXIT): ")
        if command == "LIST":
            list_directory()
        elif command == "ADD":
            add_numbers()
        elif command == "HELP":
            display_help()    
        elif command == "EXIT":
            if confirm_exit():
                break
        else:
            print("Invalid command. Type 'HELP' to see the available commands.")

# the command LIST will lists the contents of the current directory
def list_directory():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    for file in files:
        print(file)

# The ADD command adds two numbers from user input together and provides the result
def add_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break # break out of the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter integers only")
            
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
            
# the HELP command displays all the available commands
def display_help():
    print("Available commands:")
    print("LIST - Lists the contents of the current directory")
    print("ADD - Adds two numbers together and provides the result")
    print("HELP - Provides a list of commands available")
    print("EXIT - Exits the shell")

if __name__ == "__main__":
    main()
    
