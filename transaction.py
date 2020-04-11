class Transaction:
    
    def __init__(self, fromAddress, toAddress, amount):
        
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        
    def as_dict(self):
        return {'fromAddress': self.fromAddress, 'toAddress':self.toAddress, 'amount':self.amount}
    