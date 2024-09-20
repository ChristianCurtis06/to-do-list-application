tasks = []

def add_task():
    task_input = input("\nEnter the task you would like to add to your to-do list: ").strip()
    status = "Incomplete"
    task_input = task_input[0].upper() + task_input[1:]
    tasks.append([task_input, status])
    print(f"'{task_input}' added to your to-do list.")

def view_tasks():
    task_num = 1
    print(f"\nYour To-Do List:")
    for item in tasks:
        task, status = item
        print(f"{task_num}. Task: {task}. Status: {status}")
        task_num += 1

def mark_task():
    view_tasks()
    mark_input = int(input("\nEnter which task you completed " + (f"(1-{len(tasks)})" if len(tasks) > 1 else "(1)") + ": "))
    if 1 <= mark_input <= len(tasks):
        tasks[mark_input - 1][1] = "Complete"
        print(f"'{tasks[mark_input - 1][0]}' marked 'Complete'.")
    else:
        raise ValueError("Invalid input. Please enter a number corresponding to a task " + (f"(1-{len(tasks)})" if len(tasks) > 1 else "(1)") + ".")
    
def delete_task():
    view_tasks()
    delete_input = int(input(f"\nEnter which task you want to delete " + (f"(1-{len(tasks)})" if len(tasks) > 1 else "(1)") + ": "))
    if 1 <= delete_input <= len(tasks):
        print(f"'{tasks[delete_input - 1][0]}' deleted from your to-do list.")
        tasks.pop(delete_input - 1)
    else:
        raise ValueError("Invalid input. Please enter a number corresponding to a task " + (f"(1-{len(tasks)})" if len(tasks) > 1 else "(1)") + ".")

print("Welcome to the To-Do List App!")

while True:
    print("\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
    try:
        menu_input = int(input("\nEnter the action you would like to perform (1-5): "))
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
        if "invalid literal" in str(ve):
            print("ValueError: Invalid input. Please enter a positive integer.")
        else:
            print(f"ValueError: {ve}")