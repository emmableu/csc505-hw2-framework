class Solution:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0
    def compare(self, element1, element2):
        self.comparison_count += 1;
        if (element1 < element2):
            return element1, element2
        else:
            return element2, element1
    def merge_sort(self, p, r):
        if p < r:
            q = (p+r)//2
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            self.merge(p, q, r)

    def merge(self, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        left, right = [], []
        for i in range(p, q+1):
            left.append(self.sorting_array[i])
        for j in range(q+1, r+1):
            right.append(self.sorting_array[j])
        left.append(float('inf'))
        right.append(float('inf'))
        i, j = 0, 0
        for k in range(p, r+1):
            smaller_element, larger_element = self.compare(left[i], right[j])
            self.sorting_array[k] = smaller_element
            if smaller_element == left[i]:
                i = i + 1
            else:
                j = j + 1

    def heapify(self, parent, heap_size):

        l = (parent)*2+1
        r = (parent)*2+2

        largest = parent
        if l < heap_size:
            smaller_element, larger_element = self.compare(self.sorting_array[l], self.sorting_array[parent])
            if (larger_element == self.sorting_array[l]):
                largest = l
        if r < heap_size:
            smaller_element, larger_element = self.compare(self.sorting_array[r], self.sorting_array[largest])
            if (larger_element == self.sorting_array[r]):
                largest = r

        if largest!=parent:
            temp =  self.sorting_array[largest]
            self.sorting_array[largest] = self.sorting_array[parent]
            self.sorting_array[parent]= temp
            self.heapify(largest, heap_size)

    def build_heap(self):
        for i in reversed(range((len(self.sorting_array)//2))):
            self.heapify(i, len(self.sorting_array))

    def heap_sort(self):
        self.build_heap()

        for i in reversed(range(1, len(self.sorting_array))):
            temp = self.sorting_array[i]
            self.sorting_array[i] = self.sorting_array[0]
            self.sorting_array[0] = temp
            self.heapify( 0, i)


    def insertion_sort(self):
        for j in range(1, len(self.sorting_array)):
            key = self.sorting_array[j]
            i = j - 1
            while i >= 0 and self.sorting_array[i]==self.compare(self.sorting_array[i], key)[1]:
                self.sorting_array[i+1] = self.sorting_array[i]
                i = i - 1
            self.sorting_array[i+1] = key
