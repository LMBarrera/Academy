import click
import itertools

@cli.command()
def prnt(ledgerFile=None):
    with open('ledger-sample-files/index.ledger', 'r') as index_file:
        if ledgerFile != None:
            for line in index_file:
                if line.split(" ")[1].replace('\n', '').startswith(ledgerFile):
                    with open(line.split(" ")[1].replace('\n', ''), "r") as file:
                        #Uses itertools to slice the first line and start using the file from the second line. 
                        for line in itertools.islice(file, 1, None):
                            #Prints each line without adding unnecesary new lines. 
                            print(line, end='')
        if ledgerFile == None:




    ledgerFileNames = ['Bitcoin', 'Expenses', 'Income', 'Payable', 'Receivable']
    i = 0
    path = "ledger-sample-files/{}.ledger"

    if ledgerFile == None:
        for name in ledgerFileNames:
            #Opens file in read mode, and saves it in a variable called file.
            with open(path.format(ledgerFileNames[i]), "r") as file:
                #Uses itertools to slice the first line and start using the file from the second line. 
                for line in itertools.islice(file, 1, None):
                    #Prints each line without adding unnecesary new lines. 
                    print(line, end='') 
                i += 1
                print('\n')

    if ledgerFile != None:
        with open(path.format(ledgerFile), "r") as file:
                #Uses itertools to slice the first line and start using the file from the second line. 
                for line in itertools.islice(file, 1, None):
                    #Prints each line without adding unnecesary new lines. 
                    print(line, end='')

#def registerFormat(ledgerFile=None):
#    fileReader(ledgerFile)

#def balanceFormat(ledgerFile=None):
#    fileReader(ledgerFile)

re.split(r'\s{2,}', line)

@click.group()
def cli():
    pass

@cli.command()
@click.command()
@click.option('--sort', default='d', type=char)
@click.option('--price-db', is_flag=True)
@click.option('--file', is_flag=True)
def main(sort, price_db, file):

cli.add_command(main)
cli.add_command(prnt)

if __name__=="__main__":
    prnt('Bitcoin')