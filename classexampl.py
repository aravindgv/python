class Basic(object):
    def __int__(self,name):
        print "in  __init__"
        self.name = name
    def show(self):
        print "in Show"
        print self
        print "Basic --name:  %s" % self.name

x=Basic(2)
