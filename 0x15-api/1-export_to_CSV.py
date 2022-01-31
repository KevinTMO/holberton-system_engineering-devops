#!/usr/bin/python3
"""
Module: 1-export_to_CSV.py

- Get some fake data from users for name of the employee
  - convert it to json data
- Get tasks from that usr to process the completed with True value
  - Convert it to json data
- Open a csv file and pass the json output in there
  - Output should be like: "USER_ID","USERNAME",
                           "TASK_COMPLETED_STATUS","TASK_TITLE"
"""

from requests import *
from sys import argv
import csv


if __name__ == "__main__":

    empId = argv[1]

    rqDt = get('https://jsonplaceholder.typicode.com/users/'
               + empId)

    empName = rqDt.json()['username']

    rqUsrDt = get('https://jsonplaceholder.typicode.com/todos?userId='
                  + empId)

    rqUsrDt = rqUsrDt.json()

    with open("{}.csv".format(empId), "w") as csvFile:
        for dt in rqUsrDt:
            csvFile.write(
                '"{}", "{}", "{}", "{}"\n'.format(empId, empName,
                                                  dt['completed'],
                                                  dt['title'])
            )

#    print("-------------  Below is testing code  --------------")

#    print(rqDt)

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
