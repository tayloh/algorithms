"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest

branches = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False,
            11:False, 21:False, 31:False, 41:False, 61:False, 71:False, 81:False, 91:False}

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def intersection(h1, h2):

    global branches

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2: # 1
        branches[1] = True

        count += 1

        if not flag and (h1.next is None or h2.next is None): # 2
            branches[2] = True

            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)
        else: #21
            branches[21] = True

        if h1: # 3
            branches[3] = True

            h1 = h1.next
        else: # 31
            branches[31] = True

        if h2: # 4
            branches[4] = True

            h2 = h2.next
        else: #41
            branches[41] = True
    else: #11
        branches[11] = True

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None: # 5
        branches[5] = True

        shorter = h1_orig
        longer = h2_orig

    elif flag[2] is None: # 6
        branches[6] = True

        shorter = h2_orig
        longer = h1_orig
    
    else: # 61 - Unreachable
        branches[61] = True

    while longer and shorter: # 7
        branches[7] = True

        while long_len > short_len: # 8
            branches[8] = True

            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1
        else: # 81
            branches[81] = True

        if longer == shorter: # 9
            branches[9] = True

            # The nodes match, return the node
            return longer
        else: # 91
            branches[91] = True

            longer = longer.next
            shorter = shorter.next
    else: # 71
        branches[71] = True

    return None


class TestSuite(unittest.TestCase):

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


def runcoverage():
    unreachable = [61]

    coverage = 0
    max_coverage = 100
    points_per_branch = max_coverage / len(branches.keys())
    print("----------Branch Coverage----------")
    for key in branches.keys():
        print(str(key) + " : " + str(branches[key]))
    
        if branches[key] or key in unreachable:
            coverage += points_per_branch
    
    print("Unreachable:", unreachable)
    print("Branch coverage:", coverage, "%")
    print("----------Branch Coverage----------")


if __name__ == '__main__':

    unittest.main(exit=False)
    runcoverage()
