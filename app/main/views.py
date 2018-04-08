# encoding:utf8
from pprint import pprint

import os
from flask import render_template, session, redirect, url_for, current_app, request

from . import main


@main.route('/git_push', methods=['GET', 'POST'])
def git_push_hook():

    git_info = request.json

    branch = git_info.get("ref").split("refs/heads/")[-1]

    env = "pre"

    if branch == "master":
        env = "pre"
    elif branch == "pre":
        pass
    else:
        env = "dev"

    # 触发构建
    command = "curl -X POST http://10.1.6.43:8081/job/market-api-test/build --user 2dfire:2dfire --data-urlencode " + \
              "json='{\"parameter\": [{\"name\":\"env\", \"value\":\"" + env + "\"}]}'"

    print(command)

    os.system(command)

    return "1234"

def get_jenkins():
    pass


@main.route('/get_jenkins_result',methods=['POST'])
def get_jenkins_result():
    command =123
    return 1234


@main.route('/test',methods=['POST','GET'])
def test():
    return render_template("test.html")




