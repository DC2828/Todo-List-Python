from tkinter import *

def pinnedSort(taskManager, tasklist):
    dataList = taskManager.loadData()
    for i in range(1,len(dataList)):
        for j in range(i,0,-1):
            if dataList[j]["pinned"] == True and dataList[j-1]["pinned"] == False:
                dataList[j],dataList[j-1] = dataList[j-1],dataList[j]
            else:
                break

    tasklist.delete(0,END)
    for i in dataList:
        if i["pinned"]:
            tasklist.insert(END,i["title"] + "," + str(i["dueDate"])+"*")
        else:
            tasklist.insert(END,i["title"] + "," + str(i["dueDate"]))