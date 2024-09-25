from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime


def validation(titleEntry,DueDate,detailEntry,errorMsg,taskManager,task,taskList,editTaskForm,selected):
    
    if not titleEntry.get():
        errorMsg.set("Task title is Mandatory")
        return

    today = datetime.today().date()
    selectedDate = DueDate.get_date()

    if today > selectedDate:
        errorMsg.set("Due Date must be set by {}".format(today.strftime("%Y-%m-%d")))
        return
    
    result = taskManager.searchSingleData(titleEntry.get())
    if (result and titleEntry.get() == result.title and result == task) or (not result):
        taskList.delete(selected)
        taskManager.editTask(task, titleEntry.get(), DueDate.get_date(), detailEntry.get("1.0","end"))
        if task.pinned:
            taskList.insert(selected,titleEntry.get() + "," + str(DueDate.get_date())+"*")
        else:
            taskList.insert(selected,titleEntry.get() + "," + str(DueDate.get_date()))
        editTaskForm.destroy()

    elif titleEntry.get() == result.title:
        errorMsg.set("Duplicate title found")



def editWindow(root,task,taskManager,taskList,selected):
    editTaskForm = Toplevel(root)

    editTaskForm.geometry("400x400")
    editTaskForm.minsize(400,400)
    editTaskForm.maxsize(400,400)
    informationContainer = Frame(editTaskForm)
    informationContainer.pack()
# --------------------------------------------------------
    titleContainer = Frame(informationContainer,padx=10,pady=10)

    titleLabel = Label(titleContainer,text="Task Title: ")
    titleLabel.grid(row=0,column=0)

    titleEntry = Entry(titleContainer)
    titleEntry.grid(row=0,column=1)
    
    titleContainer.pack(anchor=CENTER)
# -----------------------------------------------------------
    dateContainer = Frame(informationContainer)

    DueDateLabel = Label(dateContainer,
                         font=("Arial",10))
    DueDateLabel.grid(row=0,column=0)

    DueDate = DateEntry(dateContainer,
                       date_pattern="dd/MM/yyyy",
                       font = ("Arial",10),
                       selectmode="day",
                       showweeknumbers=False)
    DueDate.grid(row=0,column=1)

    dateContainer.pack(anchor=CENTER)
# ---------------------------------------------------------
    detailContainer = Frame(informationContainer,padx=10,pady=10)

    detailLabel = Label(detailContainer,text="Detail: ")
    detailLabel.grid(row=0,column=0)

    detailEntry = Text(detailContainer,
                       width=50,
                       height=10,
                       font=("Arial",10))
    detailEntry.grid(row=1,column=0)
    
    detailContainer.pack(anchor=CENTER)
# --------------------------------------------------------------
    errorMsg = StringVar()
    errorMsg.set("")
    errorContainer = Label(informationContainer,textvariable=errorMsg,foreground="red")
    errorContainer.pack(anchor=CENTER)
# -------------------------------------------------------------- 
    btnContainer = Frame(informationContainer)
    btnContainer.pack(anchor=CENTER)

    saveEditbtn = Button(btnContainer,
                       text="Save Edit",
                       padx=10,
                       pady=10,
                       command = lambda: validation(titleEntry,DueDate,detailEntry,errorMsg,taskManager,task,taskList,editTaskForm,selected)) 
    saveEditbtn.grid(row=0,column=0)

    space = Label(btnContainer)
    space.grid(row=0,column=1)

    cancelBtn = Button(btnContainer,
                       text="Cancel",
                       padx=10,
                       pady=10,
                       command = lambda: editTaskForm.destroy())
    cancelBtn.grid(row=0,column=2)

    titleEntry.insert(0,task.title)
    DueDate.set_date(task.dueDate)
    detailEntry.insert(INSERT,task.detail.strip())

    editTaskForm.mainloop()



def edit(errorMsg,taskList,root,taskManager):
    if taskList.size() == 0:
        errorMsg.set("There is no task in the list")
    elif not taskList.curselection():
        errorMsg.set("Please select the task")
    else:
        # curselection returns a tuple of selected items in listbox
        # get() will get the content inside of the index that has been passed in
        selected = taskList.curselection()[0]
        targetTitle = taskList.get(selected).split(",")[0]

        task = taskManager.searchSingleData(targetTitle)


        editWindow(root,task,taskManager,taskList,selected)