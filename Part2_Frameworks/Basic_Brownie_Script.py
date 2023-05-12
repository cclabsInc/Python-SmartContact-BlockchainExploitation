# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
#http://cclabs.io 
  
from brownie import accounts, HelloWorld_Bank

#Accounts from Ganache
account0 = accounts[0]
account1 = accounts[1]

#Deploy contract to local Ganache
def deployBank():
    bank = HelloWorld_Bank.deploy({"from":account0})
    return bank

#Simple bank interaction examples
def bankInteractions(bank):
    print(bank.getBalance())
    bank.deposit({"from":account0, "value": 1000000000000000000})
    bank.deposit({"from":account1, "value": 2000000000000000000})
    print(f'Account2: {bank.getBalance({"from":account0})}')
    print(f'Account1: {bank.getBalance({"from":account1})}')
    return 

#Main driver function
def main():
    bank = deployBank()
    bankInteractions(bank)
