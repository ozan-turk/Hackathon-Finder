import os # importing os functions
import sys
import user_auth # importing the auth handler
import find_hackathon

def clear_screen(): # function to clear user terminal
    if os.name == "nt": # checking if windows
        _ = os.system("cls") # clear text
    else:
        _ = os.system("clear")

def intro_screen(username): # procedure to display the intro screen
    print(f"Hello {username}, what would you like to do?")
    print("1. Find upcoming hackathons")
    print("2. Logout")
    print("3. Exit program")

def get_intro_input(): # function to get the users input
    while True: # loop that breaks when user enters correct number
        try:
            user_input = int(input(""))
            if 1 <= user_input <= 3:
                return user_input
            else:
                print("Enter a number between 1 and 3")
        except:
            print("Enter a number between 1 and 3")

def main():
    username = user_auth.main() # get username of logged in user
    while True:
        clear_screen()
        intro_screen(username)
        user_input = get_intro_input()
        if user_input == 3:
            clear_screen()
            sys.exit("You chose to exit the program")
        elif user_input == 2:
            clear_screen()
            username = user_auth.main()
        elif user_input == 1:
            clear_screen()
            find_hackathon.main(username)
            

if __name__ == "__main__":
    main()