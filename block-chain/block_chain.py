from block import Block
from datetime import datetime
from transaction import Transaction
import constant as cnst

class BlockChain:

    
    def __init__(self):
        self.chainList = []
        self.pendingTransaction = []
        self.reward = 1  # 1 cryptocurrency
    
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
        block.mine(cnst.DIFFICULTY)
        self.chainList.append(block)

    def create_transaction(self, transaction):
        self.pendingTransaction.append(transaction)
        
    def process_pending_transaction(self, minerAddress):
        block = Block(datetime.now(), self.get_latest_block().hash, self.pendingTransaction)
        self.add_block(block=block)
        self.pendingTransaction = []
        self.create_transaction(Transaction(None, minerAddress, self.reward))

    def find_block_by_hash(self, hash):
        for block in self.chainList:
            if block.hash == hash:
                return block

        return False

    def find_block_by_index(self, index):
        if len(self.chainList) <= index:
            return self.chainList[index]
        else:
            return False

    def save_block_chain(self):
        for block in self.chainList:
            block.save()

    def compare_two_chain_length(self, another):
        return len(self.chainList) > len(another.chainlist)

#validation    
def isValid(chainList):
    
    for i in range(len(chainList)-1):
        previousBlock = chainList[i]
        currentBlock = chainList[i+1]
        temp = chainList[i+1]
        temp.hash = ""
        temp.nonce = 0
        temp.mine(cnst.DIFFICULTY)

        if currentBlock.hash != temp.hash:
            return False

        if currentBlock.index == previousBlock.index:
            return False
        
        if currentBlock.previousHash != previousBlock.hash:
            return False
    
    return True
        
        
if __name__=="__main__":
    
    
    startTime = datetime.now()

    blockChain = BlockChain()
    blockChain.add_genesis_block()
    blockChain.create_transaction(Transaction("Akash", "Ovi", 10))
    blockChain.process_pending_transaction('A')

    blockChain.create_transaction(Transaction("Ovi", "Akash", 5))
    blockChain.process_pending_transaction('Bhuiyan')

    blockChain.create_transaction(Transaction("Alex", "Akash", 2))
    blockChain.process_pending_transaction('Ovi')
    
    endTime = datetime.now()

    print(isValid(blockChain.chainList))

    blockChain.save_block_chain()


    print('Duration : ', startTime, '-', endTime)

