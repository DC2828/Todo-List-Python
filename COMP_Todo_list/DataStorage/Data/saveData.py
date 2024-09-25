import csv
from tkinter import messagebox

def save(root, taskManager):
    data = taskManager.loadData()

    categories = ["title","dueDate","detail","pinned"]
    try:
        dataFile = open(".//DataStorage//Data//recordData.csv",'w',newline="")
        input = csv.DictWriter(dataFile, fieldnames=categories)

        input.writeheader()
        input.writerows(data)
        
        dataFile.close()

        root.destroy()
    except:
        close = messagebox.askyesno("close window", "Save Failed, do you want to close the window?")

        if close:
            root.destroy()
        else:
            return