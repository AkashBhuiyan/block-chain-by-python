from datetime import datetime
import hashlib
from transaction import Transaction

import os, json
import constant as cnst

class Block:

    def __init__(self, timeStamp=datetime.now(), previousHash="", transactions=None):
        self.index = 0
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.transactions = transactions
        self.hash = ""
        self.nonce = 0
        self.transactionHistory = ''
        if self.transactions != None:
            self.transaction_list_to_dict()


    def as_dict(self):
        info = {}
        info['index'] = str(self.index)
        info['timeStamp'] = str(self.timeStamp)
        info['previousHash'] = str(self.previousHash)
        info['transactionHistory'] = str(self.transactionHistory)
        info['hash'] = str(self.hash)
        info['nonce'] = str(self.nonce)
        return info
        
        
    def transaction_list_to_dict(self):
        trans_str = "["
        print(type(self.transactions), self.transactions)
        for i, trans in enumerate(self.transactions):
            dict_val = "{"
            for k, v in trans.as_dict().items():
                dict_val += "'" + str(k) + "'" + ":"+ "'" + str(v) + "'" + ","
            dict_val += "}"
            if i < len(self.transactions):
                trans_str += dict_val + ","
            else:
                trans_str += dict_val
        self.transactionHistory += trans_str + "]"
                   
    def calculate_hash(self):
        data = str(self.timeStamp) + str(self.previousHash) + str(self.transactionHistory) + str(self.nonce)
        
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
        print(self.nonce)


    def __equal__(self, other):
        return (self.index == other.index and
                self.timeStamp == other.timestamp and
                self.previousHash == other.previousHash and
                self.hash == other.hash and
                self.transaction == other.transaction and
                self.nonce == other.nonce
                )
        
    def save(self, dir):
        index_string = str(self.index).zfill(6) #front of zeros so they stay in numerical order
        filename = '%s/%s.json' % (dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.as_dict(), block_file)


        
if __name__=='__main__':
    block = Block(timeStamp=datetime.now(), previousHash="", transactions=[Transaction('Akash', 'Ovi', 10), Transaction("Kam", "Kim", 10)])
    

    if not os.path.exists(cnst.BLOCK_CHAIN_DIR):
        os.mkdir(cnst.BLOCK_CHAIN_DIR)
        
    if os.listdir(cnst.BLOCK_CHAIN_DIR) == []:
        block.mine(2)
        block.save(dir=cnst.BLOCK_CHAIN_DIR)
    print(block.nonce, block.hash)
