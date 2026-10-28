"""A simple menu-based task tracker with JSON persistence."""

import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from tasks.json, or return an empty list if it is missing/invalid."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read tasks.json. Starting with an empty task list.")
        return []

    if not isinstance(tasks, list):
        print("tasks.json does not contain a valid task list. Starting empty.")
        return []

    return tasks


def save_tasks(tasks):
    """Save the current task list to tasks.json."""
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Unable to save tasks: {error}")


def add_task(tasks):
    """Ask for a title and add a new pending task."""
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Display all tasks with their current status."""
    if not tasks:
        print("No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done", False) else "Pending"
        print(f"{number}. {task.get('title', 'Untitled')} [{status}]")


def get_task_number(tasks, action):
    """Return a zero-based task index after validating user input."""
    if not tasks:
        print(f"No tasks to {action}.")
        return None

    try:
        number = int(input("Task number: ").strip())
    except ValueError:
        print("Please enter a valid task number.")
        return None

    if number < 1 or number > len(tasks):
        print("Task number is out of range.")
        return None

    return number - 1


def complete_task(tasks):
    """Mark a selected task as done."""
    index = get_task_number(tasks, "complete")
    if index is None:
        return

    if tasks[index].get("done", False):
        print("That task is already done.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Delete a selected task."""
    index = get_task_number(tasks, "delete")
    if index is None:
        return

    deleted_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {deleted_task.get('title', 'Untitled')}")


def display_menu():
    """Display the available menu choices."""
    print("\n--- TASK TRACKER ---")
    print("1. Add   2. View   3. Complete   4. Delete   5. Exit")


def main():
    """Run the task tracker until the user chooses Exit."""
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
