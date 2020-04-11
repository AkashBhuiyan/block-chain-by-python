from block import Block
from datetime import datetime
import json
import pickle

class BlockChain:
    chainList = []
    
    def __init__(self):
        self.add_genesis_block()   
    
    def create_genesis_block(self):
        block = Block(datetime.now(), None, '{}')
        block.block()
        return block
    
    def add_genesis_block(self):
        block = self.create_genesis_block()
        self.chainList.append(block)
         
    def get_latest_block(self):
        return self.chainList[-1]
    
    def add_block(self, block):
        latestBlock = self.get_latest_block()
        block.index = latestBlock.index + 1
        block.previousHash = latestBlock.hash
        block.hash = block.calculate_hash()
        self.chainList.append(block)
    
#validation    
def isValid(chainList):
    
    for i in range(len(chainList)-1):
        previousBlock = chainList[i]
        currentBlock = chainList[i+1]
        
        if currentBlock.hash != currentBlock.calculate_hash():
            return False
        
        if currentBlock.previousHash != previousBlock.hash:
            return False
    
    return True
        
        
if __name__=="__main__":
    blockChain = BlockChain()
    blockChain.add_block(Block(timeStamp=datetime.now(), previousHash=None, data="{sender:Akash,receiver:Ovi,amount:10}"))
    blockChain.add_block(Block(timeStamp=datetime.now(), previousHash=None, data="{sender:Akash,receiver:Ovi,amount:30}"))
    blockChain.add_block(Block(timeStamp=datetime.now(), previousHash=None, data="{sender:Akash,receiver:Ovi,amount:50}"))

    print(isValid(blockChain.chainList))
    
    