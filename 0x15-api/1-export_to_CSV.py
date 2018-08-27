#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{",
                        params={"id": sys.argv[1]}).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}",
                        params={"userId": sys.argv[1]}).json()
    with open(sys.argv[1] + ".csv", 'a') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for tasks in todo:
            writer.writerow([sys.argv[1], str(sys.argv[1]),
                             tasks.get('completed'),
                             tasks.get('title')])
