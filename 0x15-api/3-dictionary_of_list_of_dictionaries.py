#!/usr/bin/python3
"""
Module: 3-dictionary_of_list_of_dictionaries.py

- Get some fake data from users for name of the employee
  - convert it to json data
- Get tasks from that usr to process the completed with True value
  - Convert it to json data
- Count the number of task to compare with the total of task of that usr
- Pass all completed task to a list to print to stdout later
- Print a string with the name of that usr and the total of task completed
- Print then, after, the tasks done of the usr
"""

from requests import *
from sys import argv
import json


if __name__ == "__main__":

    rqDt = get('https://jsonplaceholder.typicode.com/users/')
    rqDt = rqDt.json()

    tdLst = {}

    for dt in rqDt:
        usrId = dt['id']
        usrNm = dt['username']

        usrDt = get('https://jsonplaceholder.typicode.com/todos?userId=' +
                    "{}".format(usrId)).json()

        tskLst = []

        for items in usrDt:
            tskLst.append({
                "username": usrNm,
                "task": items['title'],
                "completed": items['completed']
            })

        tdLst[usrId] = tskLst

    with open('todo_all_employees.json', 'w') as File:
        json.dump(tdLst, File)

#    print("-------------  Below is testing code  --------------")

#    rqDtJs = rqDtJs['name']
#    print(empName)

#    print("-----------------------------")

#    rqUsrDt = get('https://jsonplaceholder.typicode.com/todos?userId='
#                 + argv[1])

#    rqUsrDt = rqUsrDt.json()

#    print(rqUsrDt)

#    print("------------------------------")

#    for data in rqUsrDt:
#        if data['completed']:
#            print(data)

#    print("------------------------------")

#    for dt in rqUsrDt:
#        if dt["completed"] == True:
#            print(dt)
