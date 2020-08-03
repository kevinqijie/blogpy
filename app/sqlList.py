from sql import Mysqlpython
def testmsg():
    a = Mysqlpython().all('select * from test1')
    print(type(a))
    return {"data":a}

def push(title,create_user,category,description,content,create_time):
    arcticleID = Mysqlpython().all('select md5(uuid())')[0][0]
    id = Mysqlpython().all('select md5(uuid())')[0][0]
    Mysqlpython().zhixing('INSERT INTO article (id,title,create_user,category,description,content,create_time)VALUES("'
    +arcticleID+'","'
    +title+'","'
    +create_user+'",'
    +category+',"'
    +description+'","'
    +content+'","'
    +create_time+'")')
    Mysqlpython().zhixing('INSERT INTO article_list (id,article_id,title,create_user,category,description,create_time) VALUES("'
                          +id+'","'
                          +arcticleID+'","'
                          +title+'","'
                          +create_user+'",'
                          +category+',"'
                          +description+'","'
                          +create_time+'")')