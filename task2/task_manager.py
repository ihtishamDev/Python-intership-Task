tasks = []

def add_tasks():
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    task = {
        "title": title,
        "description": description,
        "completed": False       #if we use "Ture" then it by default show task completed
    }

    tasks.append(task)
    print("Task Added Successfully.\n")   

def list_task():
    if not tasks:
        print("No task will be available.\n")   
        return
    
    for index, task in enumerate(tasks, start=1):   #using enumerate for task number .. like 1,2,3
        status = "Completed" if task["completed"] else "Pending"  
        print(f"{index}. title: {task['title']} --- status : {status}")
        print(f"   Description: {task['description']}\n") 


def mark_task_completed():
    list_task()

    if not tasks:
        return
    try:
        task_number = int(input("Enter task number you want to mark: "))
        if 1 <= task_number <= len(tasks):     # use condition for user clearifing only write number
            
            tasks[task_number-1]["completed"] = True  
            print(" Task marked as completed!\n")
        else:
            print("Invalid number enter the task number in the list ... ")
    except ValueError:
            print(" Please enter a valid number only!\n")
 

def main():
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. List Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter the option (1-4): ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            list_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("Good BYE!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":     # it's nessary to run the program
    main()
