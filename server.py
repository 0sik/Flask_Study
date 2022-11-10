from flask import Flask
import random

app = Flask(__name__)

#나중에 여기 데이터베이스를 가져오는 코드를 넣으면 데이터 베이스랑도 연결 가능
topics = [
    {'id': 1,'title':'html','body':'html is ...'},
    {'id': 2,'title':'css','body':'css is ...'},
    {'id': 3,'title':'js','body':'js is ...'}
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}"/>{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/"/>WEB</a><h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello,Web
        </body>
    </html>
    '''
 
@app.route('/main')
def index2():
    return 'flask'

@app.route('/read/<id>/')
def read(id):
    return 'READ'+id

app.run(port=5001,debug=True)