#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    username = user.get("name")
    comp_list = []
    for check in todo:
        comp_list.append({"task": check.get("title"),
                          "completed": str(check.get("completed")),
                          "username": username})
    with open("todo_all_employees.json", 'a') as file:
        file.write(json.dumps({username: comp_list}))
