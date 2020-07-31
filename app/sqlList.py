from sql import Mysqlpython

def testmsg():
    a = Mysqlpython().all('select * from test1')
    print(type(a))
    return {"data":a}

