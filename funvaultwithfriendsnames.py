import time

# Color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

print("🔐 WELCOME TO THE ULTRA TOP SECRET VAULT 🔐")
print("NOTE: You only get 3 tries. Use them wisely 😈")
print("")

name = input("Enter a name: ").title()
access_code = input("Enter code: ")

todo_list = [None]
robots = [None]
missions = []
tries = 1

while True:
    if name in ["Hella", "Fatema", "Claire"] and access_code == "37654":
        print("\nChecking credentials...")
        time.sleep(2)
        print("\n🔓------------------------------------------🔓")
        print(f"\nACCESS GRANTED TO {name.upper()}. Security Cleared ")
        tries = 0

        # Fatema Menu
        if name == "Fatema":
            while True:
                print("\n------- 🔥🤬💥❤️‍🔥😠️‍🔥😡💢❤️‍🔥 WELCOME FATEMA ❤️‍🔥🤬💥😠🔥😡❤️‍🔥💢🔥 ---------")
                print("1: Add task to your to do list")
                print("2: View your to do list ")
                print("3: Mark tasks as undone ")
                print("4: Mark tasks as done")
                print("5: Remove tasks from to do list")
                print("6: View your secret missions")

                input_f = input("Choose what you want to do (1/2/3/4/5/6) 'q' to quit : ").lower()

                if input_f == "1":
                    task = input("Enter task you would like to add: ")
                    print("😤 Adding....")
                    time.sleep(2)
                    todo_list.append(task)
                    print(f"{RED}Your task {CYAN}({task}){RED} has been added!{RESET}")

                elif input_f == "2":
                    print("❤️‍🔥 Searching....")
                    time.sleep(2)
                    print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                    if all(task is None for task in todo_list):
                        print("🚫 NOTHING HERE YET 🚫")
                    else:
                        for i, task in enumerate(todo_list):
                            if task is not None:
                                print(f"{i}.♦️ {RED}{task}{RESET}")

                elif input_f == "3":
                    try:
                        undone_index = int(input("Which task number is undone? "))
                        if 0 < undone_index < len(todo_list) and todo_list[undone_index] is not None:
                            todo_list[undone_index] = f"{RED}[UNDONE] {todo_list[undone_index]}{RESET}"
                            print("Marking....")
                            time.sleep(2)
                            print(f"Marked as {RED}UNDONE{RESET}!")
                        else:
                            print("Invalid Task number.")
                    except ValueError:
                        print("Enter a valid number.")

                elif input_f == "4":
                    print("🔥 Searching....")
                    time.sleep(2)
                    print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                    for i, task in enumerate(todo_list):
                        if task is not None:
                            print(f"{i}.♦️ {task:<20}")
                    print("-------------------------------------")
                    try:
                        done_index = int(input("Which task number is done? "))
                        if 0 < done_index < len(todo_list) and todo_list[done_index] is not None:
                            todo_list[done_index] = f"[DONE] {todo_list[done_index]}"
                            print("Marking....")
                            time.sleep(2)
                            print(f"Marked as {RED}DONE{RESET}!")
                        else:
                            print("Invalid Task number.")
                    except ValueError:
                        print("Enter a valid number.")

                elif input_f == "5":
                    task = input("Enter task you would like to remove: ")
                    print("💢 Removing....")
                    time.sleep(2)
                    try:
                        todo_list.remove(task)
                        print(f"{RED}Your task {CYAN}({task}){RED} has been removed!{RESET}")
                    except ValueError:
                        print("Task not found.")
                elif input_f == "6":
                    print('')
                    print("\n🕵️‍♀️🗝️ SEARCHING FOR SECRET MISSIONS....")
                    time.sleep(2)
                    print('')
                    if len(missions) == 0:
                        print("🫢 NO SECRET MISSIONS YET...")
                    else:
                        print("\n🚨 TOP SECRET MISSIONS 🚨")
                        for i, mission in enumerate(missions):
                            print(f"{i + 1}. 🧩{RED}{mission}{RESET}")
                    add_more = input("Want to add a new secret mission? yes/no: ").lower()
                    if add_more == "yes":
                        new_mission = input("Enter your new mission: ")
                        missions.append(new_mission)
                        print("💾 Saving mission...")
                        time.sleep(2)
                        print(f"{RED}Mission '{CYAN}{new_mission}{RED}' has been added to your vault{RESET} 🗃️")

                elif input_f == "q":
                    sure = input("Are u sure you want to leave? yes/no: ").lower()
                    if sure == "yes":
                        print("\nLogging off...")
                        time.sleep(2)
                        print("❤️‍🔥💢🔥 YOU HAVE SUCCESSFULLY LOGGED OUT ❤️‍🔥💢🔥")
                        break

        # Hella Menu
        elif name == "Hella":
            while True:
                print("\n------- 🤖⚡🧠🤓📚📖🧐🎓 WELCOME HELLA 🧠📚📖🧐🎓⚡🤖 ---------")
                print("1: Add task to your to do list")
                print("2: View your to do list ")
                print("3: Add a new robot ")
                print("4: Mark tasks as undone ")
                print("5: Mark tasks as done")
                print("6: Remove tasks from to do list")
                print("7: View all your robots")
                print("8: View your secret missions")
                input_h = input("Choose what you want to do (1/2/3/4/5/6/7/8) 'q' to quit : ").lower()

                if input_h == "1":
                    task = input("Enter task you would like to add: ")
                    print("🧐 Adding....")
                    time.sleep(2)
                    todo_list.append(task)
                    print(f"{BLUE}Your task {CYAN}({task}){BLUE} has been added!{RESET}")

                elif input_h == "2":
                    print("📖 Searching....")
                    time.sleep(2)
                    print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                    if all(task is None for task in todo_list):
                        print("🚫 NOTHING HERE YET 🚫")
                    else:
                        for i, task in enumerate(todo_list):
                            if task is not None:
                                print(f"{i}.🔹 {BLUE}{task}{RESET}")

                elif input_h == "3":
                    print("🧠 Finding....")
                    time.sleep(2)
                    print("\n🤖✨🔧 WELCOME TO THE ROBOT CREATION STATION 🤖✨🔧")
                    robot = input("Enter the new robot name: ")
                    robots.append(robot)
                    print(f"🚨🧠🤖 {BLUE}Your robot {CYAN}({robot}){BLUE} has been added!{RESET} 🚨🧠🤖")

                elif input_h == "4":
                    print("📚 Searching....")
                    time.sleep(2)
                    print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                    for i, task in enumerate(todo_list):
                        if task is not None:
                            print(f"{i}.🔹 {task:<20}")
                    try:
                        undone_index = int(input("Which task number is undone? "))
                        if 0 < undone_index < len(todo_list) and todo_list[undone_index] is not None:
                            todo_list[undone_index] = f"{BLUE}[UNDONE] {todo_list[undone_index]}{RESET}"
                            print("Marking....")
                            time.sleep(2)
                            print(f"Marked as {BLUE}UNDONE{RESET}!")
                        else:
                            print("Invalid Task number.")
                    except ValueError:
                        print("Enter a valid number.")

                elif input_h == "5":
                    print("🤓 Searching....")
                    time.sleep(2)
                    print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                    for i, task in enumerate(todo_list):
                        if task is not None:
                            print(f"{i}.🔹 {task:<20}")
                    try:
                        done_index = int(input("Which task number is done? "))
                        if 0 < done_index < len(todo_list) and todo_list[done_index] is not None:
                            todo_list[done_index] = f"[DONE] {todo_list[done_index]}"
                            print("Marking....")
                            time.sleep(2)
                            print(f"Marked as {BLUE}DONE{RESET}!")
                        else:
                            print("Invalid Task number.")
                    except ValueError:
                        print("Enter a valid number.")

                elif input_h == "6":
                    task = input("Enter task you would like to remove: ")
                    print("🗂️ Removing....")
                    time.sleep(2)
                    try:
                        todo_list.remove(task)
                        print(f"{BLUE}Your task {CYAN}({task}){BLUE} has been removed!{RESET}")
                    except ValueError:
                        print("Task not found.")

                elif input_h == "7":
                    print("🧐 Searching....")
                    time.sleep(2)
                    print("\n🤖 ---------- YOUR ROBOTS ---------- 🤖")
                    for r in robots:
                        if r is not None:
                            print(f"{BLUE}🤖 {r}{RESET}")
                    print("--------------------------------------")
                elif input_h == "8":
                    print('')
                    print("\n🕵️‍♀️🗝️ SEARCHING FOR SECRET MISSIONS....")
                    time.sleep(2)
                    print('')
                    if len(missions) == 0:
                        print("🫢 NO SECRET MISSIONS YET...")
                    else:
                        print("\n🚨 TOP SECRET MISSIONS 🚨")
                        for i, mission in enumerate(missions):
                            print(f"{i + 1}. 🧩 {BLUE}{mission}{RESET}")
                    add_more = input("Want to add a new secret mission? yes/no: ").lower()
                    if add_more == "yes":
                        new_mission = input("Enter your new mission: ")
                        missions.append(new_mission)
                        print("💾 Saving mission...")
                        time.sleep(2)
                        print(f"{BLUE}Mission '{CYAN}{new_mission}{RESET}'{BLUE} has been added to your vault{RESET} 🗃️")


                elif input_h == "q":
                    sure = input("Are u sure you want to leave? yes/no: ").lower()
                    if sure == "yes":
                        print("\nLogging off...")
                        time.sleep(2)
                        print("🤖🧠📚 YOU HAVE SUCCESSFULLY LOGGED OUT 🧠📚🤖")
                        break
        if name == "Claire":
                while True:
                    print("\n------- 🌸🎀🦩🎀🪞🩰🕯️😇🌷 WELCOME CLAIRE 🌸🎀🪞🩰🕯️🎀🦩😇🌷 ---------")
                    print("1: Add task to your to do list")
                    print("2: View your to do list ")
                    print("3: Mark tasks as undone ")
                    print("4: Mark tasks as done")
                    print("5: Remove tasks from to do list")
                    print("6: View your secret missions")
                    input_c = input("Choose what you want to do (1/2/3/4/5/6) 'q' to quit : ").lower()

                    if input_c == "1":
                        task = input("Enter task you would like to add: ")
                        print("🌸 Adding....")
                        time.sleep(2)
                        todo_list.append(task)
                        print(f"{YELLOW}Your task {CYAN}({task}){YELLOW} has been added!{RESET}")

                    elif input_c == "2":
                        print("😇 Searching....")
                        time.sleep(2)
                        print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                        if all(task is None for task in todo_list):
                            print("🚫 NOTHING HERE YET 🚫")
                        else:
                            for i, task in enumerate(todo_list):
                                if task is not None:
                                    print(f"{i}.✨ {YELLOW}{task}{RESET}")

                    elif input_c == "3":
                        try:
                            undone_index = int(input("Which task number is undone? "))
                            if 0 < undone_index < len(todo_list) and todo_list[undone_index] is not None:
                                todo_list[undone_index] = f"{YELLOW}[UNDONE] {todo_list[undone_index]}{RESET}"
                                print("Marking....")
                                time.sleep(2)
                                print(f"Marked as {YELLOW}UNDONE{RESET}!")
                            else:
                                print("Invalid Task number.")
                        except ValueError:
                            print("Enter a valid number.")

                    elif input_c == "4":
                        print("🌷 Searching....")
                        time.sleep(2)
                        print("\n📋🔑 ---------- TO DO LIST ---------- 📝✨")
                        for i, task in enumerate(todo_list):
                            if task is not None:
                                print(f"{i}.✨️ {task:<20}")
                        print("-------------------------------------")
                        try:
                            done_index = int(input("Which task number is done? "))
                            if 0 < done_index < len(todo_list) and todo_list[done_index] is not None:
                                todo_list[done_index] = f"[DONE] {todo_list[done_index]}"
                                print("Marking....")
                                time.sleep(2)
                                print(f"Marked as {YELLOW}DONE{RESET}!")
                            else:
                                print("Invalid Task number.")
                        except ValueError:
                            print("Enter a valid number.")

                    elif input_c == "5":
                        task = input("Enter task you would like to remove: ")
                        print("🌸 Removing....")
                        time.sleep(2)
                        try:
                            todo_list.remove(task)
                            print(f"{YELLOW}Your task {CYAN}({task}){YELLOW} has been removed!{RESET}")
                        except ValueError:
                            print("Task not found.")
                    elif input_c == "6":
                        print('')
                        print("\n🕵️‍♀️🗝️ SEARCHING FOR SECRET MISSIONS....")
                        time.sleep(2)
                        print('')
                        if len(missions) == 0:
                            print("🫢 NO SECRET MISSIONS YET...")
                        else:
                            print("\n🚨 TOP SECRET MISSIONS 🚨")
                            for i, mission in enumerate(missions):
                                print(f"{i + 1}. 🧩 {YELLOW}{mission}{RESET}")
                        add_more = input("Want to add a new secret mission? yes/no: ").lower()
                        if add_more == "yes":
                            new_mission = input("Enter your new mission: ")
                            missions.append(new_mission)
                            print("💾 Saving mission...")
                            time.sleep(2)
                            print(f"{YELLOW}Mission '{CYAN}{new_mission}{RESET}'{YELLOW} has been added to your vault {RESET}🗃️")
                    elif input_c == "q":
                        sure = input("Are u sure you want to leave? yes/no: ").lower()
                        if sure == "yes":
                            print("\nLogging off...")
                            time.sleep(2)
                            print("🎀🪞🩰 YOU HAVE SUCCESSFULLY LOGGED OUT 🎀🪞🩰")
                            break

        break

    # DENIED ACCESS CASES
    elif name not in ["Hella", "Fatema", "Claire"] and access_code != "37654":
        print("\nChecking credentials...")
        time.sleep(2)
        print(f"\nACCESS DENIED!!! 🔁 ATTEMPT {tries}/3")
        print("🔒--------------------------------🔒")
        tries += 1
        if tries >= 4:
            print("🚨 SECURITY ALERTED 🚨 NO FURTHER ATTEMPTS POSSIBLE.")
            break
        name = input("Enter a name: ").title()
        access_code = input("Enter code: ")

    elif name not in ["Hella", "Fatema", "Claire"] and access_code == "37654":
        print("\nChecking credentials...")
        time.sleep(2)
        print(f"\nYOU ARE GOING TO DIE WHO GAVE YOU THE CODE??? 🔁 ATTEMPT {tries}/3.")
        print("🔒--------------------------------🔒")
        tries += 1
        if tries >= 4:
            print("🚨 SECURITY ALERTED 🚨 NO FURTHER ATTEMPTS POSSIBLE.")
            break
        name = input("Enter a name: ").title()
        access_code = input("Enter code: ")

    elif name in ["Hella", "Fatema", "Claire"] and access_code != "37654":
        print("\nChecking credentials...")
        time.sleep(2)
        print(f"\nGURLLLLLLLLL DON'T TELL ME YOU FORGOT THE CODE! 🔁 ATTEMPT {tries}/3.")
        print("🔒--------------------------------🔒")
        tries += 1
        if tries >= 4:
            print("🚨 SECURITY ALERTED 🚨 NO FURTHER ATTEMPTS POSSIBLE.")
            break
        name = input("Enter a name: ").title()
        access_code = input("Enter code: ")

    else:
        print("ACCESS DENIED: Unauthorized entry.")
        break
