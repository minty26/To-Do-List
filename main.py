import os

# Creates an empty to-do list
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)

# Function to remove a task from the list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        display_tasks()
    else:
        print("Task not found in the list.")

# Function to display the to-do list
def display_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen
    if len(to_do_list) == 0:
        print("No tasks in the list")
    else:
        print("Tasks in the list")
        for task in to_do_list:
            print("- " + task)

# Main program loop
while True:
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
        display_tasks()
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
