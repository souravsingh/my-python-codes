import unittest

class Node:
    def __init__(self, value):
        self.val = value
        self.n = None

    def value(self):
        return self.val

    def next(self):
        return self.n


class LinkedList:
    def __init__(self, values=[]):
        self.length = 0
        self.h = None
        for el in values:
            self.push(el)

    def __len__(self):
        return self.length

    def __iter__(self):
        self.c = self.h
        return self

    def __next__(self):
        if self.c is not None:
            result = self.c.value()
            self.c = self.c.next()
            return result
        else:
            raise StopIteration

    def head(self):
        if self.h is None:
            raise EmptyListException("error")
        return self.h

    def push(self, value):
        curr_head = self.h
        self.h = Node(value)
        self.h.n = curr_head
        self.length = self.length + 1

    def pop(self):
        if self.h is None:
            raise EmptyListException("error")
        curr_head = self.head()
        self.h = curr_head.next()
        self.length = self.length - 1
        return curr_head.value()

    def reversed(self):
        return list(self)[::-1]


class EmptyListException(Exception):
    pass
    


# Tests for Linked List

class SimpleLinkedListTest(unittest.TestCase):
    def test_empty_list_has_len_zero(self):
        sut = LinkedList()
        self.assertEqual(len(sut), 0)

    def test_singleton_list_has_len_one(self):
        sut = LinkedList([1])
        self.assertEqual(len(sut), 1)

    def test_singleton_list_has_head(self):
        sut = LinkedList([1])
        self.assertEqual(sut.head().value(), 1)

    def test_non_empty_list_has_correct_head(self):
        sut = LinkedList([1, 2])
        self.assertEqual(sut.head().value(), 2)

    def test_can_pop_from_non_empty_list(self):
        sut = LinkedList([3, 4, 5])
        self.assertEqual(sut.pop(), 5)
        self.assertEqual(len(sut), 2)
        self.assertEqual(sut.head().value(), 4)

    def test_error_on_empty_list_pop(self):
        sut = LinkedList()
        with self.assertRaisesWithMessage(EmptyListException):
            sut.pop()

    def test_push_and_pop(self):
        sut = LinkedList([1, 2])
        sut.push(3)
        self.assertEqual(len(sut), 3)
        self.assertEqual(sut.pop(), 3)
        self.assertEqual(sut.pop(), 2)
        self.assertEqual(sut.pop(), 1)
        self.assertEqual(len(sut), 0)
        sut.push(4)
        self.assertEqual(len(sut), 1)
        self.assertEqual(sut.head().value(), 4)

    def test_empty_linked_list_to_list_is_empty(self):
        sut = LinkedList()
        self.assertEqual(list(sut), [])

    def test_reversed_empty_list_is_empty_list(self):
        sut = LinkedList([])
        self.assertEqual(list(sut.reversed()), [])

    def test_reversed_singleton_list_is_same_list(self):
        sut = LinkedList([1])
        self.assertEqual(list(sut.reversed()), [1])

    def test_reverse_non_empty_list(self):
        sut = LinkedList([1, 2, 3])
        self.assertEqual(list(sut.reversed()), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
