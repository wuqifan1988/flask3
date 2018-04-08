#!/usr/bin/env python
from app import create_app, db
from flask_script import Manager

app = create_app('default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()