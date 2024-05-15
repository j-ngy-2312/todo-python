import os

# List to store tasks
tasks = []

def clear_screen():
    # Clear the console screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("To-Do List Application")
    print("----------------------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    clear_screen()
    print("Your To-Do List:")
    if len(tasks) == 0:
        print("No tasks added.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    input("\nPress Enter to return to the menu...")

def add_task():
    clear_screen()
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")
    input("\nPress Enter to return to the menu...")

def delete_task():
    clear_screen()
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
