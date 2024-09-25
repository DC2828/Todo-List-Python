from tkinter import *
from tkinter import messagebox
def deleteTask(errorMsg, tasklist, taskManager):
    if tasklist.size() == 0:
        errorMsg.set("There is no task in the list")
    elif not tasklist.curselection():
        errorMsg.set("Please select a task to delete")
    else:
        targetIndex = tasklist.curselection()[0]
        taskTitle = tasklist.get(targetIndex).split(",")[0]
        approve = messagebox.askyesno("confirmation","Do you want to delete \"" + taskTitle + "\" ?")

        if approve:
            deleted = taskManager.deleteTask(taskTitle)
            if deleted:
                tasklist.delete(targetIndex)
                print(taskManager.loadData())
            else:
                errorMsg.set("Delete failed: Task not found")


