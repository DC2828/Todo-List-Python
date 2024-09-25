class Task:
    def __init__(self,title,dueDate,detail="", pinned = False):
        self.title = title
        self.dueDate = dueDate
        self.detail = detail
        self.pinned = pinned

    def set_title(self,new_title):
        self.title = new_title

    def set_dueDate(self,new_dueDate):
        self.dueDate = new_dueDate

    def set_detail(self,new_detail):
        self.detail = new_detail
    
    def toggle_pinned(self):
        if self.pinned:
            self.pinned = False
        else:
            self.pinned = True
        return self.pinned

    def get_title(self):
        return self.title
    
    def get_dueDate(self):
        return self.dueDate
    
    def get_detail(self):
        return self.detail
    
    def get_pinned(self):
        return self.pinned