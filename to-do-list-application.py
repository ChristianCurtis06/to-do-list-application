from colorama import init, Fore, Style
init(autoreset = True)

tasks = []

def add_task():
    task_input = input("\nEnter the task you would like to add to your to-do list: ").strip()
    if task_input:
        task_input = task_input[0].upper() + task_input[1:]
    else:
        raise ValueError("Invalid input. Please enter a valid task.")
    priority_input = input("Enter the task priority (low, moderate, high): ").strip()
    if priority_input.lower() == "low":
        priority = Fore.CYAN + "Low"
    elif priority_input.lower() == "moderate":
        priority = Fore.YELLOW + "Moderate"
    elif priority_input.lower() == "high":
        priority = Fore.RED + "High"
    else:
        raise ValueError("Invalid input. Please enter a valid priority (low, moderate, high).")
    status = Fore.RED + "Incomplete"
    tasks.append([task_input, status, priority])
    print(f"'{task_input}' with '{priority}" + Fore.WHITE + "' priority added to your to-do list.")

def view_tasks():
    task_num = 1
    print(f"\nYour To-Do List:")
    for item in tasks:
        task, status, priority = item
        print(f"{task_num}. Task: {task}. Status: {status}" + Fore.WHITE + f". Priority: {priority}" + Fore.WHITE + ".")
        task_num += 1

def mark_task():
    view_tasks()
    mark_input = int(input("\nEnter which task you completed " + (f"(1-{len(tasks)})" if len(tasks) > 1 else "(1)") + ": "))
    if 1 <= mark_input <= len(tasks):
        tasks[mark_input - 1][1] = Fore.GREEN + "Complete"
        print(f"'{tasks[mark_input - 1][0]}' marked '" + Fore.GREEN + "Complete" + Fore.WHITE + "'.")
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

print(Style.BRIGHT + "Welcome to the To-Do List App!")

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