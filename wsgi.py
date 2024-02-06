# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os

from app import app

PORT = 3000

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler

    server = WSGIServer(('0.0.0.0', PORT), app, log=None, handler_class=WebSocketHandler)
    server.serve_forever()
