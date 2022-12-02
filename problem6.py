class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail=self.head
            return

        self.tail.next = Node(value)
        self.tail=self.tail.next
        
    def to_list(self):
        lt =[]
        cur_head = self.head
        while cur_head:
            lt.append(cur_head.value)
            cur_head = cur_head.next
        return lt

# Declare a SET and put all items of list 1 and 2 to this one. Set will remove duplicate items
def union(llist_1, llist_2):
    unique= set(())

    current = llist_1.head
    while(current is not None):
        unique.add(current.value)
        current=current.next
    
    current=llist_2.head
    while(current is not None):
        unique.add(current.value)
        current=current.next  

    out = LinkedList()  
    for item in unique:
        out.append(item)
    return out

#Use a Dictionary to keep all items of list 1,
#Then check items of list 2 are belong to this dictionary of not.
#If yes, we put it to new list and remove it out from dictionary (because list 2 can have duplicate items)
#Then return new linked list
def intersection(llist_1, llist_2):
    out = LinkedList()  
    items ={}
    current = llist_1.head
    while(current is not None):
        items[current.value]=1
        current=current.next
    
    current=llist_2.head
    while(current is not None):
        if current.value in items:
            out.append(current.value)
            del items[current.value]
        current=current.next  

    return out



#Helper function to test
def check_same_items(list1,list2):
    for i in list1:
        if i not in list2:
            print('{} not in list 2'.format(i))
            return False
    for i in list2:
        if i not in list1:
            print('{} not in list 1'.format(i))
            return False
    return True


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1- Normal case
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,21,2,1]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union1 = union(linked_list_1,linked_list_2)
if not check_same_items(union1.to_list() , [32 , 1 , 2 , 35 , 3 , 4 , 6 , 9 , 11 , 21]):
    raise SystemExit('Test union 1 failed, actual {}'.format(union1.to_list()))

intersection1=intersection(linked_list_1,linked_list_2)
if not check_same_items(intersection1.to_list() , [4,1,21]):
    raise SystemExit('Test intersection1 1 failed, actual {}'.format(intersection1.to_list()))
print("Test case 1 passed")

# Test Case 2- Empty
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,21,2,1]
element_4 = []

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

union2 = union(linked_list_3,linked_list_4)
if not check_same_items(union2.to_list() , [1, 2, 35, 3, 4, 21]):
    raise SystemExit('Test union 2 failed, actual {}'.format(union2.to_list()))
    

intersection2=intersection(linked_list_3,linked_list_4)
if not check_same_items(intersection2.to_list() , []):
    raise SystemExit('Test intersection1 2 failed, actual {}'.format(intersection2.to_list()))
print("Test case 2 passed")


# Test Case 3- Duplicate
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [3,2,4,35,21,2,1]
element_6 = [3,2,4,35,21,2,1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

union3 = union(linked_list_5,linked_list_6)
if not check_same_items(union3.to_list() , [3, 2, 4, 35, 21, 1]):
    raise SystemExit('Test union 3 failed, actual {}'.format(union3.to_list()))

intersection3=intersection(linked_list_5,linked_list_6)
if not check_same_items(intersection3.to_list() , [3, 2, 4, 35, 21, 1]):
    raise SystemExit('Test intersection1 3 failed, actual {}'.format(intersection3.to_list()))
print("Test case 3 passed")


# Test Case 4- Both sets are empty. 
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()


union4 = union(linked_list_7,linked_list_8)
if not check_same_items(union4.to_list() , []):
    raise SystemExit('Test union 4 failed, actual {}'.format(union4.to_list()))

intersection4=intersection(linked_list_8,linked_list_8)
if not check_same_items(intersection4.to_list() , []):
    raise SystemExit('Test intersection1 4 failed, actual {}'.format(intersection4.to_list()))
print("Test case 4 passed")