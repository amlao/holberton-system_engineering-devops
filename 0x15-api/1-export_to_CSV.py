#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/",
                        params={"id": sys.argv[1]}).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId=",
                        params={"userId": sys.argv[1]}).json()
    for name in user:
        with open(sys.argv[1] + ".csv", 'a') as file:
            output = csv.writer(file, quoting=csv.QUOTE_ALL)
            for tasks in todo:
                output.writerow([sys.argv[1], name.get('name'),
                                 tasks.get('completed'),
                                 tasks.get('title')])
