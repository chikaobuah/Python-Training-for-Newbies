class Website:
    def __init__(self,title):
        self.title = title

    def showTitle(self):
        print(self.title)

obj = Website('askpython.com')
obj.showTitle()