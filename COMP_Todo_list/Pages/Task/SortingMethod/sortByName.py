from tkinter import *

def insertionSort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j]["title"] < list[j-1]["title"]:
                list[j],list[j-1] = list[j-1],list[j]
            else:
                break
    return list


def merge(list1,list2):
    pt1 = 0
    pt2 = 0
    mergeResult = []

    while pt1 < len(list1) and pt2 < len(list2):
        if list1[pt1]["title"] >= list2[pt2]["title"]:
            mergeResult.append(list2[pt2])
            pt2+=1
        else:
            mergeResult.append(list1[pt1])
            pt1+=1
    
    while pt1 < len(list1):
        mergeResult.append(list1[pt1])
        pt1+=1

    while pt2 < len(list2):
        mergeResult.append(list2[pt2])
        pt2+=1
    
    return mergeResult

def nameSort(taskManager,tasklist):
    datalist = taskManager.loadData()
    size = len(datalist)
    minRun = 2
    sortedSublist = []
    for i in range(0,size,minRun):
        if size - i >= minRun:
            sortedSublist.append(insertionSort(datalist[i:i+minRun]))
        else:
            sortedSublist.append(insertionSort(datalist[i:size]))
    print(sortedSublist)
    ansList = []


    for j in sortedSublist:
        ansList = merge(ansList,j)
    
    tasklist.delete(0,END)

    for i in ansList:
        if i["pinned"]:
            tasklist.insert(END,i["title"] + "," + str(i["dueDate"])+"*")
        else:
            tasklist.insert(END,i["title"] + "," + str(i["dueDate"]))

    


    

    