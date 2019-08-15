# PROBLEM 5
## Blockchain
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For blockchain I am using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data. 
<br>
### In this problem I have used-
1. Link-List : List of blocks connected to each other through hash value of previous block
2. Dictionary:To store all hash value of all the blocks created and its reference address.


### Algorithm:
1. Initialise Blockchain with dictionary and last_block reference
2. Append block at the end of the list :
1. Create block .
2. Set data, timestamp, previous hash.
3. Calculate hash of new block using the data, timestamp and previous hash value.
4. Add the block hash as key in dictionary and block reference as value.
3. Print Blockchain
1. untill hash code of current block is zero
2. print data of current block
3. get previous block from dictionary using its previous hash value
4. repeat step 1


### Time Complexity Analysis:
• Append: O(1)<br>
• Print BlockChain: O(n) where n is number of blocks in blockchain<br>


### Space Complexity Analysis:
• Space to store dictionary: O(n)<br>
• BlockChain: O(n)<br>
