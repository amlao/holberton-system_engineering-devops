#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{",
                        params={"id": sys.argv[1]}).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}",
                        params={"userId": sys.argv[1]}).json()
    username = user.get('username')
    comp_list = []
    for done in todo:
        comp_list.append({"task": done.get("title"),
                          "completed": done.get("completed"),
                            "username": username})
        with open(sys.argv[1] + ".json", 'a') as file:
            file.write(json.dumps({"2": comp_list}))
