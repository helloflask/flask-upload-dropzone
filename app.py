# -*- coding: utf-8 -*-
"""
    Flask-upload-dropzone
    ===================================
    Summary: flask file upload with Dropzone.js.
    Author: Grey Li
    Repository: https://github.com/helloflask/flask-upload-dropzone
    License: MIT
"""
import os

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOADED_PATH'] = os.path.join(app.root_path, 'upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
