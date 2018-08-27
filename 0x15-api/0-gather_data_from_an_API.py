#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{",
                        params={"id": sys.argv[1]}).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}",
                        params={"userId": sys.argv[1]}).json()
    complete = []
    for task in todo:
        if task.get('completed') is True:
            complete.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(complete), len(todo)))
    for check in complete:
        print("\t {}".format(check))
