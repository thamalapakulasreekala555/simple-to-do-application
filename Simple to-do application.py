import os
import time
def print_options():
    print("-- TO-DO LIST APP --")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Remove all tasks")
    print("5. Edit a task")
    print("6. Exit")

def create_file(file_name):
    final_file = f'{file_name}.txt'
    if os.path.exists(final_file):
        print("[*] Open File...")
        time.sleep(1)
    else:
        with open(final_file, "w") as file:
            pass  # create an empty file
        print(f"[*] {file_name}.txt is being created...")
        print("[+] YOUR FILE SUCCESSFULLY CREATED!")
    return final_file


def add_task(final_file):
    with open(final_file, "r") as file:
        info = file.readlines()
        last_task_number = int(info[-1].split(".")[0]) if info else 0
    number_task = int(input("Enter the number of tasks: "))
    with open(final_file, "a") as file:
        for i in range(last_task_number + 1, last_task_number + number_task + 1):
            task = input(f"{i}. Enter the task: ").strip().lower()
            while not task:
                print("[!] Enter a valid task!")
                task = input(f"{i}. Enter the task: ").strip().lower()
            file.write(f'{i}. {task}\n')
    time.sleep(1)
    print("[+] Tasks added.")


def remove_task(final_file):
    with open(final_file, "r") as file:
        info = file.readlines()
        print("".join(info))
        task_to_remove = input("Enter the task to remove: ").strip().lower()
    filtered_info = [task for task in info if not task.lower().startswith(task_to_remove)]
    if len(filtered_info) != len(info):
        with open(final_file, "w") as file:
            file.write("".join(filtered_info))
        print("[-] Task removed.")
    else:
        print("[!] Task not found.")


def list_tasks(final_file):
    with open(final_file, "r") as file:
        info = file.read()
        print(info)


def remove_all_tasks(final_file):
    with open(final_file, "w") as file:
        file.write("")
    print("[-] All tasks removed.")


def edit_task(final_file):
    with open(final_file, "r") as file:
        info = file.readlines()
        print("".join(info))
        task_to_edit = input("Enter the task to edit: ").strip().lower()
    for i, task in enumerate(info):
        if task.lower().startswith(task_to_edit):
            new_task = input("Enter the new task: ").strip().lower()
            info[i] = f"{task.split('.')[0]}. {new_task}\n"
            with open(final_file, "w") as file:
                file.write("".join(info))
            print("[+] Task edited.")
            break
    else:
        print("[!] Task not found.")


if __name__ == "__main__":
    os.system('cls')
    file_name = input("Enter the file name: ").strip()
    while not file_name:
        print("[!] Enter a valid file name!")
        file_name = input("Enter the file name: ").strip()
    final_file = create_file(file_name)

    while True:
        try:
            print_options()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_task(final_file)

            elif choice == 2:
                remove_task(final_file)

            elif choice == 3:
                list_tasks(final_file)

            elif choice == 4:
                remove_all_tasks(final_file)

            elif choice == 5:
                edit_task(final_file)

            elif choice == 6:
                break

            else:
                print("[!] Please enter a valid choice.")

        except ValueError:
            print("[!] Please enter a valid value.")