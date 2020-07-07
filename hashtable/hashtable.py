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
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity 


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        fnvHash = 14695981039346656037
        for letter in key: 
            fnvHash = fnvHash * 1099511628211
            fnvHash = fnvHash + ord(letter)
        return fnvHash


# algorithm fnv-1 is
#     hash := FNV_offset_basis do

#     for each byte_of_data to be hashed
#         hash := hash × FNV_prime
#         hash := hash XOR byte_of_data

#     return hash 


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        


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
        # Your code here
        # index_in_list  = self.hash_index(key)
        # if index_in_list is not None:
        #   self.storage[index_in_list] = value
        

        node = HashTableEntry(key, value)   # make new Node, so that there's access to Next
        i = self.hash_index(node.key)       # get the index in the array
        if self.storage[i] is not None:     # check if that index is occupied. If index is OCCUPIED
            cur = self.storage[i]           # make cur point at the node that's in that index
            while cur.next is not None:     # loop through LinkedList at that index until you get to the tail
                if cur.key == key:          # check to see if the keys already exist. if it does...
                    cur.value = value       # overide the value and break out of al lthe things
                    return 
                cur = cur.next
            cur.next = node                 # make the tail point towards the new node 
        else:                               # if index is EMPTY...
            self.storage[i] = node          # ...insert the new node at that index


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # # Your code here
        # index_in_list = self.hash_index(key)
        # if index_in_list is not None:
        #     self.storage[index_in_list] = None
        # else:
        #     print("Key was not found")

        i = self.hash_index(node.key)       # get the index in the array
        if self.storage[i] is not None:     # if there's something at that index
            cur = self.storage[i]           # make cur point at the node that's in that index
            while cur.key != key:     
                if cur.next is not None:
                    cur = cur.next
                else: 
                    print("key was not found")
                    return 
            # if keys match....the list is only 1, or it's the tail
            if cur.next is not None:
                prev = cur
                cur = cur.next 
                prev.next

                
        else:                               # if there's nothing at that index
            print("Key was not found")      # say so

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # index_in_list = self.hash_index(key)
        # if index_in_list is not None:
        #     return self.storage[index_in_list]
        # else:
        #     return None

        i = self.hash_index(key)            # get the index
        if self.storage[i] is not None:     # if that index is OCCUPIED...
            cur = self.storage[i]           # set a cur pointer at the node in that occupied index
            while cur.key != key:           # check if the key's don't match
                if cur.next is not None:    # check if there's something to point to, if so
                    cur = cur.next          # then point to it
                else:                       # if not, 
                    return None             # return Nothing
            return cur.value                # if the keys match, the while loop won't run and you'll return the value
        else:                               # otherwise, if the index is empty...
            return None                     # return nothing

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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




# hash_table = [None] * 8   # 8 slots, all initiailized to None
# def my_hash(s):
#     sb = s.encode()  # Get the UTF-8 bytes for the string
#     total = 0
#     for b in sb:
#         total += b
#         total &= 0xffffffff  # clamp to 32 bits
#     return total
# def hash_index(key):
#     h = my_hash(key)
#     return h % len(hash_table)
# def put(key, val):
#     i = hash_index(key)
#     if hash_table[i] != None:
#         print(f"Collision! Overwriting {repr(hash_table[i])}!")
#     hash_table[i] = val
# def get(key):
#     i = hash_index(key)
#     return hash_table[i]
# def delete(key):
#     i = hash_index(key)
#     hash_table[i] = None
# put("Hello", "Hello Value")
# put("World", "World Value")


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def find(self, value):
#       #start at the head
#       #loop through the list
#       #find value
#       #return the node

#       cur = self.head
#       while cur is not None:
#           if cur.value == value:
#               return cur
#           cur = cur.next
#       return None

#     def delete(self, value):
#         cur = self.head
#         if cur.value == value:
#             self.head = cur.next
#             return cur
        
#         prev = cur
#         cur = cur.next

#         while cur is not None:
#             if cur.value == value:
#                 prev.next = cur.next
#                 return cur
#             else:
#                 prev = cur
#                 cur = cur.next


#     def insert_at_head(self, node):
#         node.next = self.head
#         self.head = node

#       return None