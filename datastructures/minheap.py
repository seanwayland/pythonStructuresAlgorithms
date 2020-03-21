# https://www.tutorialspoint.com/heap-queue-or-heapq-in-python
'''
Heap queue is a special tree structure in which each parent node is less than or equal to its child node.
In python it is implemented using the heapq module.
 It is very useful is implementing priority queues
  where the queue item with higher weight is given more priority in processing.

  The easiest way to make a maxheap is to invert the value of the keys and use heapq.
  For example, turn 1000.0 into -1000.0 and 5.0 into -5.0.
'''

import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
print(H)

# Add element
heapq.heappush(H,8)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)




