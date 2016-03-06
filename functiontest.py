def getcs():
    s=raw_input("server")
    d=raw_input("dbname")
    p=raw_input("password")
    u=raw_input("username")
    cs="server=%s;db=%s;pasword=%s;username=%s" %(s,d,u,p)
    return cs

def cstodict(cs):
    d={}
    for i in cs.split(";"):
        k,v=i.split("=")
        d[k]=v

    return d

cs=getcs()
d=cstodict(cs)
print d