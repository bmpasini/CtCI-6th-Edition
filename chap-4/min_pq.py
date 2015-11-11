class MinPQ(object):

    def __init__(self):
        self.heap = [None]

    def is_empty(self):
        return self.size() == 0

    def insert(self, val):
        self.heap.append(val)
        self.swim()

    def swim(self):
        k = self.size()
        while k > 1 and self.heap[k//2] > self.heap[k]:
            self.swap(k, k//2)
            k //= 2

    def size(self):
        return len(self.heap) - 1

    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def del_min(self):
        if self.is_empty():
            raise Exception("Priority queue underflow.")
        self.swap(1, self.size())
        self.sink()
        return self.heap.pop()

    def sink(self):
        k = 1
        while 2*k <= self.size()-1:
            j = 2*k
            if j < self.size()-1 and self.heap[j] > self.heap[j+1]:
                j += 1
            if self.heap[k] <= self.heap[j]:
                break
            self.swap(k, j)
            k = j
                
    def min(self):
        if self.is_empty():
            raise Exception("Priority queue underflow.")
        return self.pq[1]        

if __name__ == "__main__":
    q = MinPQ()
    q.insert(12)
    q.insert(32)
    q.insert(35)
    q.insert(84)
    q.insert(45)
    q.insert(62)
    q.insert(17)
    q.insert(27)
    q.insert(87)
    q.insert(887)
    q.insert(188)
    q.insert(174)
    q.insert(17)
    print(q.heap)
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())
    print(q.del_min())

