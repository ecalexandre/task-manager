#task manager
program_running = True
option_not_choosen = True
option_1_choosed = False
option_2_choosed = False
option_3_choosed = False
option_4_choosed = False 

Task_list = []

while program_running:
     if option_not_choosen:
          print("Hello! here is your list of options for your tasks below:")
          print(f"A -Add a task")
          print("")
          print(f"V -View task list")
          print("")
          print(f"R -Remove a task")
          print("")
          print(f"Q -Quit")


     while option_not_choosen:
          print('')
          user_option = input("Enter your option here: ")
          print("")
          if user_option == "A" or user_option == "a":
               option_not_choosen = False
               option_1_choosed = True
        
          elif user_option == "V" or user_option == "v":
               option_not_choosen = False
               option_2_choosed = True
        
          elif user_option == "R" or user_option == "r":
               option_not_choosen = False
               option_3_choosed = True
        
          elif user_option == "Q" or user_option =="q":
               option_not_choosen = False
               option_4_choosed = True
               program_running = False
               print("Sucessfully closed")

          else:
              print("This is not an option, try again")

     
     #option 1
     if option_1_choosed:
        while program_running and option_1_choosed:
               user_task_added = input("Add your tasks here: ")
               
               Task_list.append(user_task_added)
               
               if len(user_task_added) >= 0:
                  print(f"{user_task_added} succesfully added")  
                  option_1_choosed = False
                  option_not_choosen = True


     #option 2
     if option_2_choosed:
          print("Here is your task list:")
          if len(Task_list) == 0:
               print("Nothing was added to the list")
               option_2_choosed = False
               option_not_choosen = True
          
          else:
             for index, user_task_added in enumerate(Task_list, start=1):
               print(f"{index}. {user_task_added}")
             
             while option_2_choosed:
                 option_2_choosed = False
                 option_not_choosen = True
                 break
     
     #option 3
     if option_3_choosed:
        if len(Task_list) == 0:
          print("Nothing was added to the list")
          option_3_choosed = False
          option_not_choosen = True
        
        else:
           print(f"Choose a task in the list to remove")
           
           for index, user_task_added in enumerate(Task_list, start=1):
               print(f"{index}. {user_task_added}")
           
           removing_tasks_input = input("Remove a task: ")

           try:
              task_number_removed = int(removing_tasks_input)

              while program_running and option_3_choosed:
                  if task_number_removed > len(Task_list) or task_number_removed < 1:
                     print("Invalid task number")
                  
                  else:
                    
                    removed_task = Task_list.pop(task_number_removed -1)
                    print(f"Removed task: {removed_task}")
                    option_3_choosed = False
                    option_not_choosen = True
           
           except ValueError:
               print("Please enter a valid number")
               option_3_choosed = False
               option_not_choosen = True    

