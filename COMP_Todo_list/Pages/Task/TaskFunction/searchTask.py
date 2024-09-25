from tkinter import *

def search(tasklist, searchBar, taskManager, ):
    target = searchBar.get()
    searchBar.delete(0,END)
    if target:
        resultList = taskManager.searchData(target)
        tasklist.delete(0,END)

        for i in resultList:
            if i["pinned"]:
                tasklist.insert(0,i["title"] + "," + str(i["dueDate"])+"*")
            else:
                tasklist.insert(0,i["title"] + "," + str(i["dueDate"]))
    else:
        resultList = taskManager.loadData()
        tasklist.delete(0,END)
        for i in resultList:
            tasklist.insert(0,i["title"] + "," + str(i["dueDate"]))
