from cache import cache
from parser import inputParser, traceParser

def main(): 
    confParser = inputParser("input/conf.txt")
    cacheSize, blockSize, assoc, assocType, replacementPolicy, traceFile = confParser.parse()
    if assocType == "SA":
        numSets = int(cacheSize / (blockSize * assoc))
    elif assocType == "DM":
        numSets = int(cacheSize / blockSize)
        assoc = 1
        replacementPolicy = "RANDOM"
    elif assocType == "FA":
        assoc = int(cacheSize/blockSize)
        numSets = 1
    else:
        raise ValueError("Invalid Associativity Type" + " " + assocType)
    cacheModule = cache(numSets, assoc, replacementPolicy)
    tracer = traceParser(traceFile)
    requests = tracer.parse()
    for request in requests:
        address = request[0]
        accessType = request[1]
        cacheModule.memRequest(address, accessType)
    cacheModule.printStats()
    return

if __name__ == "__main__":
    main()
