import hashlib
from datetime import datetime
from time import gmtime, strftime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.next=None

    def __str__(self) -> str:
        return "Timestamp: {} / Data: {}".format(self.timestamp,self.data)

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = self.data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.head=None
        self.tail=None
    
    def add_data(self,data):
        if data is None or data =="":
            print("Invalid input")
            return

        #Set block is head if the chain is empty
        if self.head is None:
            self.head= Block(datetime.now(),data,"")
            self.tail=self.head
            return
        
        #Calculate hash and put it to new block, then put this block to the tail of the chain
        previous_hash= self.tail.calc_hash()
        new_tail = Block(datetime.now(),data,previous_hash)
        self.tail.next= new_tail
        self.tail=new_tail
    
    #print all the chain
    def print(self):
        if self.head is None:
            print("Nothing here")
            return
        current = self.head
        while(current is not None):
            print(current)
            current=current.next

    #Check the chain is valid or not
    def check_valid(self):
        if self.head is None:
            return
        current = self.head
        while(current.next is not None):
            hash_data = current.calc_hash()
            if hash_data != current.next.previous_hash:
                print("Invalid chain , at block {}".format(current.next))
                return
            current=current.next
        print("OK!")

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
block1 = BlockChain()
block1.add_data("1111")
block1.add_data("2222")
block1.add_data("3333")
block1.check_valid()
block1.print()
print("========================================")
# Test Case 2
block2 = BlockChain()
block2.add_data("1111")
block2.add_data("2222")
block2.add_data("3333")
block2.head.next.data="aaaa"
block2.print()
block2.check_valid()
print("========================================")
# Test Case 3 empty chain
block3 = BlockChain()
block3.print()

# Test case 4 add empty block
block4 = BlockChain()
block4.add_data(None)
block4.print()