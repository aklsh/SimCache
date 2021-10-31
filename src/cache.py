import random

class cacheBlock:
    def __init__(self, tag=None):
        self.tag = tag
        self.valid = False
        self.dirty = False
        self.LRUCounter = 0

    def print(self):
        print("Valid: {}    Dirty: {}    Tag: {}".format(self.valid, self.dirty, self.tag))

    def access(self, accessType:str):
        try:
            if self.valid is True:
                if accessType == 'r':
                    pass
                if accessType == 'w':
                    self.dirty = True
            else:
                raise ValueError("Accessing Invalid Cache Block")
        except ValueError as e:
            print(repr(e))
            self.print()

class cacheSet:
    def __init__(self, assoc:int, replacementPolicy:str):
        self.blocks = []
        self.assoc = assoc
        for _ in range(assoc):
            self.blocks.extend([cacheBlock()])
        self.replacementPolicy = replacementPolicy

    def accessBlock(self, blockTag, accessType):
        for block in self.blocks:
            if block.tag == blockTag: # block in cache - return hit (True)
                block.access(accessType)
                return True
        # if comes here, then block with given tag not in cache
        # bring to cache, and return miss (False)

        return False
    def replace(self):
        if self.replacementPolicy == "RANDOM":
            replacementCandidate = random.randint(0,self.assoc-1)
        elif self.replacementPolicy == "LRU":
            # insert LRU code here
            replacementCandidate = random.randint(0,self.assoc-1)
        elif self.replacementPolicy == "PLRU":
            # insert PLRU code here
            replacementCandidate = random.randint(0,self.assoc-1)
        else:
            raise ValueError("Invalid Replacement Policy for cache set: ", self.replacementPolicy)
        return replacementCandidate

    def insert(self, newBlock):
        index = -1
        for i, block in enumerate(self.blocks):
            if block.tag == None: # empty block
                index = i
                break
        if index == -1: # no empty block - replace
            replacementCandidate = self.replace()

            return

class cache:
    def __init__(self, numSets=-1, assoc, replacementPolicy):
