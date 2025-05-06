import unittest
from sorting_algorithms import bubble_sort
from ds import LinkedList

class TestBubbleSort(unittest.TestCase):

    def test_sort_list(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([-1, -5, 0, 4]), [-5, -1, 0, 4])

    def test_sort_linked_list(self):
        ll = LinkedList()
        for value in [3, 1, 2]:
            ll.append(value)
        sorted_ll = bubble_sort(ll)
        self.assertEqual(sorted_ll.to_list(), [1, 2, 3])

    def test_single_item_list(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_single_item_linked_list(self):
        ll = LinkedList()
        ll.append(42)
        sorted_ll = bubble_sort(ll)
        self.assertEqual(sorted_ll.to_list(), [42])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_empty_linked_list(self):
        ll = LinkedList()
        sorted_ll = bubble_sort(ll)
        self.assertEqual(sorted_ll.to_list(), [])

if __name__ == '__main__':
    unittest.main()


    