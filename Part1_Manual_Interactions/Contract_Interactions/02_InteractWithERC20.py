# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from web3 import Web3

#Make Connection To Blockchain
INFURA = '<CONNECTION_URL>'
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.isConnected()}')

#Make Connection to Target Contract
target_address = web3.toChecksumAddress("TARGET ERC20 Contract")  
target_abi = 'TARGET_ABI'
target = web3.eth.contract(address=target_address, abi=target_abi)

#Pull InfoFrom an ERC20 Token
print(target.functions.name().call())
print(target.functions.symbol().call())

#Contract values are based on the decimals..
#to get the readable total supply divide by number of decimals on the contract
print(target.functions.totalSupply().call() / 10 ** target.functions.decimals().call())

#Or just use web3 libraries to handle it
print(web3.fromWei(target.functions.totalSupply().call(), 'ether'))
