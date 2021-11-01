def LRUupdate(LRUCounters, hitBlockIndex):
    currCount = LRUCounters[hitBlockIndex]
    if currCount == -1: # block was previously free.
        for i in range(len(LRUCounters)):
            if LRUCounters[i] != -1:
                LRUCounters += 1
    else: # block already existing in cache - update only those accessed from prev access to now
        for i in range(len(LRUCounters)):
            if ((LRUCounters[i] != -1) and (LRUCounters[i] < currCount)):
                LRUCounters[i] += 1
    LRUCounters[hitBlockIndex] = 0
    return LRUCounters


def LRUreplace(LRUCounters):
    maxCounter = LRUCounters[0]
    replacementCandidate = 0
    for i in range(len(LRUCounters)):
        if LRUCounters[i] > maxCounter:
            replacementCandidate = i
            maxCounter = LRUCounters[i]
    return replacementCandidate
