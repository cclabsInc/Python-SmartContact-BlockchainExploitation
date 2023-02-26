# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

import re, requests
from colorama import Fore

bytecode = "<ADD_TARGET_BYTECODE"
signatures = "signaturesDB.txt"

#--------------Start Signature Loop-----------------------------#
for signature in open(signatures, 'r'):
    signature = str(signature.strip())
 
 #Does this signature Exist in Bytecode, if so do a lookup
    if signature in bytecode:
        r = requests.get('https://api.etherface.io/v1/signatures/hash/all/'+signature+"/1", verify=False)
        matches = re.findall(r'(?<="text":")(.*?)(?=",)', r.text)
        
 #Print things out and do error checks       
        if r.status_code == 200 and matches :
            print(f' {Fore.GREEN}Signature found:')
            print(f'{Fore.WHITE}Possible Function Values for {signature}:')
            for match in matches:   
                print(f'{Fore.YELLOW}            - {match}')
                
        elif r.status_code != 200:
            print(f'{Fore.RED}Signature Not Found: {signature} returned {r.status_code} (Might be False Positive)')
#--------------END Signature Loop-----------------------------#

print(Fore.WHITE)
