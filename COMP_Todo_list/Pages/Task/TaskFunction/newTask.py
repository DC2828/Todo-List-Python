from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
import DataStorage.taskClass as taskClass


def createTask(title,dueDate,detail,taskManager):
    temp = taskClass.Task(title,dueDate,detail)
    result = taskManager.hashData(temp)
    print(taskManager.loadData())
    if not result:
        return 0
    return temp

def validation(titleEntry,errorMsg,DueDate,detailEntry,tasklist,newTaskForm,taskManager):
    
    if not titleEntry.get():
        errorMsg.set("Task title is Mandatory")
        return

    today = datetime.today().date()
    selectedDate = DueDate.get_date()

    if today > selectedDate:
        errorMsg.set("Due Date must be set by {}".format(today.strftime("%Y-%m-%d")))
        return
    
    result = createTask(titleEntry.get(),DueDate.get_date(),detailEntry.get("1.0","end"),taskManager)

    if result:
        tasklist.insert(0,result.title+","+str(result.dueDate))
        newTaskForm.destroy()
    else:
        errorMsg.set("Duplicate title found")


        

def addTask(root,tasklist,taskManager):
    newTaskForm = Toplevel(root)
    # newTaskForm = Tk()
    newTaskForm.geometry("400x400")
    newTaskForm.minsize(400,400)
    newTaskForm.maxsize(400,400)
    informationContainer = Frame(newTaskForm)
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

    global DueDate
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
    createbtn = Button(informationContainer,
                       text="Create Task",
                       padx=10,
                       pady=10,
                       command=lambda: validation(titleEntry,errorMsg,DueDate,detailEntry,tasklist,newTaskForm,taskManager)) 
    createbtn.pack(anchor=CENTER)

    newTaskForm.mainloop()


