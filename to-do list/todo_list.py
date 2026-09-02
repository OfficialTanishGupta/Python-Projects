todo = []

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    val = input("Choose an option: ")

    if val == "1":
        if not todo:
            print("Your list is empty.")
        else:
            result = 1
            for task in todo:
                print(result, "-", task)
                result = result + 1

    elif val == "2":
        task = input("Enter new task: ")
        todo.append(task)
        print("Task added.")

    elif val == "3":
        if not todo:
            print("No tasks to delete.")
        else:
            result = 1
            for task in todo:
                print(result, "-", task)
                result = result + 1

            num = input("Enter task number to delete: ")
            idx = int(num) - 1

            if 0 <= idx < len(todo):
                todo.pop(idx)
                print("Task deleted.")
            else:
                print("Invalid number.")

    elif val == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
