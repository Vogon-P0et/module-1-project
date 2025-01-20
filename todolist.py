# Paul Jaghab, Coding Temple, January 2025 Cohort

"""Overview

In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

User Interface (UI) and Storage Method
    Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
        The tasks should be stored in a Python list
            Core Features
                Add tasks
                View tasks
                Delete tasks
                Quit the application"""
"""User Interaction
    Use input() to capture user selections and ensure proper input validation to handle invalid choices.
Error Handling
    Implement error handling using try, except, else, and finally blocks to catch errors
        Alert the user if they provide invalid input
        Alert the user if there are no tasks to view
        Alert the user if they try to delete a task that doesn't exist
        Alert the user if they select an option on the main menu that doesn't exist
Code Organization
    Organize your code into functions to improve clarity and maintainability. 
    Use descriptive function names and add comments/docstrings where necessary.
Testing and Debugging
    Thoroughly test your application, considering edge cases such as empty lists and invalid input.
    """
#======================================================================
        
"""I chose a while loop to execute the menu, otherwise I wasn't able to present the user with more than just a single choice and any entries made into the list were not saved into temporary memory"""

# Initiate Program
active = True
tasks = []

while active == True:
    print("\n\nWelcome To Your Coding To-Do List!\n\n")    
    if tasks == []:
        print("You don't have any tasks yet...Let's get started.") 
    else:
        print("Current Tasks:\n")
        for index in range(len(tasks)):
            print(f"{index + 1}. {tasks[index]}") 
        """I felt this functionality of providing the user with the full list at all times was better than having a view task list menu option. This options also displays the tasks, for the sake of continuity, in the same way as the delete selection does."""   

# User Menu
    print("\nPlease select one of the following to continue:\n")
    print("\t1. Add a task")
    print("\t2. Delete a task")
    print("\t3. Quit the Application\n")
    print("You may also type \"quit\" at any time to exit the application\n")
        
    choice = input("Enter your selection: ")

# Input and Error Handling   
    if choice.strip() == "1" or choice.lower().strip() == "add a task":
        task_name = input("\nPlease enter a task into the list: ")
        if task_name.lower().strip() == "quit":
            break
        else:
            tasks.append(task_name)
            print(f"\nThe task \"{tasks[-1]}\" has been successfully added.\n")    
        
    elif choice == "2" or choice.lower().strip() == "delete a task":
            if tasks == []:
                print("There are no list items to delete")
            else:
                print("\nCurrent Tasks:\n")
                for index in range(len(tasks)):
                    print(f"{index + 1}. {tasks[index]}")    #same as above
            try:
                delete_choice = input("\nEnter the number of the task you want to delete: ")
                if delete_choice.lower().strip() == "quit":
                    break
# Convert input to integer and adjust for indexing
                delete_index = int(delete_choice) - 1
                if delete_index >= 0 < len(tasks):
                    deleted_task = tasks.pop(delete_index)
                    print(f"\nThe task \"{deleted_task}\" has been deleted.")
                else:
                    print("\nThat task number doesn't exist. Please try again.")     
            except ValueError:
                print("\nPlease enter a valid number.")
                
#Quit, Break, and Error handling for invalid selections                    
    elif choice == "3":
        active = False
        print("Goodbye!")
    
    elif choice.lower().strip() == "quit": 
        break 
    
    else:
        print("Incorrect selection.\n\nPlease try again.\n") 
  


































