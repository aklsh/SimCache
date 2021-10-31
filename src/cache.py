class cacheBlock:
    def __init__(self):
        self.tag = None
        self.valid = False
        self.dirty = False

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
    def __init__(self, assoc, replacementPolicy:str):
        self.blocks = []
        for _ in range(assoc):
            self.blocks.extend([cacheBlock()])
        self.replacementPolicy = replacementPolicy

    def insert(self, newBlock):
        index = -1
        for i, block in enumerate(self.blocks):
            if block.tag == None: # empty block
                index = i
                break
        if index == -1: # no empty block - replace
            return

class cache:
    def __init__(self, numSets, assoc, replacementPolicy):
