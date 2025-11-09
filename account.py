import sqlite3 # importing SQL function

def create_connection(): # creating connection to be used
    return sqlite3.connect("user_credentials.db") # define connection, creates if not present

def initialise_table(connection): # initialising table if not existent within the db
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)""")

def get_username(): # getting username
    return input("Enter your username: ").strip()

def get_password(): # getting user pw
    return input("Enter your password: ").strip()

def form_type(): # getting user's desired authorisation
    while True: # loop that breaks when user enters correct auth type
        user_input = input("Would you want to Register or Log in? (R/L)? ").strip().upper()
        if user_input == "R" or user_input == "L":
            return user_input # break loop
        else:
            print("Try again")

def login(username, password, connection): # function to use passed in credentials to see if the account exists in the db, returning results
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_pw = cursor.fetchone() # get results
    if user_pw: # if there are results, username was found
        if user_pw[0] == password: # if the password found is the same as user input, return true
            print("Password correct")
            return True
        else: # else return false
            print("Incorrect password")
            return False
    else: # if no user was found on the db
        print("User not found")
        return False

def register(username, password, connection): # function to be used to create account in db with passed in credentials
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user: # checking if username is already in use
        print("Username already in use")
        return False
    else: # else create the account and commit
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        connection.commit()
        print("Account made")
        return True

connection = create_connection()
initialise_table(connection)
access_gained = False

while access_gained == False:
    form_type = form_type()
    if form_type == "R":
        username = get_username()
        password = get_password()
        access_gained = register(username,password,connection)
    else:
        username = get_username()
        password = get_password()
        access_gained = login(username,password,connection)
    print("")
connection.close()