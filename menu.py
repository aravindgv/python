class menu(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.myitem = {}

    def additem(self):
        myitem = {self.name : self.price}
        print myitem
        return myitem

    






mymenu=menu('idly',"50")
mymenu.additem()
