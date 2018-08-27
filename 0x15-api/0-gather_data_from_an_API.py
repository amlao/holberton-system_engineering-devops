#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    todo_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + '/users', params={'id': employee_id}).json()
    todo = requests.get(url + '/todos', params={'userId': todo_id}).json()
    complete = []
    task = 0

    for name in user:
        names = item['name']

    for task in todo:
        tasks += 1
        complete.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(complete), len(todo)))
    for check in complete:
        print("\t" + check)
