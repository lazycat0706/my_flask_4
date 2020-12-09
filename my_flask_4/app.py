from flask import Flask
from flask import render_template, request
import jieba
import sqlite3
from spider import get_html
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


@app.route('/')
@app.route('/s')
def search():
    return render_template('search.html')


@app.route('/sp')
def baidu_search():
    keyword = request.args.get('wd')
    return get_html(keyword)


# def db_connect():
#     conn = sqlite3.connect("testDB.db")
#     cursor = conn.cursor()
#     return cursor
#
#
# def sql_query(keyword, cursor):
#     sql = "select * from search_result where title like '%%s%' or content like '%%s%'" % (keyword, keyword)
#     cursor.excute(sql)
#     results = cursor.fetchall()
#     return results


if __name__ == '__main__':
    app.run(debug=True)
