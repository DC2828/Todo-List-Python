import csv
from tkinter import *
from DataStorage import taskClass
import datetime


def read(taskManager, tasklist):
    try:
        dataFile = open(".//DataStorage//Data//recordData.csv","r")

        reader = csv.DictReader(dataFile)
        for i in reader:
            if i["pinned"] == "True":
                i["pinned"] = True
            elif i["pinned"] == "False":
                i["pinned"] = False

            time = datetime.datetime.strptime(i["dueDate"], "%Y-%m-%d").date()
            taskObj = taskClass.Task(i["title"],time,i["detail"],i["pinned"])
            taskManager.hashData(taskObj)

            if taskObj.pinned:
                tasklist.insert(END,taskObj.title + "," + i["dueDate"] + "*")
            else:
                tasklist.insert(END,taskObj.title + "," + i["dueDate"])
        dataFile.close()
    except FileNotFoundError:
        dataFile = open(".//DataStorage//Data//recordData.csv","w")
        dataFile.close()
