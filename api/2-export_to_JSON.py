#!/usr/bin/python3
"""
Script to gather data from an API, export to JSON format
==> "requests" module allows us to send HTTP Requests
The request returns a Response Object with all data
(content, encoding, status, etc...)
"""
import json
import requests
from sys import argv


response_API = 'https://jsonplaceholder.typicode.com/'

if __name__ == "__main__":
    users = requests.get("{}users/{}".format(response_API, argv[1])).json()
    todos = requests.get("{}todos?userId={}".format(
        response_API, argv[1])).json()

    t_list = []
    t_dict = {}
    for t in todos:
        t_dict = {"task": t.get("title"),
                  "completed": t.get("completed"),
                  "username": users.get("username")
                  }
        t_list.append(t_dict)
        dict_json = {}
        dict_json[(argv[1])] = t_list
        with open("{}.json".format(argv[1]), 'w') as jsonfile:
            json.dump(dict_json, jsonfile)
