import hashlib

class blockchain:
    def __init__(self,Pre_Block_hash, transaction_list) -> None:
        self.Pre_Block_hash = Pre_Block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + Pre_Block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Sunil sends 5 NC to Ganesh"
t2 = "Sanga sends 3.1 NC to Vicky"
t3 = "Vicky sends 5.2 NC to Manoj"
t4 = "Manoj sends 5.3 NC to vicky"
t5 = "Vicky sends 5.2 NC to ganesh"
t6 = "Vicky sends 5.2 NC to sanga"

intial_block = blockchain("Initial String",[t1,t2])

print(intial_block.block_data)
print(intial_block.block_hash)

second_block = blockchain(intial_block.block_hash,[t3,t4])

print(second_block.block_data)
print(second_block.block_hash)