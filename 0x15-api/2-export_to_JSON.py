#!/usr/bin/python3
"""
This module retrieves data from a REST API and exports it to a JSON file.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    # users
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # todos
    todos_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos/'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    # Get the name of the person with the matching id
    user_name = None
    users = users_response.json()

    for user in users:
        # check if the id of this user matches, and store their name
        if user['id'] == int(argv[1]):
            # store the name
            user_name = user['name']

    todo_lists = todos_response.json()  # store all the todos for the user
    total_tasks = len(todo_lists)

    completed_todos = []  # store the completed todos

    # look through each todo, checking if it is completed
    for todo_list in todo_lists:
        if todo_list['completed'] is True:
            completed_todos.append(todo_list)

    completed_count = len(completed_todos)

    # print message about user info
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, completed_count, total_tasks
        )
    )
    # print titles
    for todo in completed_todos:
        print(f"\t {todo['title']}")

    # Create JSON structure
    user_tasks = {
        argv[1]: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user_name,
            }
            for todo in todo_lists
        ]
    }

    # Export data to JSON
    json_filename = f"{argv[1]}.json"
    with open(json_filename, mode='w') as jsonfile:
        json.dump(user_tasks, jsonfile, indent=4)
