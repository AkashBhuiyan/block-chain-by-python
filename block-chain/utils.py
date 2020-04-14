import constant as cnst
import datetime

def dict_to_object(block_info):
    from block import Block

    block_object = Block()
    block_object.index = block_info['index']
    block_object.timeStamp = block_info['timeStamp']
    block_object.previousHash = block_info['previousHash']
    block_object.transactions = block_info['transactions']
    block_object.hash = block_info['hash']
    block_object.nonce = block_info['nonce']

    return block_object

def object_to_dict(object):

    transactions = []
    for trans in object:
        transactions.append(trans.as_dict())

    return transactions


def transaction_list_to_dict(self):
    trans_str = "["
    print(type(self.transactions), self.transactions)
    for i, trans in enumerate(self.transactions):
        dict_val = "{"
        for k, v in trans.as_dict().items():
            dict_val += "'" + str(k) + "'" + ":" + "'" + str(v) + "'" + ","
        dict_val += "}"
        if i < len(self.transactions):
            trans_str += dict_val + ","
        else:
            trans_str += dict_val
    self.transactionHistory += trans_str + "]"


def create_new_block_from_previous_block(previousBlock=None, transactions=None, timeStamp=None):
    from block import Block
    new_block = Block()
    if not previousBlock:
        # index zero and arbitrary previous hash
        new_block.index = 0
        new_block.previousHash = ''
    else:
        new_block.index = int(previousBlock.index) + 1
        new_block.previousHash = previousBlock.hash

    if not transactions:
        filename = '%sdata.txt' % (cnst.BLOCK_CHAIN_DIR)
        with open(filename, 'r') as data_file:
            new_block.transactions = data_file.read()

    if not timeStamp:
        new_block.timeStamp = datetime.now()

    return new_block
