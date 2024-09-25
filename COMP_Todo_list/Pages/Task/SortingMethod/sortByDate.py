from datetime import *
from tkinter import *

def dateSort(taskManager, tasklist):
  dataList = taskManager.loadData()

  dateDiff = []
  today = datetime.now()

  for data in dataList:
    time = data["dueDate"]
    year = int(time.strftime("%Y-%m-%d")[0:4])
    month = int(time.strftime("%Y-%m-%d")[5:7])
    day = int(time.strftime("%Y-%m-%d")[8:10])

    date1 = datetime(year, month, day)
    todayDate = datetime(today.year, today.month, today.day)
    diff = date1 - todayDate
    dateDiff.append(diff.days)
    list = heapSort(dateDiff, dataList)
    tasklist.delete(0,END)
    for i in list:
      if i["pinned"]:
        tasklist.insert(END,i["title"] + "," + str(i["dueDate"])+"*")
      else:
        tasklist.insert(END,i["title"] + "," + str(i["dueDate"]))


def heapSort(list, dueDatesList):
  listLength = len(list) 
  # Build max heap
  heapify(list, listLength, dueDatesList) # Call heapify function until the root is the largest
  for i in range(listLength-1, 0, -1): # Reduce the list length by one each time so the unsorted region will eventually remain one element
    list[0], list[i] = list[i], list[0] # Extract the maximum element and place it at the end of the list
    dueDatesList[0], dueDatesList[i] = dueDatesList[i], dueDatesList[0] # The dueDatesList follows the changes of datediff list
    heapify(list, i, dueDatesList) # Build the max heap again
  return dueDatesList

def heapify(list, listLength, dueDatesList):
  for parentIndex in range(listLength//2-1, -1, -1): # Loop through the parent indexes in the list
    leftChildIndex = 2*parentIndex+1 # Formula for finding the left child index of the current parent index
    rightChildIndex = 2*parentIndex+2 # Formula for finding the right child index of the current parent index
    largestNode = leftChildIndex

    if rightChildIndex < listLength and list[rightChildIndex] > list[leftChildIndex]: # Check if right child exists and whether it is larger than its parent
      largestNode = rightChildIndex

    if list[largestNode] > list[parentIndex]:
      list[parentIndex], list[largestNode] = list[largestNode], list[parentIndex] # Swap the values if the parent is smaller than its child to make the parent the largest
      dueDatesList[parentIndex], dueDatesList[largestNode] = dueDatesList[largestNode], dueDatesList[parentIndex]

