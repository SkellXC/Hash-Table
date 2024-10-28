

class HashTable():
    def __init__(self,capacity):
        self.size = 0# How many items are stored in the hash table
        self.capacity = capacity# Total space available
        self.table = [None] * capacity# Creates a list of "None" with the length "capacity"


    def hashStuff(self,key):
        asciiSum = sum(ord(char) for char in key)# Adds all the ascii values in the string  
        return asciiSum % self.capacity# Gives the modulus of it (the position in the list)

    def insert(self,key,value):
        index = self.hashStuff(key)
        print(f"Hash is {index}")

        while self.table[index] is not None:
            if self.table[index][0] == key:  
                

                if isinstance(self.table[index][1], list):
                    self.table[index][1].append(value)
                else:
                    self.table[index] = (key,[self.table[index][1],value])# Creates an array and 
                                                                        # keeps the existing value


                # If a value with the same key is found, add this to that key. 
                # Array size/load factor doesn't change as same num of slots are used
                # Just that 1 slot has more items in it. Can't add it to another slot as
                # if you search for it with that key, the first item with that key will
                # be the only one that gets returned.

                return # End the loop as we don't want to increment the size of the table

            index = (index + 1)%self.capacity # Loop through array trick
        self.table[index] = (key,value) # Keeps the key so the search can look for the key
        self.size += 1 #
    
    def find(self,key):
        index = self.hashStuff(key)
        print(f"Hash is {index}")

        while self.table[index] != None:
             # (key,value) is stored in the position so [index][0] just gets the key
             # instead of the entire tuple
            if self.table[index][0] == key:
                return self.table[index][1]# Gives the actual value
            
            index = (index + 1) % self.capacity # Mod trick to loop in an array
        
        return None # If the value isn't found
            
    def getLoadFactor(self):
        lf = self.size/self.capacity
        print(f"Load factor: {lf*100}%")
        return lf


# Tests
if __name__ == "__main__":
    ht = HashTable(10)

    # Test 1: Insert and retrieve basic key-value pairs
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")

    assert ht.find("name") == "Alice", "Test 1.1 Failed: 'name' key retrieval"
    assert ht.find("age") == 30, "Test 1.2 Failed: 'age' key retrieval"
    assert ht.find("city") == "New York", "Test 1.3 Failed: 'city' key retrieval"

    # Test 2: Update an existing key
    ht.insert("city", "Los Angeles")  # Update the value for the key "city"
    assert ht.find("city") == ["New York", "Los Angeles"], "Test 2 Failed: Updating 'city' key"

    # Test 3: Handle collisions
    ht.insert("job", "Engineer")
    ht.insert("salary", 50000)
    ht.insert("hobby", "Hiking")

    assert ht.find("job") == "Engineer", "Test 3.1 Failed: 'job' key retrieval"
    assert ht.find("salary") == 50000, "Test 3.2 Failed: 'salary' key retrieval"
    assert ht.find("hobby") == "Hiking", "Test 3.3 Failed: 'hobby' key retrieval"

    # Test 4: Non-existent key
    assert ht.find("non_existent_key") is None, "Test 4 Failed: Non-existent key retrieval"

    # Test 5: Check load factor
    load_factor = ht.getLoadFactor()  # Should print and return the load factor
    assert load_factor == ht.size / ht.capacity, "Test 5 Failed: Load factor calculation"

    print("All tests passed!")
