"""
This module provides functionality for managing a to-do list.
"""

import argparse


def add_task(tasks, title, description) -> None:
    """
    Add a new todo item

    :param tasks: required tasks to do
    :param title: title of todo item
    :param description: description of todo item
    :return:
    """

    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Your task is added successfully!")


def view_tasks(tasks) -> None:
    """
    View all the tasks
    :param tasks: existed tasks
    :return:
    """

    print("List of tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")


def complete_task(tasks, title) -> None:
    """
    Mart task as completed
    :param tasks: existed tasks
    :param title: title of task to mark as completed
    :return:
    """

    for task in tasks:
        if task['title'] == title:
            task['completed'] = True
            print("Your task is marked as done.")
            return
    print("This task is not found.")


def delete_task(tasks, title) -> None:
    """
    Delete a todo item
    :param tasks: existed task
    :param title: title of task to delete
    :return:
    """
    for task in tasks:
        if task['title'] == title:
            del tasks[task]
            print("Your task is deleted successfully.")
            return
    print("This task is not found.")


def save_tasks(tasks, filename):
    """
    Save all the tasks to file
    :param tasks: existed tasks
    :param filename: file to write info
    :return:
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        for task in tasks:
            file.write(f"{task['title']},"
                       f"{task['description']},{task['completed']}\n")


def load_tasks(filename):
    """
    Load all the tasks from file
    :param filename: file to upload
    :return:
    """

    tasks = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            data = line.strip().split(',')
            task = {
                'title': data[0],
                'description': data[1],
                'completed': data[2] == 'True'
            }
            tasks.append(task)
    return tasks


def main() -> None:
    """
    Main function
    :return:
    """

    parser = argparse.ArgumentParser(description="ToDo List Manager")
    parser.add_argument('--file',
                        default='todo_list.txt', help='Path to file')
    parser.add_argument('command',
                        choices=['add', 'complete', 'delete', 'view'])
    parser.add_argument('--title',
                        help="Title of the task")
    parser.add_argument('--description',
                        help="Description of the task")

    args = parser.parse_args()
    tasks = load_tasks(args.file)

    if args.command == 'add':
        add_task(tasks, args.title, args.description)
    elif args.command == 'complete':
        complete_task(tasks, args.title)
    elif args.command == 'delete':
        delete_task(tasks, args.title)
    elif args.command == 'view':
        view_tasks(tasks)
    else:
        return

    save_tasks(tasks, args.file)


if __name__ == '__main__':
    main()
