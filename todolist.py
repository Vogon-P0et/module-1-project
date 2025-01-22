# Paul Jaghab, Coding Temple, January 2025 Cohort


def show_tasks():
    print("Current Tasks:\n")
    for index in range(len(tasks)):
        print(f"\t{index + 1}. {tasks[index]}") 

def add_tasks():
    task_name = input("\nPlease enter a task into the list: ")
    if task_name.lower().strip() == "quit":
        print("Goodbye!")
        active = False
    else:
        tasks.append(task_name)
        print(f"\nThe task \"{tasks[-1]}\" has been successfully added.\n") 

def del_tasks():
    delete_choice = input("\nEnter the number of the task you want to delete: ")
    if delete_choice.lower().strip() == "quit":
        print("Goodbye!")
        active = False    
    try:
        delete_index = int(delete_choice) - 1
        if delete_index >= 0 < len(tasks):
            deleted_task = tasks.pop(delete_index)
            print(f"\nThe task \"{deleted_task}\" has been deleted.")
    except IndexError:
            print("\nThat task number doesn't exist. Please try again.")     
            
active = True
tasks = []

while active == True:
    print("\n\nWelcome To Your Coding To-Do List!\n\n")    
    if tasks == []:
        print("You don't have any tasks yet...Let's get started.") 
    else:
        show_tasks() 

    print("\nPlease select one of the following to continue:\n")
    print("\t1. Add a task")
    print("\t2. Delete a task")
    print("\t3. Quit the Application\n")
    print("You may also type \"quit\" at any time to exit the application\n")
        
    choice = input("Enter your selection: ")
 
    if choice.strip() == "1" or choice.lower().strip() == "add a task":
        add_tasks()
    elif choice == "2" or choice.lower().strip() == "delete a task":
            if tasks == []:
                print("There are no list items to delete")
            else:
                show_tasks()
            try:
                del_tasks()    
            except ValueError:
                print("\nPlease enter a valid number.")                 
    elif choice == "3":
        print("Goodbye!")
        active = False
    elif choice.lower().strip() == "quit": 
        active = False
    else:
        print("\n\t\t\*Incorrect selection. Please try again\*\n") 
  


































