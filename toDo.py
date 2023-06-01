import argparse


tasks = []


def add_task(title, description) -> None:
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Your task is added successfully!")


def view_tasks() -> None:
    print("List of tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")


def complete_task(title) -> None:
    for task in tasks:
        if task['title'] == title:
            task['completed'] = True
            print("Your task is marked as done.")
            return
    print("This task is not found.")


def delete_task(title) -> None:
    for task in tasks:
        if task['title'] == title:
            del tasks[task]
            print("Your task is deleted successfully.")
            return
    print("This task is not found.")


def main() -> None:
    parser = argparse.ArgumentParser(description="ToDo List Manager")
    parser.add_argument('command', choices=['add', 'complete', 'delete', 'view'])
    parser.add_argument('--title', help="Title of the task")
    parser.add_argument('--description', help="Description of the task")

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.title, args.description)
    elif args.command == 'complete':
        complete_task(args.title)
    elif args.command == 'delete':
        delete_task(args.title)
    elif args.command == 'view':
        view_tasks()
    else:
        return


if __name__ == '__main__':
    main()
