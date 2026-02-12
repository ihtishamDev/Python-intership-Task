import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name  # Store file name inside object
        self.tasks = []
        self.load_tasks()


    def generate_id(self):
        if not self.tasks:
            return 1
        return max(task.get('id', 0) for task in self.tasks) + 1



    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_task(self):
        with open(self.file_name , "w") as file:
            json.dump(self.tasks, file , indent=4)

    def add_tasks(self,title,description ):
        

        task = {
            "id":self.generate_id(),
            "title": title,
            "description": description,
            "status": "pending",
            "created_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.tasks.append(task)
        self.save_task()
        print("Task Added Successfully.\n")   

    def list_task(self):
        if not self.tasks:
            print("No task will be available.\n")   
            return
        
        for index, task in enumerate(self.tasks, start=1):
            status = task["status"].capitalize()
            # print(f"[{task['id']}] {index}. title: {task['title']} --- status: {status}")
            print(f"[{task['id']}] title: {task['title']} --- status: {status}")

            print(f"   Description: {task['description']}")
            print(f"   Created At: {task['created_at']}\n")



    def mark_task_completed(self):
        self.list_task()

        if not self.tasks:
            return

        try:
            task_id = int(input("Enter the ID of the task you want to complete: "))
        except ValueError:
            print("Please enter a valid number only!\n")
            return

        for task in self.tasks:
            if task['id'] == task_id:
                task["status"] = "completed"
                self.save_task()
                print("Task completed successfully!\n")
                return

        print("Task ID not found.\n")
            
        # except ValueError:
        #     print(" Please enter a valid number only!\n")


        # try:
        #     task_number = int(input("Enter task number you want to mark: "))
        #     if 1 <= task_number <= len(tasks):     # use condition for user clearifing only write number
                
        #         tasks[task_number-1]["completed"] = True  
        #         print(" Task marked as completed!\n")
        #         save_task()
        #     else:
        #         print("Invalid number enter the task number in the list ... ")
        # except ValueError:
        #         print(" Please enter a valid number only!\n")
    

def main():
    manager = TaskManager()
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. List Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter the option (1-4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_tasks(title,description)
        elif choice == "2":
            manager.list_task()
        elif choice == "3":
            manager.mark_task_completed()
        elif choice == "4":
            print("Good BYE!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":     # it's nessary to run the program
   
    main()
