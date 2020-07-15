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

        if self.array[index] is not None: 
            # If this already contains some values, we may have to update
            for kvp in self.array[index]: # iterate over key value pairs
                if kvp[0] == key: # if key is found
                    kvp[1] = value  # update current value to the new value
                    break
            else:
                # If no breaks was hit in the for loop, it 
                # means that no existing key was found, 
                # so we can simply just add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])
        # print("self.array[index]", self.array[index])


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key) # initiate index with hash func
        if self.array[index] is None: # if nothing here, raise err
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[index]: # loop over all key value pairs
                if kvp[0] == key: # if this key exists
                    kvp[1] = None # delete it
                    return kvp[1] # return deleted one
            
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
        print("key", key)
        index = self.hash_index(key)
        print("index", index)
        print("capacity", self.capacity)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()


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
            for kvp in self.array[i]:
                ht2.put(kvp[0], kvp[1])
        # Finally we just replace our current list with 
        # the new list of values that we created in ht2.

        self.array = ht2.array
        self.capacity = new_capacity
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