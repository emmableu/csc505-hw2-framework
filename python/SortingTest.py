import unittest
from SolutionFilled import *
class SortingTest(unittest.TestCase):
    def test_insertion_sort(self):
        input_array = [3, 6, 1]
        solution = Solution(input_array)
        solution.insertion_sort()
        self.assertEqual(solution.sorting_array,[1, 3, 6])
        self.assertEqual(solution.comparison_count, 3)

        input_array = [1, 2, 3, 4]
        solution = Solution(input_array)
        solution.insertion_sort()
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4])
        self.assertEqual(solution.comparison_count, 3)

        input_array = [7, 3, 1, 5, 6, 2, 4]
        solution = Solution(input_array)
        solution.insertion_sort()
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(solution.comparison_count, 16)

        input_array = list(reversed(range(1, 100)))
        solution = Solution(input_array)
        solution.insertion_sort()
        self.assertEqual(solution.sorting_array,list(range(1, 100)))
        self.assertEqual(solution.comparison_count, 4851)

    def test_merge_sort(self):
        input_array = [3, 6, 1]
        solution = Solution(input_array)
        solution.merge_sort(0, len(input_array)-1)
        self.assertEqual(solution.sorting_array,[1, 3, 6])
        self.assertEqual(solution.comparison_count, 5)

        input_array = [1, 2, 3, 4]
        solution = Solution(input_array)
        solution.merge_sort(0, len(input_array)-1)
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4])
        self.assertEqual(solution.comparison_count, 8)

        input_array = [7, 3, 1, 5, 6, 2, 4]
        solution = Solution(input_array)
        solution.merge_sort(0, len(input_array)-1)
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(solution.comparison_count, 20)

        input_array = list(reversed(range(1, 100)))
        solution = Solution(input_array)
        solution.merge_sort(0, len(input_array)-1)
        self.assertEqual(solution.sorting_array,list(range(1, 100)))
        self.assertEqual(solution.comparison_count, 664)

    def test_heap_sort(self):
        input_array = [3, 6, 1]
        solution = Solution(input_array)
        solution.heap_sort()
        self.assertEqual(solution.sorting_array,[1, 3, 6])
        self.assertEqual(solution.comparison_count, 3)


        input_array = [1, 2, 3, 4]
        solution = Solution(input_array)
        solution.heap_sort()
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4])
        self.assertEqual(solution.comparison_count, 7)

        input_array = [7, 3, 1, 5, 6, 2, 4]
        solution = Solution(input_array)
        solution.heap_sort()
        self.assertEqual(solution.sorting_array,[1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(solution.comparison_count, 19)

        input_array = list(reversed(range(1, 100)))
        solution = Solution(input_array)
        solution.heap_sort()
        self.assertEqual(solution.sorting_array,list(range(1, 100)))
        self.assertEqual(solution.comparison_count, 927)



if __name__ == '__main__':
    unittest.main()
