# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io

from web3 import Web3
import asyncio, json

#---------------------- Start Setup Stuff-----------------------------------------#
#Make Connection To local Ganache Blockchain
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))

#Setup Contract Communications
target_address = ''
target_abi = json.loads('')
target = web3.eth.contract(address=target_address, abi=target_abi)
#---------------------- End Setup Stuff-----------------------------------------#

#----------------Handle output from code doing real things---------------------------#
def EventHandler(event): 
    event = Web3.toJSON(event)
    event = json.loads(event)
    print(event["args"]["sender"], event["args"]["value"], event["args"]["message"])
#----------------------------End Handing of output-----------------------------------#
    
    
#---------------------Start of Code thats actually doing real things------------#
#-------------------------------------------------------------------------------#
#Keep Polling for Events and send to Handler for printing
#But only if they match the DepositLog Events
async def EventLogLoop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            EventHandler(event)
        await asyncio.sleep(poll_interval)

#Create an event filter for DepositLog subscription
#Run the EventLogLoop with asyncio Every 2 seconds to poll for new events
def main():
    event_filter = target.events.DepositLog.createFilter(fromBlock='latest')
    asyncio.run(EventLogLoop(event_filter, 2))

#-------------------------------------------------------------------------------#
#---------------------End of Code thats actually doing real things------------#

if __name__ == "__main__": 
    main()
