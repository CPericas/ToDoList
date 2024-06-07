#In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. The 
#objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, and error 
#handling while building a practical and interactive application.
completed_tasks = []
incomplete_tasks = []
def add_task():
    new_task = input("What task would you like to add?: ")
    incomplete_tasks.append(new_task)
    print(f"{new_task} has been added to your incomplete tasks.")

def view_tasks():
    print("Incompleted Tasks:")
    for index, do_task in enumerate(incomplete_tasks, start=1):
        print(f"{index}. {do_task}")
    print("Completed Tasks:")
    for index, done_task in enumerate(completed_tasks, start=1):
        print(f"{index}. {done_task}")

def just_completed():
    print("Incompleted Tasks:")
    for index, do_task in enumerate(incomplete_tasks, start=1):
        print(f"{index}. {do_task}")
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if task_num >= 1 and task_num <= len(incomplete_tasks):
            completed_task = incomplete_tasks.pop(task_num - 1)
            completed_tasks.append(completed_task)
            print("Task moved successfully.")
        else:
            print("Invalid task number. No task moved.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Invalid task number. No task moved.")
    print("\nUpdated Incomplete Tasks:")
    for index, do_task in enumerate(incomplete_tasks, start=1):
        print(f"{index}. {do_task}")
    print("\nUpdated Completed Tasks:")
    for index, done_task in enumerate(completed_tasks, start=1):
        print(f"{index}. {done_task}")

def delete_task():
    while True:
        list_choice = input("Enter 'I' to delete from Incomplete Tasks; Enter 'C' to delete from Completed Tasks: ").upper()
        try:
            if list_choice == 'I':
                tasks = incomplete_tasks
                print("\nUpdated Incomplete Tasks:")
                for index, do_task in enumerate(incomplete_tasks, start=1):
                    print(f"{index}. {do_task}")
                break
            elif list_choice == 'C':
                tasks = completed_tasks
                print("\nUpdated Completed Tasks:")
                for index, done_task in enumerate(completed_tasks, start=1):
                    print(f"{index}. {done_task}")
                break
            else:
                raise ValueError("Invalid entry. Please enter 'I' or 'C'.")
        except ValueError as ve:
            print(ve)

    while True:
        try:
            task_number = int(input("Enter the number of the task you'd like to delete: "))
            if task_number >= 1 and task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
                break
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nUpdated Incomplete Tasks:")
    for index, do_task in enumerate(incomplete_tasks, start=1):
        print(f"{index}. {do_task}")
    print("\nUpdated Completed Tasks:")
    for index, done_task in enumerate(completed_tasks, start=1):
        print(f"{index}. {done_task}")


        

while True:
    print("\nWelcome to the To-Do-List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    try:
        choice = input("Enter the number of your choice: ")
    except ValueError:
        print("Please input a number from the menu.")
    if choice == "1":
        add_task()        

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        just_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        break


