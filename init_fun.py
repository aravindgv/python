class person:
    def __init__(self,name,place):
        self.myname = name
        self.myplace = place

    def sayhi(self):
        print 'Hello, my name is',self.myname

    def place(self):
        print 'my place is',self.myplace

p  =    person('JaiSriram','Bangalore')
p.sayhi()
p.place()
print p.myname
print p.myplace