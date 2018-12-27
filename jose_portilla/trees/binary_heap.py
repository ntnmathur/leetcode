# A Binary Heap is a Binary Tree with following properties.
# 1) It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.
#
# 2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.


# Complete Binary Tree --> Each level has all nodes
# priority queues are queues where element of highest priority is at the beginning of the queue. Basically all elements are arranged by priority
# Its implemented using Binary Heap:
# Below formula applies if 0th element is defaulted to 0
# index of right side element = 2i+1 => i is the current index
# parent node = i//2
# index of left side element = 2i
# root
# /  \
# L   R

class BinHeap(object):
    def __init__(self):
        self.heapList = [0]  # single 0 as first element
        self.currentSize = 0

    def perc_up(self, i):
        while i//2 > 0: # if parent exists
            if self.heapList[i] < self.heapList[i//2]: # if parent > child; swap
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def insert(self, k): # Insert at the end and swap
        self.heapList.append(k)
        self.currentSize += 1
        self.perc_up(self.currentSize)

    def perc_down(self, i):
        while i*2 <= self.currentSize:
            mc = self.min_child(i) # Get index of the minchild of the node
            if self.heapList[i] > self.heapList[mc]: # if parent > minchild, swap
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def min_child(self, i):
        if i*2 + 1 > self.currentSize: # if right child > size (does not exist) return the left
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]: # parent < right child return lower
                return i*2
            else:
                return i*2+1

    def del_min(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize] # Make last value as root
        self.currentSize = self.currentSize - 1
        self.heapList.pop() # Remove the last value from list as we moved it to the root
        self.perc_down(1) # perc down the root value to the right position
        return retval

    # Build heap from a list
    def build_heap(self, alist):
        i = len(alist) // 2 # start point is mid of the binary heap and use perdown for downstream correction
        self.currentSize = len(alist) # set the size
        self.heapList = [0] + alist[:] # set the initial order with 0 appended
        while i > 0:
            self.perc_down(i)
            i = i - 1
