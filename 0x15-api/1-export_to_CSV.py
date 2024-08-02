#!/usr/bin/python3
"""
This module retrieves data from a REST API and exports it to a CSV file.
"""
import csv
import requests
import sys

if __name__ == '__main__':

    # users
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # todos
    todos_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos/'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    # Get the name of the person with the matching id
    user_name = None
    users = users_response.json()

    for user in users:
        # check if the id of this user matches, and store their name
        if user['id'] == int(sys.argv[1]):
            # store the name
            user_name = user['username']

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

    # Export data to CSV
    with open("{}.csv".format(sys.argv[1]), mode="w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, quoting=csv.QUOTE_ALL
        )
        for todo in todo_lists:
            writer.writerow(
                    [sys.argv[1],  user_name, todo.get('completed'), todo.get('title')]
            )
