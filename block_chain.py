from block import Block
from datetime import datetime
import json, os
import pickle
from transaction import Transaction
import constant as cnst

class BlockChain:
    chainList = []
    difficulty = 3
    pendingTransaction = []
    reward = 1 #1 cryptocurrency
    
    def __init__(self):
        self.add_genesis_block()   
    
    def create_genesis_block(self):
        block = Block(datetime.now(), '', None)
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
        #block.hash = block.calculate_hash()
        block.mine(self.difficulty)
        self.chainList.append(block)

    def create_transaction(self, transaction):
        self.pendingTransaction.append(transaction)
        
    def process_pending_transaction(self, minerAddress):
        block = Block(datetime.now(), self.get_latest_block().hash, self.pendingTransaction)
        self.add_block(block=block)
        self.pendingTransaction = []
        self.create_transaction(Transaction(None, minerAddress, self.reward))
        
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
    
    
    startTime = datetime.now()

    blockChain = BlockChain()

    blockChain.create_transaction(Transaction("Akash", "Ovi", 10))
    blockChain.process_pending_transaction('Bhuiyan')
    
    blockChain.create_transaction(Transaction("Ovi", "Akash", 5))
    blockChain.process_pending_transaction('Bhuiyan')
    
    endTime = datetime.now()

    print(isValid(blockChain.chainList))

    if os.listdir(cnst.BLOCK_CHAIN_DIR) == []:
        for block in blockChain.chainList:
            block.save(dir=cnst.BLOCK_CHAIN_DIR)

    print('Duration : ', startTime, '-', endTime)

