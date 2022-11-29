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

if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    dict_json = {}
    list_id = [u.get('id') for u in users]
    for ids in list_id:
        users_id = requests.get(
            "https://jsonplaceholder.typicode.com/users?id:ids").json()
        # print(users_id)
        user = users_id[0].get("username")
        users_task = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId:ids").json()
        # print(user)
        t_list = []
        t_dict = {}
        for t in users_task:
            t_dict = {"username": user,
                      "task": t.get('title'),
                      "completed": t.get('completed')
                      }
            t_list.append(t_dict)
        dict_json.update({ids: t_list})
        with open("todo_all_employees.json", 'w') as jsonfile:
            json.dump(dict_json, jsonfile)
