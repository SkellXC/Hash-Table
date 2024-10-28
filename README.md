# Hash Table Implementation

This repository contains a Python implementation of a hash table that utilizes linear probing for collision resolution. The hash table allows for efficient insertion, retrieval, and deletion of key-value pairs, making it suitable for various applications such as indexing, caching, and password authentication.

## Key Features

- **Hash Function**: Uses ASCII values of characters to compute the hash index.
- **Collision Resolution**: Implements linear probing to handle collisions by finding the next available slot.
- **Load Factor Calculation**: Provides a method to calculate the load factor, allowing for effective management of storage efficiency.
- **Deletion Handling**: Uses placeholders to manage deletions, ensuring that search operations remain efficient even after items are removed.

## Usage Example

```python
ht = HashTable(11)  # Create a hash table with capacity for 11 items
ht.insert("Ada", "Engineer")  # Insert key-value pair
ht.insert("Mia", "Designer")  # Handle collision with linear probing
value = ht.find("Mia")  # Retrieve value associated with key "Mia"
print(value)  # Outputs: "Designer"
```
## Performance Considerations
Aiming for a low load factor to minimize clustering and enhance search efficiency.
Incorporates strategies to ensure uniform distribution of hash values and minimize collisions.
