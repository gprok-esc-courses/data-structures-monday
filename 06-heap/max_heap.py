
class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()

    def is_empty(self):
        return len(self.heap) == 0

    def get_max(self):
        if self.is_empty():
            return None
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.heapify_down()
        return max

    def heapify_down(self):
        pos = 0
        while pos is not None:
            max_pos = self.max_child_pos(pos)
            if max_pos is not None:
                if self.heap[max_pos] > self.heap[pos]:
                    self.heap[max_pos], self.heap[pos] = \
                        self.heap[pos], self.heap[max_pos]
            pos = max_pos

    def max_child_pos(self, pos):
        left = self.left_child_pos(pos)
        right = self.right_child_pos(pos)
        if left >= len(self.heap):
            return None
        elif right >= len(self.heap):
            return None
        else: 
            return left if self.heap[left] > self.heap[right] else right
        

    def left_child_pos(self, pos):
        return 2 * pos + 1
    
    def right_child_pos(self, pos):
        return 2 * pos + 2

    def heapify_up(self):
        pos = len(self.heap) - 1
        while pos > 0:
            parent_pos = self.get_parent_position(pos)
            if self.heap[pos] > self.heap[parent_pos]:
                self.heap[pos], self.heap[parent_pos] = \
                        self.heap[parent_pos], self.heap[pos]
                pos = parent_pos
            else:
                break

    def get_parent_position(self, pos):
        return (pos - 1) // 2
    

if __name__ == "__main__":
    data = [8, 4, 13, 2, 18, 41, 1, 3, 5, 22, 7, 5]
    heap = MaxHeap()
    for v in data:
        heap.insert(v)
    print(heap.heap)
    max = heap.get_max()
    print("MAX:", max)
    print(heap.heap)