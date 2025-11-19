to_do_list = []

def show_menu():
    print("To-Do List Menu")
    print("1. Add a task")
    print("2. View Task")
    print("3. Exit")

choice = ""

while choice != "3":
    show_menu()
    choice = input("Enter your choice (1-3)")

    if choice == "1":
        task = input("Enter a new task")
        to_do_list.append(task)
        print("Task added")
    elif choice == "2":
        print("Your Tasks")
        for task in to_do_list:
            print("- ", task)
    elif choice == "3":
        print("Goodbye")
    else:
        print("Invalid choice, please try again.")














