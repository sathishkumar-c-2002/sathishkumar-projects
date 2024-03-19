class To_do_list:
    def __init__(self):
        self.tasks = []                         #empty list created
        
    def adding_task(self):
        task = input("Enter your Task:  ")
        self.tasks.append(task)                 #join the task to list
        print(f"{task} is add to the list")
    
    def delete_task(self):
        task = input("Enter your Task:  ")
        self.tasks.remove(task)                 #delete the task to list
        print(f"{task} is removed from the list")
        
    def mark_the_task_done(self):
        task = input("Mention the Task to be done:  ")
        if task in self.tasks:
            print(f"{task} is done")            # Make the task done
            self.tasks.remove(task)             # Remove task from the list
        else:
            print(f"{task} is not found in the list")
    
    def display_task(self):
        if self.tasks:
            print("TO DO LIST")
            for i,task in enumerate(self.tasks, start= 1):  #count the task from 1
                print(f"{i}. {task}")           #i is orderlist
        else:
            print("List is Empty.")

def main():
    to_do_list = To_do_list()
    while True:
        print("\n  Welcome to the To do list")
        print("1.   Add Task")
        print("2.   Delete Task")
        print("3.   Mark the Task done")
        print("4.   Display All Tasks")
        print("5.   Quit")
        
        choice = input("Enter your Choice:  ")
        if choice == '1':
            to_do_list.adding_task()                
        elif choice == '2':
            to_do_list.delete_task()                
        elif choice == '3':
            to_do_list.mark_the_task_done()
        elif choice == '4':
            to_do_list.display_task()
        elif choice == '5':
            break
        else:
            print("Enter valid Choice...")
            
if __name__ == '__main__':
    main()
            

        
            
        

