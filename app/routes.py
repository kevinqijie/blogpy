from flask import request

from app import app
from app.article import getArticleLists


@app.route('/getArticleList/<category>/<page>')
def getArticleList(category,page):
    return getArticleLists(category,page)