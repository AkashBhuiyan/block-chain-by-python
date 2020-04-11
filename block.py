from datetime import datetime
import hashlib
from transaction import Transaction

class Block:
    transaction = list()
    def __init__(self, timeStamp, previousHash, transactions):
        self.index = 0
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.transactions = transactions
        self.hash = ""
        self.nonce = 0
        self.transactionHistoryStr = ''
        
    def transaction_list_to_string(self):
        self.transactionHistoryStr = ""
        for i, trans in enumerate(self.transactions):
            for k, v in trans.as_dict().items():
                if i < len(self.transaction)-1:
                    self.transactionHistoryStr += str(k) + " " + str(v) + ","
                else:
                    self.transactionHistoryStr += str(k) + " " + str(v)
        
                   
    def calculate_hash(self):
        data = str(self.timeStamp) + str(self.previousHash) + str(self.transactionHistoryStr) + str(self.nonce)
        
        result = hashlib.sha256(data.encode())
        return result.hexdigest()
        
    def block(self):
        self.hash = self.calculate_hash()
        
    def mine(self, difficulty):
        leadingZeros = ''
        for i in range(difficulty):
            leadingZeros += "0"
            
        self.transaction_list_to_string()
        
        while self.hash == None or self.hash[0:difficulty] != leadingZeros:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(self.nonce)


        
if __name__=='__main__':
    b = Block(timeStamp=datetime.now(), previousHash=None, transactions=[Transaction('Akash', 'Ovi', 10)])
    # b.block()
    # print(b.hash)
    b.transaction.append(Transaction("Kam", "Kim", 10))
    
    b.mine(2)

    print(b.nonce, b.hash)
