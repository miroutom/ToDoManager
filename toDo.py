tasks = []


def add_task() -> None:
    title = input("Enter the title of your task: ")
    description = input("Enter the description of your task: ")
    deadline = input("Enter the deadline of your task: ")
    task = {
        "title": title,
        "description": description,
        "deadline": deadline,
        "completed": False
    }
    tasks.append(task)
    print("Your task is added successfully!")


def view_tasks() -> None:
    print("List of tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']}: {task['description']}.\n"
              f"Deadline: {task['deadline']} - {task['completed']}")


def complete_task() -> None:
    task_number = int(input("Enter the number of task that you want to mark as done: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task['completed'] = True
        print("Your task is mark as done!")
    else:
        print("Wrong number!")


def delete_task() -> None:
    task_number = int(input("Enter the number of task that you want to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Your task is deleted successfully!")
    else:
        print("Wrong number!")


def main() -> None:
    print("Menu:\n1. Add a task\n2. See tasks\n3. Mark a task as done\n4. Delete a task\n0. Quit")
    while True:
        choice = int(input("Choose the option: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            delete_task()
        elif choice == 0:
            break
        else:
            print("Wrong choice. Try again.")


if __name__ == '__main__':
    main()