import DataStorage.linkedList as linkedList
import DataStorage.taskClass as taskClass
import hashlib

class Hash_Table:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.loadFactor = 0.7
        self.bucketList = [linkedList.Linked_List() for i in range(capacity)]
        self.size = 0

    def loadData(self):
        datalist = []
        for bucket in self.bucketList:
            datalist += bucket.loadData()
        return datalist
    
    def _resizeHashTable(self):
        recordList = self.loadData()
        self.capacity = self.capacity*2
        self.bucketList = [linkedList.Linked_List() for i in range(self.capacity)]
        self.size = 0

        for i in recordList:
            task = taskClass.Task(i["title"], i["dueDate"], i["detail"], i["pinned"])
            self.hashData(task)

    def _addSize(self):
        self.size += 1

    def _minusSize(self):
        self.size -= 1

    def _checkLoadFactor(self):
        usedPercentage = self.size / self.capacity

        if usedPercentage >= self.loadFactor:
            self._resizeHashTable()
            print("_checkLoadFactor: Table resized")
            print("new capacity: ", self.capacity)
            return 1
        return 0
    
    def _hashingFunction(self,title):
        data = title
        # create a sha256 object from hashlib
        sha256 = hashlib.sha256()
        # update sha256 with encoded data
        sha256.update(data.encode("utf-8"))
        # get the hash value from sha256 and convert it from hex to integer
        hashValue =  int(sha256.hexdigest(),16)
        # get the hash index by dividing hashvalue by the capacity
        index = hashValue % self.capacity
        # return index
        return index


    def checkDuplicate(self,newTaskTitle,index):
        if self.bucketList[index].checkDuplicate(newTaskTitle):
            return 1
        return 0 
    
    def hashData(self,task):
        index = self._hashingFunction(task.title)
        if not self.checkDuplicate(task.title,index):
            self.bucketList[index].append(task)
            self._addSize()
            self._checkLoadFactor()
            print("task appended")
            print("size: ",self.size)
            return 1
        print("Found Duplicate title")
        return 0
    
    # search function for user
    def searchData(self,target):
        searchResult = []
        for bucket in self.bucketList:
            searchResult += bucket.search(target)
        return searchResult
    
    # search function for code
    def searchSingleData(self,target): 
        index = self._hashingFunction(target)
        result = self.bucketList[index].readSingleData(target)
        return result
    
    def deleteTask(self,target):
        index = self._hashingFunction(target)
        result = self.bucketList[index].delete(target)

        if result:
            self._minusSize()
            print("task deleted")
            return 1
        return 0
    
    #edit task attributes
    def editTask(self, target, newtitle, newDueDate, newDetail):
        # save the pinned attribute since it can be changed using other function
        targetPinned = target.pinned
        # find the task location
        index = self._hashingFunction(target.title)
        # delete and create task with new attributes then rehash the task for avoiding hash function search error
        self.bucketList[index].delete(target.title)
        self.size-=1
        self.hashData(taskClass.Task(newtitle, newDueDate, newDetail, targetPinned))
    
    #pin or unpin a task 
    def editPinned(self,target):
        index = self._hashingFunction(target)
        
        result = self.bucketList[index].readSingleData(target)
        if result:
            return result.toggle_pinned()
        return 0

    


if __name__ == "__main__":
    hash_table = Hash_Table()  # Set initial capacity to 4 for testing purposes

    # Add tasks to trigger hashtable resizing
    task1 = taskClass.Task("Task 1", "2024-04-05", "Task 1 details")
    hash_table.hashData(task1)

    task2 = taskClass.Task("Task 2", "2024-04-06", "Task 2 details")
    hash_table.hashData(task2)

    task3 = taskClass.Task("Task 3", "2024-04-07", "Task 3 details")
    hash_table.hashData(task3)

    task4 = taskClass.Task("Task 4", "2024-04-08", "Task 4 details")
    hash_table.hashData(task4)

    task5 = taskClass.Task("Task 5", "2024-04-11", "Task 5 details")
    hash_table.hashData(task5)

    task6 = taskClass.Task("Task 6", "2024-04-12", "Task 6 details")
    hash_table.hashData(task6)

    task7 = taskClass.Task("Task 7", "2024-04-13", "Task 7 details")
    hash_table.hashData(task7)

    task8 = taskClass.Task("Task 8", "2024-04-13", "Task 8 details")
    hash_table.hashData(task8)

    task9 = taskClass.Task("Task 9", "2024-04-13", "Task 9 details")
    hash_table.hashData(task9)

    # Display current hashtable state
    print("Hashtable Contents:")
    for bucket in hash_table.bucketList:
        bucket.displayNode()



