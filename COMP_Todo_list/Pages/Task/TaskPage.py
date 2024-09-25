from tkinter import *
from tkinter import ttk
import Pages.Task.TaskFunction.newTask as newTask
import Pages.Task.TaskFunction.searchTask as searchTask
import Pages.Task.TaskFunction.editTask as editTask
import Pages.Task.TaskFunction.setPinned as setPinned
import Pages.Task.TaskFunction.deleteTask as deleteTask
import Pages.Task.SortingMethod.sortByDate as sortByDate
import Pages.Task.SortingMethod.sortByName as sortByName
import Pages.Task.SortingMethod.sortByPinned as sortByPinned


def getSortFunction(selectedSort,taskManager,tasklist,errorMsg):
    if selectedSort == "Sort by Name":
        sortByName.nameSort(taskManager,tasklist)
    elif selectedSort == "Sort by Date":
        sortByDate.dateSort(taskManager,tasklist)
    elif selectedSort == "Sort by Pinned":
        sortByPinned.pinnedSort(taskManager,tasklist)
    else:
        errorMsg.set("Please select a sort function")


def taskPageDisplay(root, Task, taskManager, readData):
    root.minsize(800, 500)
    root.maxsize(800, 500)


    ytaskScrollbar = Scrollbar(Task,orient=VERTICAL)
    ytaskScrollbar.grid(row=0,column=1,sticky=NS)

    xtaskScrollbar = Scrollbar(Task,orient=HORIZONTAL)
    xtaskScrollbar.grid(row=1,column=0,sticky=EW)


    tasklist = Listbox(Task,
                   bg="#f7ffde",
                   font=("Arial",20),
                   selectmode=SINGLE,
                   selectbackground="grey",
                   yscrollcommand=ytaskScrollbar.set,
                   xscrollcommand=xtaskScrollbar.set,
                   width=35,
                   height=7
                   )
    tasklist.grid(row=0,column=0,sticky=NS)

    ytaskScrollbar.config(command=tasklist.yview)
    xtaskScrollbar.config(command=tasklist.xview)

    buttonContainer = Frame(Task,
                            bg="grey",
                            width=250,
                            height=400,
                            padx=10,
                            pady=10)
    buttonContainer.grid(row=0,column=2)
    # set container-------------------
    setContainer = Frame(buttonContainer,bg="grey",width=400,padx=10,pady=10)

    addTaskbtn = Button(setContainer,text="Add Task",command = lambda: newTask.addTask(root,tasklist,taskManager))
    addTaskbtn.grid(row=0,column=0)

    setContainer.pack(anchor=CENTER)
    # search container---------------------
    searchContainer = Frame(buttonContainer,bg="grey",width=400,padx=10,pady=10)
    
    searchBar = Entry(searchContainer)
    searchBar.grid(row=0,column=0)

    space = Label(searchContainer,bg="grey")
    space.grid(row=0,column=1)
    
    searchBtn = Button(searchContainer,
                       text="search",
                       command=lambda:searchTask.search(tasklist,searchBar,taskManager))
    searchBtn.grid(row=0,column=2)

    searchContainer.pack(anchor=CENTER)
    # edit container------------------------
    editContainer = Frame(buttonContainer,bg="grey",width=400,padx=10,pady=10)

    editBtn = Button(editContainer,text="Check task",command=lambda: editTask.edit(errorMsg,tasklist,root,taskManager))
    editBtn.grid(row=0, column=0)

    editSpaceLabel = Label(editContainer,bg="grey",width=2)
    editSpaceLabel.grid(row=0,column=1)

    editPinned = Button(editContainer,text="Pin/Unpin",command=lambda: setPinned.setPinned(errorMsg,tasklist,taskManager))
    editPinned.grid(row=0, column=2)
    editContainer.pack(anchor=CENTER)
    # Delete container------------------------
    deleteContainer = Frame(buttonContainer, bg="grey",width=400, padx=10,pady=10)
    deleteBtn = Button(deleteContainer,text="Delete",command=lambda: deleteTask.deleteTask(errorMsg,tasklist,taskManager))
    deleteBtn.grid(row=0,column=0)
    deleteContainer.pack(anchor=CENTER)
    # sorting container----------------------------
    sortContainer = Frame(buttonContainer,bg="grey",width=400,padx=10,pady=10)

    sortSelect = ttk.Combobox(sortContainer,width=14)
    sortSelect["values"] = ["Sort by Name","Sort by Date","Sort by Pinned"]
    sortSelect.grid(row=0,column=0)

    sortLabel = Label(sortContainer,width=1,bg="grey")
    sortLabel.grid(row=0,column=1)
    sortBtn = Button(sortContainer, text="Start sort",command=lambda:getSortFunction(sortSelect.get(),taskManager,tasklist,errorMsg))
    sortBtn.grid(row=0,column=2)

    sortContainer.pack(anchor=CENTER)
    # error container-------------------------
    errorMsg = StringVar()
    errorMsg.set("")
    errorContainer = Frame(buttonContainer, bg="grey",width=400, padx=10,pady=10)

    error = Label(errorContainer, textvariable=errorMsg, bg="grey", foreground="red")
    error.pack(anchor=CENTER)
    errorContainer.pack(anchor=CENTER)
    # ------------------------------------------
    buttonContainer.pack_propagate(0)
    
    readData.read(taskManager,tasklist)
