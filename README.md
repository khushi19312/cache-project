# cache-project

cache 1:
    This code stimulates the working of cache memory, the process of writing into Memory and the involvement
    of cache in the process of the CPU generating queries to access data from the Main Memory.
    This code implements three types of cache mapping, namely Direct mapping, Associative mapping and
    Set-Associative mapping.
    
    INPUT
    There are 3 levels of input:
      1. For the size of main memory, cache memory and the block size. These are taken in the form of
    powers of 2.
      2. For choosing between direct, associative and set-associative mapping.
      3. For performing read and write operations any number of times.
        a. In case of write operation, the user is asked to enter the address and the data.
        b. In case of read operation, the user is asked to enter the address.
    
    OUTPUT
    After selecting the mapping method, the user chooses between read and write operation and enters the
    required information.
      a. If it is the write operation, the output is the modified or updated cache memory.
      b. If it is the read operation, the output is “HIT” or “MISS” followed by the same or the updated cache
    memory respectively
    
    
cache 2:
    This code stimulates the working of a two level cache memory. The cache level one(L1) is half in size of the
    cache level two(L2). It implements the interaction of the 2 caches, the main memory and the CPU when the
    CPU produces a query.
    The implementation is based on direct mapping technique, write through and write allocation concept and
    NINE policy for multilevel cache.
    *This code is just a stimulation of cache memory and does not store data in the main memory. It just shows
    the working and not the actual process.
    
    INPUT
      1. For the size of main memory, cache memory and the block size. These are taken in the form of
      powers of 2.
      2. For performing read and write operations any number of times.
      c. In case of write operation, the user is asked to enter the address and the data.
      d. In case of read operation, the user is asked to enter the address.
    
    OUTPUT
    the user chooses between read and write operation and enters the required information.
      1. If it is the write operation, the output is the modified or updated cache memories.
      2. If it is the read operation, the output is “HIT IN L1” or “MISS IN L1, HIT IN L2” or “MISS IN BOTH L1
    AND L2” followed by the same or the updated cache memories respectively.

    
    
  
