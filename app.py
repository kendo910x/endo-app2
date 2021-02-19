#coding: utf-8
from flask import Flask, request, make_response
app = Flask(__name__, static_folder='.')
@app.route('/')
def index():
    html = '<html><body>endo app<br>Good-bye World!!</body></html>'
    return(html)
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8081) 
