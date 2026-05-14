from PIL.ImageOps import posterize
from pyasn1_modules.rfc2985 import signingTime, friendlyName


class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook!! How would you like to proceed?
                               1. Press 1 to signup
                               2. Press 2 to signin
                               3. Press 3 to write a post
                               4. Press 4 to message a friend
                               5. Press any key to exit""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.mypost()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        pwd = input("setup your password here ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your username here ->")
            pwd = input("enter your password here ->")
            if uname == self.username and pwd == self.password:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()


    def mypost(self):
        if self.loggedin == True:
            txt = input("enter your message here ->")
            print(f"Your message is -> {txt}")
        else:
            print("You have not logged in, please signin first to post something")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            msg = input("enter your message here ->")
            frnd = input("enter your friend here ->")
            print(f"your message has been sent successfully TO {frnd}")
            print(f"Your message is -> {msg}")
        else:
            print("You need to signin first to post something")
            print("\n")
            self.menu()

user1 = chatbook()
# obj = chatbook()
