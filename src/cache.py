import random
from replacePLRU import Tree
from replaceLRU import LRUreplace, LRUupdate
import math
from copy import copy

class cacheBlock:
    def __init__(self, tag=None):
        self.tag = tag
        if tag == None:
            self.valid = False
        else:
            self.valid = True
        self.dirty = False

    def print(self):
        print("Valid: {}    Dirty: {}    Tag: {}".format(self.valid, self.dirty, self.tag))

    def access(self, accessType:str):
        if self.valid is True:
            if accessType == 'r':
                pass
            if accessType == 'w':
                self.dirty = True
        else:
            raise ValueError("Accessing Invalid Cache Block")

class cacheSet:
    def __init__(self, assoc:int, replacementPolicy:str):
        self.assoc = assoc
        self.blocks = []
        for _ in range(assoc):
            self.blocks.extend([cacheBlock()])
        self.replacementPolicy = replacementPolicy
        if self.replacementPolicy == "LRU":
            self.LRUCounter = []
            for _ in range(self.assoc):
                self.LRUCounter.extend([-1])
        if (self.replacementPolicy == "PLRU"):
            numStages = int(math.log(assoc,2))
            self.PLRUTree = Tree(numStages)

    def accessBlock(self, blockTag, accessType):
        for idx, block in enumerate(self.blocks):
            idx += 1
            if block.tag == blockTag: # block in cache - return hit (True)
                block.access(accessType)
                if (self.replacementPolicy == "PLRU"):
                    self.PLRUTree.traverse(idx)
                elif self.replacementPolicy == "LRU":
                    self.LRUCounter = LRUupdate(self.LRUCounter, idx)
                return True, None
        # if comes here, then block with given tag not in cache
        # bring to cache, and return miss (False)
        newBlock = cacheBlock(blockTag)
        status, replaceBlock = self.insert(newBlock)
        if status == 0:
            return False, None
        else:
            return False, replaceBlock

    def replace(self):
        if self.replacementPolicy == "RANDOM":
            replacementCandidate = random.randint(0,self.assoc-1)
        elif self.replacementPolicy == "LRU":
            replacementCandidate = LRUreplace(self.LRUCounter)
        elif self.replacementPolicy == "PLRU":
            replacementCandidate = self.PLRUTree.getVictim()
        else:
            raise ValueError("Invalid Replacement Policy for cache set: ", self.replacementPolicy)
        return replacementCandidate

    def insert(self, newBlock):
        index = -1
        replacedBlock = None
        for i, block in enumerate(self.blocks):
            if block.tag == None: # empty block
                index = i
                if (self.replacementPolicy == "PLRU"):
                    self.PLRUTree.traverse(i)
                elif self.replacementPolicy == "LRU":
                    self.LRUCounter = LRUupdate(self.LRUCounter, i)
                break
        if index == -1: # no empty block - replace
            replacementCandidate = self.replace()
            replacedBlock = copy(self.blocks[replacementCandidate])
            self.blocks[replacementCandidate].valid = True
            self.blocks[replacementCandidate].dirty = False
            self.blocks[replacementCandidate].tag = newBlock.tag
            return 1, replacedBlock
        return 0, None

class cache:
    def __init__(self, numSets, assoc, replacementPolicy):
        self.numSets = numSets
        self.assoc = assoc
        self.replacementPolicy = replacementPolicy
        self.cacheSets = []
        for _ in range(self.numSets):
            self.cacheSets.extend([cacheSet(self.assoc, self.replacementPolicy)])

    def memRequest(self, blockAddress, accessType):
        setIndex = blockAddress % self.numSets
        blockTag = blockAddress//self.numSets
        self.cacheSets[setIndex].accessBlock(blockTag, accessType)
