todo_list = [None]

print("WELCOME TO YOUR TO DO LIST!")
print("---------------------------------")
print(f"{'1: Add a task':^30}")
print(f"{'2: View tasks':^30}")
print(f"{'3: Mark tasks as done':^38}")
print(f"{'4: Mark a task as undone':^40}")
print("----------------------------------")

userinput = input("Enter: 1/2/3/4: ")

while True:
    if userinput == "1":
        task = input("Enter your task: ")
        todo_list.append(task)
        print(f"Your task ({task}) has been added!")
        userinput = input("Enter: 1/2/3/4 (q to quit): ")
    elif userinput == "2":
        print("------TO DO LIST------")
        for i, task in enumerate(todo_list):
            if task is not None:
                print(f"{i}: {task:<20}")
        print("-----------------------")
        userinput = input("Enter: 1/2/3/4 (q to quit): ")
    elif userinput == "3":
        print("-------TO DO LIST-------")
        for i, task in enumerate(todo_list):
            if task is not None:
                print(f"{i}: {task:<20}")
        print("-------------------------")
        try:
            done_index = int(input("Which task number is done?"))
            if 0 < done_index < len(todo_list) and todo_list[done_index] is not None:
                todo_list[done_index] = f"[DONE] {todo_list[done_index]}"
                print("Marked as done!")
            else:
                print("Invalid Task number.")
        except ValueError:
            print("Enter a valid number.")
        userinput = input("Enter 1/2/3/4 (q to quit): ")
    elif userinput == "4":
        print("--------TO DO LIST---------")
        for i, task in enumerate(todo_list):
            if task is not None:
                print(f"{i}: {task:<20}")
        try:
            undone = int(input("Which task is undone?"))
            if 0 < undone < len(todo_list) and todo_list[undone] is not None:
                todo_list[undone] = f"[UNDONE]{todo_list[undone]}"
                print("Marked as Undone!")
            else:
                print("Invalid Task number.")
        except ValueError:
            print("Enter a valid number.")
        userinput = input("Enter 1/2/3/4 (q to quit): ")
    elif userinput.lower() == "q":
        break

print("------------------------------------")
print("Goodbye <3!")
print("Thank you for using TO DO LIST!")
