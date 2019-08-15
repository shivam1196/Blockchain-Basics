import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = self.timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        string = str(timestamp) + data + str(previous_hash)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def timestamp(self):
        return datetime.datetime.now().timestamp()


class BlockChain:
    def __init__(self):
        self.last_block = None
        self.blocks = {}

    def append(self, data):
        block = None
        if self.last_block is None:
            block = Block(data, 0)
            self.last_block = block
            self.blocks[block.hash] = block
        else:
            block = Block(data, self.last_block.hash)
            self.last_block = block
            self.blocks[block.hash] = block
        return block

    def print_chain(self):
        if self.last_block is None:
            print("Block chain is empty")
            return
        hash_code = self.last_block.hash
        while hash_code is not 0:
            block = self.blocks[hash_code]
            print("data:", block.data, "timestamp:", block.timestamp)
            hash_code = block.previous_hash


if __name__ == "__main__":
    block_chain = BlockChain()
    block_chain.append("This is my Block 1")
    block_chain.append("This is my Block 2")
    block_chain.append("Block 3")
    block_chain.append("Block 4")
    block_chain.print_chain()

    # Results
    # data: Block 4 timestamp: 1560537500.016537
    # data: Block 3 timestamp: 1560537500.01653
    # data: This is my Block 2 timestamp: 1560537500.01652
    # data: This is my Block 1 timestamp: 1560537500.016491

    block_chain = BlockChain()
    block_chain.print_chain()
    # Block chain is empty

    block_chain = BlockChain()
    block_1 = block_chain.append("New Block")
    block_2 = block_chain.append("this is my new block 2")
    print("Is previous hash of block is equal to hash of block behind it: ", block_2.previous_hash is block_1.hash)
    # Is previous hash of block is equal to hash of block behind it:  True
