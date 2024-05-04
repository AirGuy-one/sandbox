from blockchain.chain import Blockchain
from blockchain.block import Block


class BlockchainService:
    def __init__(self):
        self.blockchain = Blockchain()
        self.block = self._create_new_block
        self.__init__()

    @property
    def _create_new_block(self):
        return Block()
