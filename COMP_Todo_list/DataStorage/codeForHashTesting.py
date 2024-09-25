    # # Test 1: Empty Hash Table
    # hash_table = Hash_Table()
    # search_result = hash_table.searchData("Task")
    # print("Search Result:", search_result)


    # # Test 2: Collision Handling
    # task1 = taskClass.Task("Task 1", "2024-04-05", "Task 1 Detail")
    # task2 = taskClass.Task("Task 2", "2024-04-06", "Task 2 Detail")
    # task3 = taskClass.Task("Task 3", "2024-04-07", "Task 3 Detail")

    # # hash_table = Hash_Table(capacity=1)  # Set capacity to 1 to force collisions
    # hash_table.hashData(task1)
    # hash_table.hashData(task2)
    # hash_table.hashData(task3)
    # data_list = hash_table.loadData()
    # print("Data List:", data_list)

    # hash_table.editPinned("Task 1")

    # search_result = hash_table.searchData("Task 1")
    # print("Search Result:", search_result)

    # hash_table.editTask(task1,"Task 100", "2004-10-10", "Task 100 Detail")

    # data_list = hash_table.loadData()
    # print("Data List:", data_list)


    # search_result = hash_table.searchData("Task 100")
    # print("Search Result:", search_result)

    # # Test 3: Key Overlapping
    # task4 = taskClass.Task("Aa", "2024-04-08", "Task 4 Detail")
    # task5 = taskClass.Task("BB", "2024-04-09", "Task 5 Detail")

    # # hash_table = Hash_Table()
    # hash_table.hashData(task4)
    # hash_table.hashData(task5)

    # search_result = hash_table.searchData("Aa")
    # print("Search Result for Aa:", search_result)

    # search_result = hash_table.searchData("BB")
    # print("Search Result for BB:", search_result)

    # # Test 4: Load Factor
    # # hash_table = Hash_Table(capacity=2)  # Set capacity to 2 for testing load factor
    # task6 = taskClass.Task("Task 6", "2024-04-10", "Task 6 Detail")
    # task7 = taskClass.Task("Task 7", "2024-04-11", "Task 7 Detail")
    # task8 = taskClass.Task("Task 8", "2024-04-12", "Task 8 Detail")

    # hash_table.hashData(task6)
    # hash_table.hashData(task7)
    # hash_table.hashData(task8)

    # data_list = hash_table.loadData()
    # print("Data List:", data_list)

    # # Test 5: Duplicate Keys
    # task9 = taskClass.Task("Task 6", "2024-04-13", "Task 9 Detail")  # Duplicate key with task6
    # hash_table.hashData(task9)

    # search_result = hash_table.searchData("Task 6")
    # print("Search Result:", search_result)

    # # # Test 6: Deleting Elements
    # hash_table = Hash_Table()
    # task10 = taskClass.Task("Task 10", "2024-04-14", "Task 10 Detail")
    # hash_table.hashData(task10)

    # print("Before Deletion")
    # search_result = hash_table.searchData("Task 10")
    # print("Search Result:", search_result)

    # hash_table.deleteTask("Task 10")

    # print("After Deletion")
    # search_result = hash_table.searchData("Task 10")
    # print("Search Result:", search_result)
