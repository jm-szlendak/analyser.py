from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import utils
import resource
from analyse import analyse

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello</h1>"


@app.route('/analyse', methods=['POST'])
def analyze():
    print("analyzing")
    if not request.files:
        return utils.error_response('no file', 400)

    for file, file_storage in request.files.items():
        results = analyse(file_storage.stream)

        print('MEMORY USED:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024/1024)

        return jsonify({'response': 'ok', 'data': results}), 200
