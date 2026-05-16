#!/usr/bin/env python3

tasks = []

program_running = True

while program_running:

    print("\n===== TASK MANAGER =====")
    print("A - Add a task")
    print("V - View tasks")
    print("R - Remove a task")
    print("Q - Quit")

    user_option = input("Choose an option: ").upper()

    match user_option:

        case "A":
            task = input("Enter the task you want to add: ")

            if task == "":
                print("You cannot add an empty task.")
            else:
                tasks.append(task)
                print("Task added successfully.")

        case "V":
            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                print("\nHere are your tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        case "R":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nChoose a task to remove:")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(input("Enter the task number: "))

                    if task_number < 1 or task_number > len(tasks):
                        print("Invalid task number.")
                    else:
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")

                except ValueError:
                    print("Please enter a valid number.")

        case "Q":
            print("Successfully closed.")
            program_running = False

        case _:
            print("Invalid option. Try again.")