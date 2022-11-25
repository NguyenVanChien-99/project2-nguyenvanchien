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



linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,21,2,1]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))