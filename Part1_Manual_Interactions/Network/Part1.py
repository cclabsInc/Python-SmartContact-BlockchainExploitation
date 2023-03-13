# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from web3 import Web3

#Make Connection To Blockchain
INFURA = ''
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.isConnected()}')

block = web3.eth.get_block('latest')

#Monitoring for Approve Functions: 
for transaction in block['transactions']:
    value = web3.eth.get_transaction(web3.toHex(transaction))
    if '095ea7b3' in value['input']:
        print(web3.toHex(value['hash']))
        
        
#See Video for other operations we performed with transactions and blocks.....
#This is just the final code from a specific operation with bytecode monitoring
