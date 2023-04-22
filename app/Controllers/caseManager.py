# coding=utf-8
# 导包
from flask import Flask, jsonify, request
from app import app
# 固定格式 实例化
# app = Flask(__name__)

# 路由
@app.route("/caseManager",methods=["GET"])
def caseManager():
    return "hello"


if __name__ == '__main__':
# 启动服务
    # app.run()
    pass