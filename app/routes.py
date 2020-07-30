from app import app
from app.article import getArticleLists


@app.route('/getArticleList')
def getArticleList():
    return getArticleLists()