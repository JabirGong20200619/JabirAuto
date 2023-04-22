from flask import Flask, jsonify, request
#权限模块 https://github.com/raddevon/flask-permissions
#from flask_permissions.core import Permissions
import os, json
import app
import environment as e
#读取启动环境
environment = e.read()

#普通json带error_code风格使用此app示例
app = Flask(__name__)
from app.Controllers import caseManager