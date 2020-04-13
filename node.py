from flask import Flask
import sync
from flask import jsonify, request
import json
import sys


node = Flask(__name__)

sync.sync(save=True)

@node.route('/blockchain', methods=['GET'])
def blockchain():

    node_blocks = sync.sync_local()

    blocks = []
    for dic in node_blocks.chainList:
        blocks.append(dic.as_dict())
    return jsonify(blocks)
@node.route('/peer-mined', methods=['POST'])
def peer_mined():
    req_block_data = request.get_json()
    print(req_block_data)

if __name__== '__main__':

    if len(sys.argv) >= 2:
        port = sys.argv[1]
    else:
        port = 5000

    node.run(host='127.0.0.1', port=port)
