import DataStorage.taskClass as taskClass
import DataStorage.hashTable as hashTable
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
    # append task
    def append(self,data):
        if self.head == None:
            self.head = node(data)
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node(data)
        return
    # delete task
    def delete(self,target):
        frontNode = self.head
        if frontNode == None:
            return 0

        if frontNode.data.title == target:
            self.head = None
            return 1
        
        prevNode = frontNode
        frontNode = frontNode.next

        while frontNode != None:
            if frontNode.data.title == target:
                prevNode.next = frontNode.next
                return 1
            prevNode = frontNode
            frontNode = frontNode.next
        return 0
    # check duplicate task
    def checkDuplicate(self,newDataTitle):
        if self.head == None:
            return 0
        
        temp = self.head

        while temp != None:
            if temp.data.title == newDataTitle:
                return 1
            temp = temp.next
        
        return 0

    def readSingleData(self,target):
        temp = self.head
        while temp != None:
            if target == temp.data.title:
                print("readSingleData: Task found")
                return temp.data
            temp = temp.next

        print("readSingleData: Task not found")
        return 0
    
    # search function for user
    def search(self,target):
        if self.head == None:
            return []
        
        temp = self.head
        searchResult = []
        while temp != None:
            if target in temp.data.title:
                searchResult.append(vars(temp.data))
            temp = temp.next
        
        return searchResult
    

    # load all data
    def loadData(self):
        if self.head == None:
            return []
        
        temp = self.head
        dataList = []
        while temp != None:
            data = vars(temp.data)
            data["detail"].rstrip()
            dataList.append(data)
            temp = temp.next
        return dataList

    def displayNode(self):
        if self.head == None:
            print("displayNode: nothing is in the list")
            return 0
        
        temp = self.head
        result = []
        while temp != None:
            data = vars(temp.data)
            data["detail"].rstrip()
            result.append(data)
            temp = temp.next
        print(result)

if __name__ == "__main__":
    # test code
    task1 = taskClass.Task("Task 1", "2024-04-05", "Complete task 1")
    task2 = taskClass.Task("Task 2", "2024-04-06", "Complete task 2")
    task3 = taskClass.Task("Task 3", "2024-04-07", "Complete task 3")

    task_list = Linked_List()

    task_list.append(task1)
    task_list.append(task2)
    task_list.append(task3)

    # search_results = task_list.search("Task")
    # print("Search Results:")
    # print(search_results)


    task_list.displayNode()

   


    # deleted = task_list.delete("Task 2")
    # if deleted:
    #     print("Task 2 deleted successfully")
    # else:
    #     print("Task 2 not found")


    # task_list.displayNode()

    # print(task_list.loadData())
