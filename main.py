import os # importing os functions
import user_auth # importing the auth handler

def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

username = user_auth.main()
clear_screen()