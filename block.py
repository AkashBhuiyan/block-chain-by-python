from datetime import datetime
import hashlib

class Block:
    
    def __init__(self, timeStamp, previousHash, data):
        self.index = 0
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.data = data
        self.hash = ""
        
    def calculate_hash(self):
        data = str(self.timeStamp) + str(self.previousHash) + str(self.data)
        #print(data)
        result = hashlib.sha256(data.encode())
        return result.hexdigest()
        
    def block(self):
        self.hash = self.calculate_hash()

        
     
        
# if __name__=='__main__':
#     b = Block(timeStamp=datetime.now(), previousHash=None, data="{sender:Akash,receiver:Ovi,amount:10}")
#     b.block()
#     print(b.hash)
        