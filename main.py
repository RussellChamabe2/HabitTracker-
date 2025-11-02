# from the user.py file we can use/import the objects in the User class 
from user import User


class Main:

    #Creating class object to gain data of User class. So right now user1 has all the data of User Class
    user1 = User()

    #user1 calls GreetUser function which is in the User Class
    user1.GreetUser()

    # Create a Menu for users to select, which repeats until they want to Quit
    while True:  #ignore #allows the program to keep running until user selects 
        print("\nMenu") # \n means print at a new line
        print("1. Create tasks")
        print("2. Add/Remove tasks")
        print("3. Show tasks")
        #print("3. Show Full Table")
        print("4. Quit")
        

        choice = input("Choose an option please: ")

        if choice == "1":
            #user1 calls CreateTasks function which is in the User Class
            user1.CreateTasks()
        elif choice == "2":
            user1.UpdateTasks()
        elif choice == "3":
            user1.ShowHabits()
        elif choice == "4":
            print("See you next time!")
            break
        else:
            print("Invaild option, please try again!")




    


