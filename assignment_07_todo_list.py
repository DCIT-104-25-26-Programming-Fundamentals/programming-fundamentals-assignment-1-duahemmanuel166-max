def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n============================")
    print("     TO-DO LIST MENU        ")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """
    Prompts the user for a task description and adds it to the list.
    """
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task description cannot be empty.")


def view_tasks(tasks):
    """
    Displays all tasks currently in the list with 1-based indexing.
    """
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    """
    Shows the current tasks and allows the user to remove one by its number.
    """
    if not tasks:
        print("\nYour to-do list is empty! Nothing to delete.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number. Please try again.")
    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()