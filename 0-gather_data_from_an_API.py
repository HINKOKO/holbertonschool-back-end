#!/usr/bin/python3
"""
Script to gather data from an API
==> "requests" module allows us to send HTTP Requests
The request returns a Response Object with all data
(content, encoding, status, etc...)
"""
# import json
import requests
from sys import argv

response_API = 'https://jsonplaceholder.typicode.com/'
if __name__ == "__main__":
    users = requests.get("{}users/{}".format(response_API, argv[1])).json()
    todos = requests.get("{}todos?userId={}".format(
        response_API, argv[1])).json()

    task_completed = [task['title'] for task in todos if task['completed']]
    print("Employee {} is done with tasks ({}/{})"
          .format(users["name"], len(task_completed), len(todos)))
    print("\n".join("\t {}".format(done) for done in task_completed))
