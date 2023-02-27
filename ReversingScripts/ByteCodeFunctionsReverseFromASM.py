# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from pyevmasm import  disassemble_hex 
import re, requests
from colorama import Fore


disass = disassemble_hex("<ADD_BYTECODE").split("\n")
signatures = [line.strip() for line in open("SignaturesDB.txt")]
signature_from_asm = []

def getFunctionsFromASM():
    for instruction in disass: 
        if (len(instruction) == 16) and (instruction[-8:] not in signature_from_asm):
                signature_from_asm.append(instruction[-8:])


def onlineFunctionLookup():
    for signature in signature_from_asm:
        if signature in signatures:
                r = requests.get(f"https://api.etherface.io/v1/signatures/hash/all/{signature}/1", verify=False)
                matches = re.findall(r'(?<="text":")(.*?)(?=",)', r.text)

            
                if r.status_code == 200 and matches :
                    print(f' {Fore.GREEN}Signature found:')
                    print(f'{Fore.WHITE}Possible Function Values for {signature}:')
                    for match in matches:   
                        print(f'{Fore.YELLOW}            - {match}')
                    
                elif r.status_code != 200:
                    print(f'{Fore.RED}Signature Not Found: {signature} returned {r.status_code} (Might be False Positive)')

    print(Fore.WHITE)

getFunctionsFromASM()
onlineFunctionLookup()
