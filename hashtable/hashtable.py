class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity): 
        self.array = [None] * capacity
        self.capacity = capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        total = 0
        for i in self.array:
            if self.array[i] is not None:
                # iterate over LL, adding to total
                current = self.array[i].head
                while current is not None:
                    total += 1 # current is there, so increment
                    current = current.next # move to next
                # at the end of LL
                break
        return total / self.capacity
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Define Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis
        for c in key: # loop over letters
            hash = hash ^ ord(c) # ^ Sets each bit to 1 if only one of two bits is 1 (not sure what this bitwise operator does)
            hash = hash * FNV_prime
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
            hash = ((hash * 33) + hash) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity 
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        """Add a value to our array by its key"""
        index = self.hash_index(key) # hash key

        lf = self.get_load_factor()
        if lf > 0.7:
            self.resize(self.capacity * 2)

        if self.array[index] is not None: 
            # If this already contains some values, we may have to update
            current = self.array[index].head
            while current is not None:
                print(current.value[0])
                if current.value[0] == key: # if key is found
                    current.value = (key, value) # update value
                    return current.value[1] # return value
            
                current = current.next # key wasn't found, so move to next
            # if while loop ends, there is no head. just add the kvp
            self.array[index].insert_at_tail([key, value])
        else:
            # This index is empty. We should initiate 
            # a LL and add our key-value-pair to it.
            self.array[index] = LinkedList()
            self.array[index].insert_at_tail((key, value))


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        lf = self.get_load_factor()
        if lf < 0.2:
            self.resize(self.capacity / 2)
        index = self.hash_index(key) # initiate index with hash func
        if self.array[index] is None: # if nothing here, raise err
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            current = self.array[index].head
            print(current.value)
            while current is not None: # loop over all key value pairs
                if current.value[0] == key: # if this key exists
                    return self.array[index].delete(current.value) # delete it
                current = current.next # next node
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        """Get a value by key"""
        index = self.hash_index(key)

        if self.array[index] is None:
            raise KeyError()
        else:
            # Iterate over LL
            # and find if our key exist. If it does 
            # then return its value.
            current = self.array[index].head
            while current is not None:
                if current.value[0] == key:
                    return current.value[1]
            
                current = current.next
            # If no return was done during loop,
            # it means key didn't exist.
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        """Double the list length and re-add values"""
        ht2 = HashTable(new_capacity)
        # print(self.array)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            # Since our list is now a different length,
            # we need to re-add all of our values to 
            # the new list for its hash to return correct
            # index.
            current = self.array[i].head 
            while current is not None:
                (key, val) = current.value # destructure key, val
                ht2.put(key, val) # add to new hash table
                current = current.next # next kvp
        # Finally we just replace our current list with 
        # the new list of values that we created in ht2.
        self.array = ht2.array
        self.capacity = new_capacity # replace capacity as well so our hash works correctly
        return self.array




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


############################################# NOTES

'''
Index  Chain (linked list)
----   ---------------
0      ("qux", 54)  -> None
1      ("foo", 29)  -> None
2      ("bar", 99)  -> None
3      LL[self.head = Node(self.key = "fox", self.value = 101) -> Node("tree", 209) -> None]
4      -> None
​
put("foo", 42)   # hashed to index 1
put("foo", 29)   
put("bar", 99)   # hashes to index 2
put("baz", 38)   # hashes to index 1! collision!
put("qux", 54)   # hashes to 0
put("fox", 101)  # hashes 3
put("tree", 209) # hashes 3
​
get("qux")
get("foo")
get("fred")  # hashes to 0 --> return None
​
​
delete("baz")
​
'''
# Insert a LL into the hash table, when you put something in
# hash table main data structure: [LL, LL, LL, None, LL, None, None]

# how to make the LL work with our hash table?
## ensure each node has a key as well as a value
## change methods to use keys, not just values, where necessary
## write a new method, maybe insert_or_overwrite
### search for the key, if found, overwrite
### otherwise, add a new node

# generic ListNode and LinkedList

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current

            current = current.next

        return None

    def insert_at_tail(self, value):
        node = ListNode(value)

        # if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, value):
        current = self.head

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting head
        if current.value == value:
            self.head = current.next
            return current

        # when deleting something else
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.value == value: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node

                else:
                    previous = current
                    current = current.next

            return None # if we got here, nothing was found!




'''

0   A  ->  E  -> O -> P
1   B  ->  F  -> I -> J -> K -> L
2   C  ->  G  -> M
3   D  ->  H  -> N -> Q -> R

get(A)
get(H)


Hash Table Load Factor
number of things / length of array (number of buckets)

18/4 = 9/2 = 4.5

Load factor < 0.7, aka 70%

0  A
1  B -> C
2 
3  


# How to resize??
make a new array, with double the capacity, to reduce how much often we need to do this

0
1
2  B
3
4  A -> D
5
6  C
7

# How to keep track of how many things we've inserted?
## keep a counter, every time you insert
### if you overwrite, that's not a new thing


# Shrinking, based on the load factor
When you delete, also update your tracker
if load factor < 0.2, rehash! 
Make a new array, half the size

Minimum size 8, don't halve below 8

STRETCH GOAL

'''