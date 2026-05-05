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
          print(f"- Add a task (Enter A to choose this option)")
          print("")
          print(f"- View task list (Enter V to choose this option)")
          print("")
          print(f"- Remove a task (Enter R to choose this option)")
          print("")
          print(f"- Quit (Enter Q to choose this option)")


     while option_not_choosen:
          print('')
          user_option = input("Enter your option here: ")
          print("")
          if user_option == "A":
               option_not_choosen = False
               option_1_choosed = True
        
          elif user_option == "V":
               option_not_choosen = False
               option_2_choosed = True
        
          elif user_option == "R":
               option_not_choosen = False
               option_3_choosed = True
        
          elif user_option == "Q":
               option_not_choosen = False
               option_4_choosed = True
               program_running = False
               print("Sucessfully closed")

          elif user_option != "Q" or user_option != "V" or user_option != "R" or user_option != "A":
                print("This is not an option, try again")

     
     #option 1
     if option_1_choosed:
        while program_running and option_1_choosed:
               user_task_added = input("Add your tasks here (Type 'done' if you are done with adding tasks): ")
               Task_list.append(user_task_added)
               if user_task_added == "done":
                  Task_list.remove("done")
                  option_1_choosed = False
                  option_not_choosen = True
                  display_list = Task_list              

     #option 2
     if option_2_choosed:
          print("Here is your task list:" if len(Task_list) > 0 else "")
          print(display_list if len(Task_list)> 0 else "Nothing is in the list")
          print("Type 'finished viewing' if you're done viewing the list")
          while option_2_choosed:
               user_finished_viewing = input()
               if user_finished_viewing == "finished viewing":
                  option_2_choosed = False
                  option_not_choosen = True
                  break
               else:
                  print("Type 'finished viewing' if you're done viewing the list")
     
     #option 3
     if option_3_choosed:
        print("Choose a task in the list to remove" if len(Task_list)> 0 else "Nothing was added to the list")
        print('')
        while program_running and option_3_choosed:
              removing_tasks = input("Remove a task (Type 'finished removing' if you're done): ")
              if removing_tasks in Task_list:
                 Task_list.remove(removing_tasks)
              elif removing_tasks == "finished removing" and removing_tasks not in Task_list:
                  option_3_choosed = False
                  option_not_choosen = True
              elif removing_tasks not in Task_list:
                   print("This task is not in the list")
