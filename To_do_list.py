# Project Name : 
print("To-Do-List")
tasks = []
while True :
    print("\nWhat you want to do from the following options?")
    # Options :
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")
    # User's choice :
    choice = input("Enter your choice number (1,2,3,4) : ")
    # Conditions :
    if choice == "1" :
        task = input("Enter your task : ")
        tasks.append(task)
        print("Task added successfully !")
    elif choice == "2" :
        if not tasks :
            print("You have no tasks yet ! ")
        else :
            for number , task in enumerate(tasks , start = 1) :
                print(f"{number}. {task}")
    elif choice == "3" :
        if not tasks :
            print("You have no tasks to delete ! ")
            continue
        print("Your tasks : ")
        for number , task in enumerate(tasks , start = 1) :
            print(f"{number}. {task}")
        try :
            task_number = int(input("Enter the task number to delete : "))
        except ValueError :
            print("Please enter a number ! ")
            continue
        if 1 <= task_number <= len(tasks):
            index = task_number - 1
            tasks.pop(index)
            print("Task deleted successfully !")
        else :
            print("Invalid task number ! ")
    elif choice == "4" :
        print("Goodbye!")
        break # Stop 
    else :
        print("Invalid Choice ! ")
