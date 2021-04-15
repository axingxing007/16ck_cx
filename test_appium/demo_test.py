# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
import yaml

data = yaml.safe_load(open('data.yaml'))
print(data, type(data))
