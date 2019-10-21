import click
import datetime

# Object builder for storing each transaction in each document #
class transaction(object):
    transDate = datetime.date.today()
    comment = ''
    account = ''
    money = ''

    def __init__(self, transDate, comment, account, money):
        self.transDate = transDate
        self.comment = comment
        self.accoun =  account
        self.money = money

def createTransaction(transDate, comment, account, money):
    trans = transaction(transDate, comment, account, money)
    return trans
# End of object builder block #

def readFile():
    path = 'ledger-sample-files/{}'
    trans = []
    count = 0
    with open('ledger-sample-files/index.ledger', 'r') as index_file:
        for line in index_file:
            with open(path.format(line.split(" ")[1].replace('\n', '')), 'r') as ledgerFile:
                for line in ledgerFile:
                    if line.startswith(';'):
                        continue
                    if line.startswith('\n'):
                        continue
                    if line.startswith('2'):
                        trans[count] = line
                    if line.startswith('\s'):
                        trans[count].append()
                        count =+ 1

                    
                    #Insert into an object, excluding lines starting with ';'

if __name__=="__main__":
    readFile()