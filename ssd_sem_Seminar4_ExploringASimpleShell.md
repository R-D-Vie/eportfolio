# Exploring a simple shell in python

[You can see my solution in my GitHub repository, here.](https://github.com/R-D-Vie/SecureSoftwareDevelopment/blob/e9ec731d9894e24ea85d7aef024b7af01055f3fd/Python_Practice/Simple_Shell.py)

This document will outline security issues and solutions.

1. What are the two main security vulnerabilities with your shell?
- Privileges: the shell I have made runs with the privileges of the user executing it - if an attacker gets access to the shell via a user with elevated privileges, they could access sensitive data.
- Lack of input sanitization: an attacker may be able to inject malicious commands unless the input is validated and sanitized.

3. What is one recommendation you would make to increase the security of the shell?
- Input validation and sanitization should be implemented:
  - restrict the length of user input to prevent buffer overflow or DOS attacks.
  - sanitize user input by removing or neutralizing potentially harmful characters, such as escape sequences or shell metacharacters.
  - escape or properly handle special characters to prevent unintended command execution or shell interpretation.
  - check that user input matches the expected format.
  
5. Provide (pseudo)code examples of changes you would make to the shell to improve its security.


Restrict the length of user input for commands and restrict to letters only:
```python
# function to check whether a given string consists only of alphabetic characters:
def is_letters_only(input_string):
    return all(ch.isalpha() for ch in input_string)

def main():
    while True:
        command = input("Enter a command (letters only, max 4 characters): ")[:4]
        # check if input is letters only
        if not is_letters_only(command):
          print("Invalid input. Letters only.")
          continue
          
 ```
            
 Sanitize user input by removing or neutralizing potentially harmful characters, such as escape sequences or shell metacharacters:
 ```Python
import re

#...

def sanitize_input(input_string):
  # remove/ neutralise potentially harmful characters
  sanitized_string = re.sub(r'[;&|`<>$!]', '', input_string)
    return sanitized_string
  
  def main():
    while True:
        command = input("Enter a command (max 4 characters): ")[:4]
        sanitized_command = sanitize_input(command)

        if command != sanitized_command:
            print("Invalid input. Removed potentially harmful characters.")
            continue
            
        if sanitized_command == "LIST":
            list_directory()
        elif sanitized_command == "ADD":
            add_numbers()
        elif sanitized_command == "HELP":
            display_help()
        elif sanitized_command == "EXIT":
            if confirm_exit():
                break
        else:
            print("Invalid command. Type 'HELP' to see the available commands.")
 # ...
            
 ```
 
 Escape or properly handle special characters to prevent unintended command execution or shell interpretation:
 ```Python
import shlex

#...

def sanitize_input(input_string):
    # Remove or neutralize potentially harmful characters
    sanitized_string = input_string.replace(';', '').replace('&', '').replace('|', '')
    sanitized_string = sanitized_string.replace('<', '').replace('>', '').replace('$', '')
    sanitized_string = sanitized_string.replace('!', '').replace('`', '')
    return sanitized_string

def main():
    while True:
        command = input("Enter a command (max 4 characters): ")[:4]
        sanitized_command = sanitize_input(command)

        if command != sanitized_command:
            print("Invalid input. Removed potentially harmful characters.")
            continue
            
        if sanitized_command == "LIST":
            list_directory()
        elif sanitized_command == "ADD":
            add_numbers()
        elif sanitized_command == "HELP":
            display_help()
        elif sanitized_command == "EXIT":
            if confirm_exit():
                break
        else:
            print("Invalid command. Type 'HELP' to see the available commands.")
#...

```


 
 
  
