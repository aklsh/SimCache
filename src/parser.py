'''
SimCache: A Python-Based Uniprocessor Cache Simulator
Authors: Akilesh K, Arjun Menon V
Assignment 6, Computer Architecture
Nov 2021
Config Parser Module
'''

class inputParser:
    def __init__(self, inputFile:str):
        self.inputFile = inputFile
    def parse(self):
        replacementPolicies = ["RANDOM", "LRU", "PLRU"]
        with open(self.inputFile) as f:
            lines = f.read().splitlines()
        cacheSize = int(lines[0].split("\t")[0])
        blockSize = int(lines[1].split("\t")[0])
        associativity = int(lines[2].split("\t")[0])
        associativityType = "SA"
        if associativity < 2:
            if associativity == 1:
                associativityType = "DM"
            else:
                associativityType = "FA"
        replacementPolicy = replacementPolicies[int(lines[3].split("\t")[0])]
        traceFile = lines[4].strip()
        return cacheSize, blockSize, associativity, associativityType, replacementPolicy, traceFile

if __name__ == "__main__":
    parser = inputParser("test/input.txt")
    cs, bs, a, at, rp, tf = parser.parse()
    print("Cache size: {}".format(cs))
    print("Block size: {}".format(bs))
    print("Associativity: {}".format(a))
    print("  Type: {}".format(at))
    print("Replacement Policy: {}".format(rp))
    print("Trace File: {}".format(tf))
