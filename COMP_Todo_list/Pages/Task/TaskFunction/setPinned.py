
def setPinned(errorMsg,tasklist,taskManager):
    if tasklist.size() == 0:
        errorMsg.set("There is no task in the list")
    elif not tasklist.curselection():
        errorMsg.set("Please select a task")


    else:
        targetIndex = tasklist.curselection()[0]
        targetContent = tasklist.get(tasklist.curselection()[0])

        taskTitle = targetContent.split(",")[0]
        print(taskTitle)
        taskManager.editPinned(taskTitle)

        tasklist.delete(targetIndex)
        if "*" in targetContent:
            tasklist.insert(targetIndex,targetContent.rstrip("*"))
        else:
            tasklist.insert(targetIndex,targetContent+"*")

        

