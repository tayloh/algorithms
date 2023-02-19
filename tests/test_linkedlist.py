import unittest

from algorithms.linkedlist import (
    reverse_list, reverse_list_recursive,
    is_sorted,
    remove_range,
    swap_pairs,
    rotate_right,
    is_cyclic,
    intersection,
    merge_two_list, merge_two_list_recur,
    is_palindrome, is_palindrome_stack, is_palindrome_dict,
    RandomListNode, copy_random_pointer_v1, copy_random_pointer_v2
)


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Convert from linked list Node to list for testing
def convert(head):
    ret = []
    if head:
        current = head
        while current:
            ret.append(current.val)
            current = current.next
    return ret


class TestSuite(unittest.TestCase):
    def setUp(self):
        # list test for palindrome
        self.l = Node('A')
        self.l.next = Node('B')
        self.l.next.next = Node('C')
        self.l.next.next.next = Node('B')
        self.l.next.next.next.next = Node('A')

        self.l1 = Node('A')
        self.l1.next = Node('B')
        self.l1.next.next = Node('C')
        self.l1.next.next.next = Node('B')

    def test_reverse_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        self.assertEqual([4, 3, 2, 1], convert(reverse_list(head)))
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        self.assertEqual([4, 3, 2, 1], convert(reverse_list_recursive(head)))

    def test_is_sorted(self):
        head = Node(-2)
        head.next = Node(2)
        head.next.next = Node(2)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(9)
        # head -> -2 -> 2 -> 2 -> 4 -> 9
        self.assertTrue(is_sorted(head))
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(8)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(6)
        # head -> 1 -> 2 -> 8 -> 4 -> 6
        self.assertFalse(is_sorted(head))

    def test_remove_range(self):
        # Test case: middle case.
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        # Expect output: 0 4
        self.assertEqual([0, 4], convert(remove_range(head, 1, 3)))

        # Test case: taking out the front node
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        # Expect output: 2 3 4
        self.assertEqual([2, 3, 4], convert(remove_range(head, 0, 1)))

        # Test case: removing all the nodes
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        self.assertEqual([], convert(remove_range(head, 0, 7)))

    def test_swap_in_pairs(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        # Expect output : 2 --> 1 --> 4 --> 3
        self.assertEqual([2, 1, 4, 3], convert(swap_pairs(head)))

    def test_rotate_right(self):
        # Given 1->2->3->4->5->NULL
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        # K = 2. Expect output: 4->5->1->2->3->NULL.
        self.assertEqual([4, 5, 1, 2, 3], convert(rotate_right(head, 2)))

    def test_is_cyclic(self):
        # create linked list => A -> B -> C -> D -> E -> C
        head = Node('A')
        head.next = Node('B')
        curr = head.next
        cyclic_node = Node('C')
        curr.next = cyclic_node
        curr = curr.next
        curr.next = Node('D')
        curr = curr.next
        curr.next = Node('E')
        curr = curr.next
        curr.next = cyclic_node
        self.assertTrue(is_cyclic(head))

        # create linked list 1 -> 2 -> 3 -> 4
        head = Node(1)
        curr = head
        for i in range(2, 6):
            curr.next = Node(i)
            curr = curr.next
        self.assertFalse(is_cyclic(head))

    def test_intersection_samelength(self):
        """Contract:
        Pre: Input is two linked lists, h1, h2, which intersect at the same index.
        Post: intersection(h1, h2) returns the intersected node.
        Asserts equal at the intersected node.
        """

        # create linked list as:
        # 1 -> 3 -> 5
        #            \
        #             7 -> 9 -> 11
        #            /
        # 2 -> 4 -> 6
        a1 = Node(1)
        b1 = Node(3)
        c1 = Node(5)
        d = Node(7)
        a2 = Node(2)
        b2 = Node(4)
        c2 = Node(6)
        e = Node(9)
        f = Node(11)

        a1.next = b1
        b1.next = c1
        c1.next = d
        a2.next = b2
        b2.next = c2
        c2.next = d
        d.next = e
        e.next = f

        self.assertEqual(7, intersection(a1, a2).val)
    
    def test_intersection_singlenodelists(self):
        """Contract:
        Pre: Input is two linked lists, h1, h2, which do not intersect.
        Post: intersection(h1, h2) returns None.
        Asserts equal None.
        """
        # h1: a
        #
        # h2: b

        a = Node(1)
        b = Node(2)
        self.assertEqual(None, intersection(a, b))

    def test_intersection_selfintersection(self):
        """Contract:
        Pre: Input is one linked list h.
        Post: intersection(h, h) returns the first intersection with itself.
        Asserts equal at the intersected node.
        """
        a = Node(1)
        b = Node(2)
        a.next = b
        self.assertEqual(1, intersection(a, a).val)

    def test_intersection_h1longer(self):
        """Contract:
        Pre: Input is two linked lists, h1, h2, where there's an intersection further along h1 than h2.
        Post: intersection(h1, h2) returns the intersected node.
        Asserts equal at the intersected node.
        """
        # h1: a1 -> a2
        #            \ 
        #             a3
        #            /
        # h2:       b1 

        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(3)
        a1.next = a2
        a2.next = a3

        b1 = Node(4)
        b1.next = a3

        self.assertEqual(3, intersection(a1, b1).val)
    
    def test_intersection_h2longer(self):
        """Contract:
        Pre: Input is two linked lists, h1, h2, where there's an intersection further along h2 than h1.
        Post: intersection(h1, h2) returns the intersected node.
        Asserts equal at the intersected node.
        """ 
        # h1:        a1
        #             \ 
        #             b3
        #             /
        # h2: b1 ->  b2 

        b1 = Node(1)
        b2 = Node(2)
        b3 = Node(3)
        b1.next = b2
        b2.next = b3

        a1 = Node(4)
        a1.next = b3

        self.assertEqual(3, intersection(a1, b1).val)


    def test_merge_two_list(self):
        """
        Input: head1:1->2->4, head2: 1->3->4
        Output: 1->1->2->3->4->4
        """
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(4)
        head2 = Node(1)
        head2.next = Node(3)
        head2.next.next = Node(4)
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         convert(merge_two_list(head1, head2)))
        # Test recursive
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(4)
        head2 = Node(1)
        head2.next = Node(3)
        head2.next.next = Node(4)
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         convert(merge_two_list_recur(head1, head2)))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(self.l))
        self.assertFalse(is_palindrome(self.l1))

    def test_is_palindrome_stack(self):
        self.assertTrue(is_palindrome_stack(self.l))
        self.assertFalse(is_palindrome_stack(self.l1))

    def test_is_palindrome_dict(self):
        self.assertTrue(is_palindrome_dict(self.l))
        self.assertFalse(is_palindrome_dict(self.l1))

    def test_solution_0(self):
        self._init_random_list_nodes()
        result = copy_random_pointer_v1(self.random_list_node1)
        self._assert_is_a_copy(result)

    def test_solution_1(self):
        self._init_random_list_nodes()
        result = copy_random_pointer_v2(self.random_list_node1)
        self._assert_is_a_copy(result)

    def _assert_is_a_copy(self, result):
        self.assertEqual(5, result.next.next.next.next.label)
        self.assertEqual(4, result.next.next.next.label)
        self.assertEqual(3, result.next.next.label)
        self.assertEqual(2, result.next.label)
        self.assertEqual(1, result.label)
        self.assertEqual(3, result.next.next.next.next.random.label)
        self.assertIsNone(result.next.next.next.random)
        self.assertEqual(2, result.next.next.random.label)
        self.assertEqual(5, result.next.random.label)
        self.assertEqual(4, result.random.label)

    def _init_random_list_nodes(self):
        self.random_list_node1 = RandomListNode(1)
        random_list_node2 = RandomListNode(2)
        random_list_node3 = RandomListNode(3)
        random_list_node4 = RandomListNode(4)
        random_list_node5 = RandomListNode(5)

        self.random_list_node1.next, self.random_list_node1.random = random_list_node2, random_list_node4
        random_list_node2.next, random_list_node2.random = random_list_node3, random_list_node5
        random_list_node3.next, random_list_node3.random = random_list_node4, random_list_node2
        random_list_node4.next = random_list_node5
        random_list_node5.random = random_list_node3


if __name__ == "__main__":
    unittest.main()
