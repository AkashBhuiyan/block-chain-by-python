from block import Block
import os
import json
import constant as cnst
import requests
from utils import dict_to_object
import block_chain
import glob

from block_chain import BlockChain

def sync_local():

    local_chain = BlockChain()

    if os.path.exists(cnst.BLOCK_CHAIN_DIR):
        for filepath in glob.glob(os.path.join(cnst.BLOCK_CHAIN_DIR, '*.json')):
            with open(filepath, 'r') as block_file:
                try:
                    block_info = json.load(block_file)
                except:
                    print(filepath)
                block_object = dict_to_object(block_info=block_info)
                local_chain.chainList.append(block_object)

    return local_chain

def syns_all(save_data=False):
    best_chain = sync_local()
    for peer in cnst.PEERS:

        peer_block_chain_url = peer + 'blockchain'

        try:
            req = requests.get(peer_block_chain_url)
            peer_blockchain_dict = req.json()
            peer_blocks = [dict_to_object(bcDict) for bcDict in peer_blockchain_dict]
            peer_chain = BlockChain()
            peer_chain.chainList = peer_blocks

            if block_chain.isValid(chainList=peer_blocks) and len(peer_chain.chainList) > len(best_chain.chainList):
                best_chain = peer_chain
        except requests.exceptions.ConnectionError as e:
            print(e)

    if save_data:
        best_chain.save_block_chain()

    return best_chain


def sync(save=False):
    return syns_all(save_data=save)


if __name__=='__main__':
    node_blocks = sync()

