#!/usr/bin/python3
"""
This module retrieves data from a REST API and exports it to a JSON file.
"""
if __name__ == '__main__':
    import requests
    import json

    # API URLs
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Retrieve all users
    users_response = requests.get(users_url)
    users = users_response.json()

    # Retrieve all todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Dictionary to hold all user tasks
    all_user_tasks = {}

    # Populate the dictionary with tasks for each user
    for user in users:
        user_id = user['id']
        user_name = user['name']
        
        # Filter todos for the current user
        user_todos = [
            {
                "username": user_name,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user_id
        ]
        
        # Assign the list of todos to the user_id key in the dictionary
        all_user_tasks[user_id] = user_todos

    # Export data to JSON
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as jsonfile:
        json.dump(all_user_tasks, jsonfile, indent=4)
