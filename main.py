from blockchain.block import Block
from blockchain.chain import Blockchain

blockchain = Blockchain()

# Create a new block
block1 = Block(
    index=1,
    timestamp="02/01/2022",
    transactions=[{"sender": "Alice", "recipient": "Bob", "amount": 10}],
    previous_hash="0",
)
blockchain.add_block(block1)

# Create another block
block2 = Block(
    index=2,
    timestamp="03/01/2022",
    transactions=[{"sender": "Bob", "recipient": "Charlie", "amount": 5}],
    previous_hash="0",
)
blockchain.add_block(block2)

# Print the blockchain
for block in blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}\n")
