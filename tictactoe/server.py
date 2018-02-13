import os
from random import shuffle

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, send_from_directory, jsonify

from . game import do_move


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return send_from_directory("templates", "index.html")

@app.route('/<string:name>')
def static_files(name):
    return send_from_directory("templates", name)

@app.route('/next_move')
def next_move():
    ret = do_move( request.args )
    print(" Playing on position {}".format(ret))
    return jsonify(result=ret)

