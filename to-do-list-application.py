tasks = []

def add_task():
    task_input = input("Enter the task you would like to add to your to-do list: ").capitalize()
    status = "Incomplete"
    tasks.append([task_input, status])
    print(f"'{task_input}' added to your to-do list.")

def view_tasks():
    print(f"To-Do List:\n{tasks}")

def mark_task():
    view_tasks()
    mark_input = int(input(f"Enter which task you completed (1-{len(tasks)}): "))
    if 1 <= mark_input <= len(tasks):
        tasks[mark_input[1]] = "Complete"
    else:
        raise ValueError(f"Invalid input. Please enter a number corresponding to a task (1-{len(tasks)}).")
def delete_task():
    delete_input = int(input(f"Enter which task you want to delete (1-{len(tasks)}): "))
    if 1 <= delete_input <= len(tasks):
        tasks.pop(delete_input)
        print(f"'{tasks[delete_input[0]]}' deleted from your to-do list.")
    else:
        raise ValueError(f"Invalid input. Please enter a number corresponding to a task (1-{len(tasks)}).")

print("Welcome to the To-Do List App!")

while True:
    print("\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
    try:
        menu_input = int(input("Enter the action you would like to perform (1, 2, 3, 4, or 5): "))
        if menu_input == 1:
            add_task()
        elif menu_input == 2:
            if len(tasks) >= 1:
                view_tasks()
            else:
                print("Your to-do list is empty.")
        elif menu_input == 3:
            if len(tasks) >= 1:
                mark_task()
            else:
                print("Your to-do list is empty.")
        elif menu_input == 4:
            if len(tasks) >= 1:
                delete_task()
            else:
                print("Your to-do list is empty.")
        elif menu_input == 5:
            print("Quitting the app...")
            break
        else:
            raise ValueError("Invalid input. Please enter a number corresponding to an action (1-5).")
        
    except ValueError as ve:
        if "invalid literal" in ve:
            print("ValueError: Invalid input. Please enter a number.")
        else:
            print(f"ValueError: {ve}")

# Task 6: Testing and Debugging


# Task 8: Optional Features
