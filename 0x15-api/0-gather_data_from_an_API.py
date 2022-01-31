#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API.py

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


if __name__ == "__main__":

    empId = argv[1]

    rqDt = get('https://jsonplaceholder.typicode.com/users/'
               + empId)

    empName = rqDt.json()['name']

    rqUsrDt = get('https://jsonplaceholder.typicode.com/todos?userId='
                  + empId)

    rqUsrDt = rqUsrDt.json()

    doneTask = 0
    lstDnTsk = []

    for dt in rqUsrDt:
        if dt["completed"] is True:
            doneTask += 1
            lstDnTsk.append(dt['title'])

    print("Employee {} is done with tasks({}/{}):".format(empName,
                                                          doneTask,
                                                          len(rqUsrDt)))

    for tskDt in range(len(lstDnTsk)):
        print("\t {}".format(lstDnTsk[tskDt]))

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
