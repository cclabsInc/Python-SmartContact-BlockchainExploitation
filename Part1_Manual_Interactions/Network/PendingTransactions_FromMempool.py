# 2023 Console Cowboys Python Smart Contract/blockchain Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io
import asyncio
import json
from web3 import Web3
from websockets import connect

#Note there are some issues with older websocket libraries soooo do the following: 
#pip install --upgrade web3
#pip install --upgrade websockets
#--------------------------Connection Setup stuff -------------------------------#
INFURA_WS = ''
INFURA_HTTP = ''
web3 = Web3(Web3.HTTPProvider(INFURA_HTTP))
print(f'Connected via HTTP: {web3.isConnected()}')
#--------------------------Connection Setup stuff -------------------------------#


def EventHandler(pending_tx): 
    """Takes in a subscription transacton response as pending_tx
       Then currently prints out data or can be modified for whatever"""
    transaction = json.loads(pending_tx)
    txHash = transaction['params']['result']
    #print(f'Transaction Hash: {txHash}')
    print(web3.eth.get_transaction(txHash))


#--------------------------Start Subscribe Pending TX -------------------------------#
#This code actually grabs the pending transactons from the mempool
#Reference: https://docs.alchemy.com/reference/newpendingtransactions
#           https://websockets.readthedocs.io/en/3.4/intro.html
async def subscribePendingTX():
    """Subscribes to the mempool listening for pending transactions
       Sends off the responses to be processed by the eventhandler function"""
    async with connect(INFURA_WS) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
       
        while True:
            try:
                pending_tx = await asyncio.wait_for(ws.recv(), timeout=15)
                EventHandler(pending_tx)

            except KeyboardInterrupt:
                exit()
            except:
                pass
#--------------------------End Subscribe Pending TX -------------------------------#

if __name__ == "__main__":
        asyncio.run(subscribePendingTX())
