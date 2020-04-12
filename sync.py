from block import Block
import os
import json
import constant as cnst

def sync():
    node_blocks = []
    a = ''
    if os.path.exists(cnst.BLOCK_CHAIN_DIR):
        for filename in os.listdir(cnst.BLOCK_CHAIN_DIR):
            if filename.endswith('.json'):
                filepath = '%s/%s' % (cnst.BLOCK_CHAIN_DIR, filename)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)

                    block_object = Block()
                    block_object.index = block_info['index']
                    block_object.timeStamp = block_info['timeStamp']
                    block_object.previousHash = block_info['previousHash']
                    block_object.transactionHistory = block_info['transactionHistory']
                    block_object.hash = block_info['hash']
                    block_object.nonce = block_info['nonce']

                    node_blocks.append(block_object)

    return node_blocks


if __name__=='__main__':
    node_blocks = sync()
