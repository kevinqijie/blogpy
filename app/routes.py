from flask import request

from app import app
from app.article import getArticleLists, postArticles


@app.route('/getArticleList/<category>/<page>')
def getArticleList(category,page):
    return getArticleLists(category,page)
@app.route('/postArticle',methods=['POST'])
def postArticle():
    data = request.get_json()
    return postArticles(data)