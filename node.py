from flask import Flask
import sync

import json

node = Flask(__name__)

node_blocks = sync.sync()

@node.route('/blockchain', methods=['GET'])
def blockchain():

    node_blocks = sync.sync()

    blocks = []

    for block in node_blocks:
        blocks.append(block.as_dict())

    json_blocks = json.dumps(blocks)

    return json_blocks

if __name__== '__main__':
    node.run()
