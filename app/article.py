from app.date import now
from app.sqlList import testmsg, push
import uuid


def getArticleLists(category,page):
    return testmsg()
def postArticles(data):
    try:
        date = now()
        push(data["title"],data["createUser"],data["category"],data["description"],data["content"],date)
    except Exception:
        print(Exception)
        return "error"
    return "ok"