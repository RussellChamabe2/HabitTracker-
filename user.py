
# This class is about how the user would likely function. 


class User:
    #Constructor method where __init__ is another word for User class and Self is used as a reference for a class object(user1) when called in the main class
    def __init__(self):
        self.displayname = ""
        self.user_tasks = []
        self.user_tasksrecords = []

    # Greeting user. self is used here because we used user1 to call this method 
    def GreetUser(self):
        while True:
            self.displayname = input("Enter your display name: ").strip()

            if len(self.displayname) == 0:
                print("Your name cannot be empty. Please enter a valid name.")
            else:
                break

            
       

# Creating task's that the user will have to enter
    def CreateTasks(self):
        # Creates a loop that is making sure the user adds a number
        while True: 
            numberOfTasks =(input("Ok " + self.displayname + ", please enter the amount of tasks you would like to create: "))
            # if the user enters a string or a different type of data type. it will not work
            if numberOfTasks.strip() == "": 
                print("No tasks was created")
                break

            try:
                numberOfTasksINT = int(numberOfTasks)

            except ValueError:
                print("Invalid input. Please enter a valid integer!")
                continue

            # A for loop that uses the number from numTasks2 to determine the amount of times it loops
            for x in range(numberOfTasksINT):
            # Each iteration the user adds their task. append allows us to add value into the array
                userInputtedTasks = input("Enter a task you would like here: ")
                self.user_tasks.append(userInputtedTasks)
            
            print("Here is the your list of Habits", self.user_tasks)
            break
    
    # Allows the user to remove or create their tasks
    def UpdateTasks(self):
        if not self.user_tasks:
                print("\n-------------------------------------")
                print("You do not have any habits for this")
                print("-------------------------------------")
                return
        print("\nHello this is the Adding/Removing Tasks Menu")
        print("Here is you current Tasks!")
        print(self.user_tasks)
        # A loops that loops until the user has done either Add or Remove 
        while True:  
            updateChoice = input("write ""Add"" to add a new task or write ""Remove"" to delete a task: ")

            # If user typed "Add" they can add a task. Loop will break/stop and then prints the current Tasks below
            if updateChoice == "Add":
                self.user_tasks.append(input("Enter a task you would like here: "))
                break

            # If user typed "Remove" they can choose an index of their list to remove.        
            elif updateChoice == "Remove":
                selectedUserEleDelete = (input("Enter a number you would like to delete here: "))
                # Checks if the user didnt enter a value/number if they did the loop will end
                if selectedUserEleDelete.strip() == "":
                        print("You didn't delete anything")
                        break
                try:
                        #Program tries to convert the user input into integer 
                        index = int(selectedUserEleDelete)
                        if 0 <= index - 1: # if 0 is less than (index - 1)
                            self.user_tasks.pop(index-1)
                except ValueError:
                    # This only runs if the user entered an String or any other data type othr than integer. It will print and contiune the loop
                    print("Invalid input. Please enter a valid integer.")
                    continue
            
            # it will print the updated list
            print("\nHere is your updated Tasks", self.user_tasks)
            break 



    # Function where the user can see their habits and if they have completed it or not
    def ShowHabits(self):
            if not self.user_tasks:
                print("\n-------------------------------------")
                print("You do not have any habits for this")
                print("-------------------------------------")
                return
        # Implementing pandas to allow us to use its library and analyse data. So here we use Dataframe to display the data
            import pandas as pd
        
            days = [f"Day {i}" for i in range(1, 8)]
            df = pd.DataFrame(index=days)
        

            for habit in self.user_tasks:
                df[habit] = "Not Completed"  # empty cells for now
        
            print(df)






        
        
            
            







                            


    


    



