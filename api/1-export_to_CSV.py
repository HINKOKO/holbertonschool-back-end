#!/usr/bin/python3
"""
Script to gather data from an API, and export it in CSV format
==> "requests" module allows us to send HTTP Requests
The request returns a Response Object with all data
(content, encoding, status, etc...)
"""
# import json
import csv
import requests
from sys import argv

response_API = 'https://jsonplaceholder.typicode.com/'
if __name__ == "__main__":
    users = requests.get("{}users/{}".format(response_API, argv[1])).json()
    todos = requests.get("{}todos?userId={}".format(
        response_API, argv[1])).json()

    with open("{}.csv".format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos:
            writer.writerow(["{}".format(argv[1]),
                             users['username'],
                             tasks['completed'],
                             tasks['title']])
