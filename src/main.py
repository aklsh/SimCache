'''
SimCache: A Python-Based Uniprocessor Cache Simulator
Authors: Akilesh K, Arjun Menon V
Assignment 6, Computer Architecture
Nov 2021
Main Module
'''
from parser import inputParser
from cache import cache
from tqdm import tqdm
import math

def main():
    configPath = "test/input.txt"
    parser = inputParser(configPath)
    cSize, bSize, assoc, assocType, replacementPolicy, traceFile = parser.parse()
    # check if cSize, bSize and assoc are powers of 2:
    if (isNotPow2(cSize)):
        print("ERROR: Cache Size is not Power of 2, exiting...")
        exit()
    elif(isNotPow2(bSize)):
        print("ERROR: Block Size is not Power of 2, exiting...")
        exit()
    elif(isNotPow2(assoc)):
        print("ERROR: Associativity is not Power of 2, exiting...")
        exit()
    numSets = cSize//(bSize * assoc)
    cacheDUT = cache(numSets, assoc, replacementPolicy)
    with open(traceFile) as f:
        reqs = f.read().splitlines()
    print("---------- Cache Configuration  ----------")
    print("\tCache Size: {} \n\tBlock Size: {} \
            \n\tNumber of Sets: {} \n\tAssociativity: {} \n\tReplacement Policy: {}\
            ".format(cSize, bSize, numSets, assoc, replacementPolicy))
    print("------------------------------------------\n")
    print("Beginning Simulation ...")
    for i in tqdm(range(len(reqs))):
        req = reqs[i]
        address, accessType = req.split()
        blockAddress = int(address, 0)//bSize
        cacheDUT.memRequest(blockAddress, accessType)
    # Dumping out all metrics
    print("\n----------- Simulation Results -----------")
    print("\tNum Accesses: {}".format(cacheDUT.numAccesses))
    print("\tNum Reads: {}".format(cacheDUT.numReads))
    print("\tNum Writes: {}".format(cacheDUT.numWrites))
    print("\tNum Hits: {}".format(cacheDUT.numHits))
    print("\tNum Misses: {}".format(cacheDUT.numMisses))
    print("\tNum Compulsory Misses: {}".format(cacheDUT.numCompMisses))
    print("\tNum Capacity Misses: {}".format(cacheDUT.numCapMisses))
    print("\tNum Conflict Misses: {}".format(cacheDUT.numConfMisses))
    print("\tNum Read Misses: {}".format(cacheDUT.numReadMisses))
    print("\tNum Write Misses: {}".format(cacheDUT.numWriteMisses))
    print("\tNum Dirty Evictions: {}".format(cacheDUT.numDEs))
    print("------------------------------------------\n")
    return

def isNotPow2(val):
    log_val = math.log(val, 2)
    res_val = log_val - int(log_val)
    if (res_val == 0):
        return False
    else:
        return True

if __name__ == "__main__":
    print("------------- SimCache: A Python-Based Uniprocessor Cache Simulator -------------\n")
    main()
