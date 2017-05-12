# Importing assets
import cat_left
import cat_right

# Error handling variable
err = print("Your selection hasn't worked")

# Help section
def help():
    print("     Welcome to more_ascii_art help!      ")
    print("Usage: ")
    print("       1. Build the library with $ pip install -e .")
    print("       2. Use the python shell to $ import more_ascii_art")
    print("       3. Type in print and then the build name and then the function you wish to execute")
    print("            Like this: $ print more_ascii_art.help()")
    print("Commands: ")
    print("       1. help() - Displays this help message")
    print("Upcoming Features: ")
    print("       1. Support for PyPI")
    print("       2. A CAT")

# User selection and processing    
def selection():
    print("Please note that selections are case sensitive...")
    print("Here are the selections you can choose from: ")
    print("1. cat_left ")
    print("2. cat_right ")
    user_input = input("Please type in your selection: ")
    
    if (user_input == "cat_left"):
        print cat_left()
    else:
        print err
        
    if (user_input == "cat_right"):
        print cat_right()
    else:
        print err
