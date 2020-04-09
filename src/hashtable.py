# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # wrap the key-value pair in a linked list node
        new_node = LinkedPair(key, value)
        # run the key through the hash mod algorithm
        index = self._hash_mod(key)
        # declare a variable for keeping track of the current node
        curr_node = self.storage[index]
        # check to see if there is a key there already
        if self.storage[index] == None:
            self.storage[index] = new_node
            return
        # go down the linked list chain of that particular index
        while curr_node:
            # if it exists already, oops error out
            if curr_node.key == key:
                curr_node.value = value
                return
        # if not, insert the value as a new linked list node
            elif curr_node.next == None:
                curr_node.next = new_node
                return
            else:
                curr_node = curr_node.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash the key to retrieve a valid index within storage
        index = self._hash_mod(key)
        # iterate through each linked list node until finding the correct node
        curr_node = self.storage[index]
        while curr_node:
            if curr_node.key == key:
                # delete the value (change it to none)
                curr_node.value = None
                return
            else:
                curr_node = curr_node.next
        # print a warning if the key isn't found
        print("Warning! Key was not found.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash the key using _hash_mod method
        index = self._hash_mod(key)
        # loop through that index in storage until finding the matching key
        curr_node = self.storage[index]
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            else:
                curr_node = curr_node.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double the capacity
        self.capacity = self.capacity * 2
        # declare a new_storage variable to hold the new buckets
        new_storage = [None] * self.capacity
        # iterate through each index of the old table
        for index in self.storage:
            old_storage_node = index
            # traverse through each linked list node of the index
            while old_storage_node:
                # re-hash the key
                rehashed_index = self._hash_mod(old_storage_node.key)
                # declare a new LinkedPair node
                new_node = LinkedPair(
                    old_storage_node.key, old_storage_node.value)
                # insert the re-hashed key-value pair into the new table
                if new_storage[rehashed_index] == None:
                    new_storage[rehashed_index] = new_node
                    break
                # if there is already a key-value pair there, set up a loop to avoid collisions
                new_storage_node = new_storage[rehashed_index]
                while new_storage_node:
                    if new_storage_node.next == None:
                        new_storage_node.next = new_node
                        break
                    else:
                        new_storage_node = new_storage_node.next
        # overwrite the old storage with the new storage table
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
