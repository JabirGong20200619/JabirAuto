# coding=utf-8
'''

@author: Jabir
'''

import environment
environment.init("run") 
from app import app
from flask_cors import CORS
app = app
CORS(app, supports_credentials=True)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=500)
    pass