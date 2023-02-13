# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from web3 import Web3

#Make Connection To Blockchain
INFURA = '<ConnectionURL>'
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.isConnected()}')

#Make Connection to Target Contract
target_address = web3.toChecksumAddress("<TARGETWALLET")
print(web3.fromWei(web3.eth.getBalance(target_address), 'ether'))

#Differentiate between contract or wallet: 
print(web3.eth.getCode(target_address))  #Normal Wallet Address
print(web3.eth.getCode("TARGET_CONTRACT")) #chainlink Contract
