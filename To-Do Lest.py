message = """
==>What do yoy think 
1- Add tasks 
2- Show tasks
3- Mark task as done
4- Exit"""

Tasks = []

while True :
    print("\n=====> To-Do List <=======")
    print(message)
    choice = int(input())
    
    if choice == 1 :
        print("-"*30)
        print('====> Add Tasks') 
        n_task = int(input("How many task you want to add: "))
        
        for i in range(n_task):
            task = input("please,Enter your task ")
            Tasks.append({"task":task,"done":False})
            print("Task added!")
    
    elif choice == 2 :
        print("-"*30)
        print('====> Show your task') 
        
        for i , task in enumerate(Tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['task']} - {status}")
        
    elif choice == 3:
        print("-"*30)
        print('====> Show your task') 
        task_index = int(input("Enter the task number to mark as done: ")) - 1
       
        if 0 <= task_index < len(Tasks):
            Tasks[task_index]["done"] = True
            print("Task marked as done!")
        
        else:
            print("Invalid task number.")
        
    elif choice == 4 :
            print("Exiting the To-Do List.")
            break

    else:
        print("Invalid choice. Please try again.")
          
