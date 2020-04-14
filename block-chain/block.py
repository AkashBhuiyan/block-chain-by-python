from datetime import datetime
import hashlib
from transaction import Transaction

import os, json
import constant as cnst

import utils

class Block:

    def __init__(self, timeStamp=datetime.now(), previousHash="", transactions=None):
        self.index = 0
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.transactions = []
        self.hash = ""
        self.nonce = 0

        if transactions!= None:
            self.transactions = utils.object_to_dict(transactions)

    def as_dict(self):
        info = {}
        info['index'] = str(self.index)
        info['timeStamp'] = str(self.timeStamp)
        info['previousHash'] = str(self.previousHash)
        info['transactions'] = self.transactions
        info['hash'] = str(self.hash)
        info['nonce'] = str(self.nonce)
        return info
        

                   
    def calculate_hash(self):
        data = str(self.timeStamp) + str(self.previousHash) + str(self.transactions) + str(self.nonce)
        
        result = hashlib.sha256(data.encode())
        return result.hexdigest()
        
    def block(self):
        self.hash = self.calculate_hash()
        
    def mine(self, difficulty):
        leadingZeros = ''
        for i in range(difficulty):
            leadingZeros += "0"
            

        
        while self.hash == None or self.hash[0:difficulty] != leadingZeros:
            self.nonce += 1
            self.hash = self.calculate_hash()
        #print(self.nonce)

    def is_valid(self):
        self.calculate_hash()
        if str(self.hash[0:cnst.DIFFICULTY]) == '0' * cnst.DIFFICULTY:
            return True
        else:
            return False


    def __equal__(self, other):
        return (self.index == other.index and
                self.timeStamp == other.timestamp and
                self.previousHash == other.previousHash and
                self.hash == other.hash and
                self.transactions == other.transaction and
                self.nonce == other.nonce
                )

        
    def save(self):
        if not os.path.exists(cnst.BLOCK_CHAIN_DIR):
            os.mkdir(cnst.BLOCK_CHAIN_DIR)

        index_string = str(self.index).zfill(6) #front of zeros so they stay in numerical order
        filename = '%s/%s.json' % (cnst.BLOCK_CHAIN_DIR, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.as_dict(), block_file)


        
if __name__=='__main__':
    block = Block(timeStamp=datetime.now(), previousHash="", transactions=[Transaction('Akash', 'Ovi', 10), Transaction("Kam", "Kim", 10)])
    

    if not os.path.exists(cnst.BLOCK_CHAIN_DIR):
        os.mkdir(cnst.BLOCK_CHAIN_DIR)
        
    if os.listdir(cnst.BLOCK_CHAIN_DIR) == []:
        block.mine(2)
        block.save()
    print(block.nonce, block.hash)
