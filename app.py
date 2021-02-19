#coding: utf-8
from flask import Flask, request, make_response
import datetime
app = Flask(__name__, static_folder='.')
@app.route('/')
def index():
    dt_now = datetime.datetime.now()
    html = '<html><body>endo app<br>Good-bye World!!<br>' + dt_now.isoformat() + '</body></html>'
    return(html)
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8081) 
