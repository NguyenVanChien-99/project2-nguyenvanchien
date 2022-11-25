### Explain:
# I use a list (self.use) to track what is the least recently used. 
# The value of the list will be the key we input
# The least recently used will be the first element of list (self.use[0])
# When we call get() function, if it exist , we will move this element to the last index of list
# Eg. : current: [1,2,3,4,5] -> get(3) -> [1,2,4,5,3]
# And i use dictionary to as a cache


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.use=[]
        self.cache= {}

    def get(self, key):
        if key not in self.cache:
            return -1
        self.use.remove(key)
        self.use.append(key)
        return self.cache[key]

    def set(self, key, value):
        if key is None or value is None:
            return
        if len(self.cache)>=self.capacity:
            del self.cache[self.use[0]]
            self.use.pop(0)
            self.use.append(key)
        else:
            self.use.append(key)
        self.cache[key]=value

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Input large values
our_cache.set(19999999999999999999999999999999,19999999999999999999999999999999999)
if our_cache.get(19999999999999999999999999999999) !=19999999999999999999999999999999999:
    print("Test Case 1 Failed")
if our_cache.get(4) !=-1:
    print("Test Case 1 Failed(Least use)")
print("Test Case 1 pass")
# Test Case 2: Input None
our_cache.set(None,1)
if our_cache.get(None) !=-1:
    print("Test Case 2 Failed")
print("Test Case 2 pass")
# Test Case 3: Input negative values
our_cache.set(-100,-100)
if our_cache.get(-100) !=-100:
    print("Test Case 3 Failed")
print("Test Case 3 pass")
