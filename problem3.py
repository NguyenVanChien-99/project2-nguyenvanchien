import sys
from heapq import heapify, heappush, heappop
  
class Node(object):
    def __init__(self,char, val):
        self.char=char #character
        self.val = val  #frequency
        self.left=None
        self.right=None
    def __repr__(self):
        return f'{self.char}== {self.val}'
    # use this function to compare when we put node in to priority queue
    def __lt__(self, other):
        return self.val < other.val

def huffman_encoding(data):
    if data=="":
        return "",None
    
    #Determine the frequency of each character in the message
    frequency = generate_frequency_dic(data)

    # Creating heap to save nodes with its character and frequency (kind of priority queue)
    heap = []
    heapify(heap)
    for key in frequency:
        heappush(heap,Node(key,frequency[key]))
    
    #Build a huffman tree
    while(len(heap))>=2:
        #Get 2 firsts element and create a node as parent of them , then put it back to priority queue
        first= heappop(heap)
        second= heappop(heap)
        parent =Node("",first.val+second.val)
        parent.left=first
        parent.right=second
        heappush(heap,parent)
    #The last element of priority queue will be the head of tree
    head= heappop(heap)

    #Generate the Encoded Data based on the Huffman tree
    encoded=generate_code_from_tree(data,head)
    return encoded,head

def generate_code_from_tree(data,head):
    binary_code ={}
    # If the tree has only 1 node , that mean we have only one character in the message
    # So save the binary code of character as 0
    if head.left is None and head.right is None:
        binary_code[head.char]="0"
    else:
        #Function to generate unique binary (here is the path from root to leaf) code for each character
        def trasever_tree(node,path):
            if node.left is None and node.right is None: #leaf node
                binary_code[node.char]=path
                return
            if node.left is not None:
                trasever_tree(node.left,path+"0")
            if node.right is not None:
                trasever_tree(node.right,path+"1")

        if head.left is not None:
            trasever_tree(head.left,"0")
        if head.right is not None:
            trasever_tree(head.right,"1")
    
    encoded=""
    #generate encoded data base on the unique binary code we just created
    for char in data:
        encoded+=binary_code[char]
    return encoded


def generate_frequency_dic(data):
    fre ={}
    for char in data:
        if char not in fre:
            fre[char]=1
        else:
            fre[char]=fre[char]+1
    return fre

def huffman_decoding(data,tree):
    if data=="" or tree is None :
        return ""

    #If the tree has only 1 node , that mean we have only one character in the message 
    #This character is saved as 0 before(binary code)
    if tree.left is None and tree.right is None:
        out =""
        for char in data:
            if char=="0":
                out+=tree.char
            else:
                print("Invalid encoded data")
                return ""
        return out

    #Decode
    decoded_data=""
    #Current node is head of tree
    node= tree
    for char in data:
        # if current character is 0 , then we go to the left of current node (node = node.next)
        # if the left of current node is NONE , that's mean invalid encoded data
        if char =="0" :
            if node.left is not None:
                node=node.left
            else :
                print("Invalid encoded data")
                return ""
        # Same logic with above but for the right side
        if char =="1" :
            if node.right is not None:
                node=node.right
            else:
                print("Invalid encoded data")
                return ""
        # If current node is leaf , then we get the character of node and put it to decoded_data
        if node.left is None and node.right is None:
            decoded_data+=node.char
            node=tree
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree=huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
encoded1,head1= huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
if encoded1!="1010101010101000100100111111111111111000000010101010101":
    raise SystemExit("Test case 1 : encode failed")
decoded1= huffman_decoding(encoded1,head1)
if decoded1!="AAAAAAABBBCCCCCCCDDEEEEEE":
    raise SystemExit("Test case 1 : decode failed")
print("Test case 1 pass")
# Test Case 2
encoded1,head1= huffman_encoding("A")
if encoded1!="0":
    raise SystemExit("Test case 2 : encode failed")
decoded1= huffman_decoding(encoded1,head1)
if decoded1!="A":
    raise SystemExit("Test case 2 : decode failed")
print("Test case 2 pass")
# Test Case 3
encoded1,head1= huffman_encoding("")
if encoded1!="":
    raise SystemExit("Test case 3 : encode failed")
decoded1= huffman_decoding(encoded1,head1)
if decoded1!="":
    raise SystemExit("Test case 3 : decode failed")
print("Test case 3 pass")

# Test Case 4- same character repeated multiple
encoded1,head1= huffman_encoding("AAAAAAA")
if encoded1!="0000000":
    raise SystemExit("Test case 4 : encode failed")
decoded1= huffman_decoding(encoded1,head1)
if decoded1!="AAAAAAA":
    raise SystemExit("Test case 4 : decode failed")
print("Test case 4 pass")