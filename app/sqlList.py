from sql import Mysqlpython

def testmsg():
    a = Mysqlpython().all('select * from test1')
    print(type(a))
    return {"data":a}

def push():
    INSERT INTO article (id,title,create_user,category,description,content,create_time) VALUES (REPLACE(UUID(),"-",""),"sss","sss",1,"description","content","2020-07-31 10:40:12");
    INSERT INTO article_list (id,article_id,title,create_user,category,description,create_time) VALUES(REPLACE(UUID(),"-",""),"hhh","sss","sss",1,"description","2020-07-31 10:40:12");