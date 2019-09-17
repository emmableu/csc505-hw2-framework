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
            # print("q: ",q)
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
        # print('left: ', left, 'right: ', right)
        left.append(float('inf'))
        right.append(float('inf'))
        i, j = 0, 0
        for k in range(p, r+1):
            smaller_element, larger_element = self.compare(left[i], right[j])
            # print(smaller_element, larger_element)
            self.sorting_array[k] = smaller_element
            if smaller_element == left[i]:
                i = i + 1
            else:
                j = j + 1

    def heapify(self, parent, heap_size):

    # This is the reverse from the max_heapify.
        l = (parent)*2+1
        r = (parent)*2+2
        try:
            print('parent: ', self.sorting_array[parent], "left_child: ", self.sorting_array[l], "right_child: ", self.sorting_array[r])
        except:
            pass
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
            print('largest is not parent')
            print('before swap: ',  self.sorting_array)
            temp =  self.sorting_array[largest]
            self.sorting_array[largest] = self.sorting_array[parent]
            self.sorting_array[parent]= temp
            print('after swap: ', self.sorting_array)
            # Exchange heap[largest], heap[parent]
            self.heapify(largest, heap_size)

    def build_heap(self):
        for i in reversed(range((len(self.sorting_array)//2))):
            # print('i: ', i)
            self.heapify(i, len(self.sorting_array))

    def heap_sort(self):
        self.build_heap()
        print(self.sorting_array)

        for i in reversed(range(1, len(self.sorting_array))):
            temp = self.sorting_array[i]
            self.sorting_array[i] = self.sorting_array[0]
            self.sorting_array[0] = temp
            print("i: ", i, "self.sorting_array: ", self.sorting_array)
            self.heapify( 0, i)
            print('after heapify: ', self.sorting_array)


    def insertion_sort(self):
        for j in range(1, len(self.sorting_array)):
            key = self.sorting_array[j]
            i = j - 1
            while i >= 0 and self.sorting_array[i]==self.compare(self.sorting_array[i], key)[1]:
                # print("i: ", i, 'self.sorting_array[i]', self.sorting_array[i])
                self.sorting_array[i+1] = self.sorting_array[i]
                i = i - 1
            self.sorting_array[i+1] = key



#create a class that receives and holds 101 timestamps
#whenever a timestamp comes, it goes by t(add).
#if the timestamp is more than the 101st in the stream, whenever it comes, another one comes out of the heap. On the other hand, if it's in the 101 first ones. It needs to be remained in the stream.

#t= Timestamp() for initialization
#t.add() (whenever there's a number comes)

#if no timestamp is ever coming anymore (we reaches the end of the data stream), run heap_sort(t.heap) to get the sorted heap.





#
#
# solution = Solution([4, 3, 2,1])
# solution.heap_sort()
# print(solution.sorting_array)
# print(solution.comparison_count)
