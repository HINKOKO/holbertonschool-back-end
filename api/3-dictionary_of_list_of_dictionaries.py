#!/usr/bin/python3
"""
Script to gather data from an API
Export in JSON format, all tasks from all employees!
Party time !!
==> "requests" module allows us to send HTTP Requests
The request returns a Response Object with all data
(content, encoding, status, etc...)
"""
import json
import requests
from sys import argv


response_API = 'https://jsonplaceholder.typicode.com/'

if __name__ == "__main__":
    res = requests.get("{}users".format(response_API)).json()
    # print(res)
    tasks_list = []
    tasks_dict = {}
    for user in res:
        name = user.get("username")
        # print(name)
        user_id = user.get("id")
        # print(user_id)
        tasks = requests.get("{}todos?userId={}".format(
            response_API, user_id)).json()
        # print(tasks)
        for task in tasks:
            # print(task)
            t_d = {"username": name,
                   "task": task.get("title"),
                   "completed": task.get("completed")}
            tasks_list.append(t_d)
        tasks_dict[user_id] = tasks_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)
