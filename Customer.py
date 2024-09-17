from _datetime import datetime
import sys
class Order:
    def __init__(self,ordername,immediance,time,cus_name): #class order to send datas
        self.ordername=ordername
        self.immediance=immediance
        self.time=time
        self.cus_name=cus_name
    def __gt__(self,other): #operation for comparing two diffrent object of orders
        if self.immediance>other.immediance:
            return True
        if self.immediance<other.immediance:
            return False
        if self.immediance==other.immediance:
            if self.time<other.time:
                return True
            if self.time>other.time:
                return False

class MaxHeap: #heap we are using as priority Queue

        def __init__(self, maxsize):

            self.maxsize = maxsize
            self.size = 0
            self.Heap = [0] * (self.maxsize + 1)
            self.Heap[0] = sys.maxsize
            self.FRONT = 1

        def parent(self, pos):

            return pos // 2

        def leftChild(self, pos):

            return 2 * pos

        def rightChild(self, pos):

            return (2 * pos) + 1

        def isLeaf(self, pos):

            if pos >= (self.size // 2) and pos <= self.size:
                return True
            return False

        def swap(self, fpos, spos):

            self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                                self.Heap[fpos])


        def maxHeapify(self, pos):

            if not self.isLeaf(pos):
                if (self.Heap[self.leftChild(pos)]>self.Heap[pos]) or(
                        self.Heap[self.rightChild(pos)]>  self.Heap[pos]) :

                    if (self.Heap[self.leftChild(pos)]) > (self.Heap[self.rightChild(pos)]):
                        self.swap(pos, self.leftChild(pos))
                        self.maxHeapify(self.leftChild(pos))


                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.maxHeapify(self.rightChild(pos))

        # Function to insert a node into the heap
        def insert(self, element):

            if self.size >= self.maxsize:
                return
            self.Heap[self.size] = element
            self.size += 1

            current = self.size-1
            while (  current!=0 and self.Heap[current]  > self.Heap[self.parent(current)]):

                self.swap(current, self.parent(current))
                current = self.parent(current)


        def Print(self):
            for i in range(0, (self.size // 2) + 1):

                 print(str(self.Heap[i].ordername+ self.Heap[i].cus_name))
                 if self.Heap[2 * i]!=0:
                       print(str(self.Heap[2 * i].ordername+ self.Heap[i].cus_name))
                 if self.Heap[2 * i + 1]!=0:
                       print(str(self.Heap[2 * i + 1].ordername + self.Heap[i].cus_name))

        def extractMax(self):

            popped = self.Heap[self.FRONT]
            self.Heap[self.FRONT] = self.Heap[self.size]
            self.size -= 1
            self.maxHeapify(self.FRONT)

            return popped

