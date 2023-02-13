# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from web3 import Web3

#Make Connection To Blockchain
INFURA = '<ConnectionURL>'
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.isConnected()}')

#Make Connection to Target Contract
target_address = web3.toChecksumAddress("")
target_abi = ""
target = web3.eth.contract(address=target_address, abi=target_abi)
