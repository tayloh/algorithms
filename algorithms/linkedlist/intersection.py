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

class Node(object): # pragma: no cover
    def __init__(self, val=None):
        self.val = val
        self.next = None

def get_length(h):
    length = 0
    head = h
    while head:
        length += 1
        head = head.next
    
    return length

def get_n_last_nodes(h, n):
    length = get_length(h)

    if length <= n:
        return h
    
    head = h
    while length > n:
        length -= 1
        head = h.next
    
    return head


def intersection(h1, h2):
    # Get the lengths
    h1_length = get_length(h1)
    h2_length = get_length(h2)

    # Check which list is the longer / shorter one / if they're the same it doesn't matter
    if h1_length > h2_length:
        longer, long_len = h1, h1_length
        shorter, short_len = h2, h2_length
    else:
        longer, long_len = h2, h2_length
        shorter, short_len = h1, h1_length

    # Advance the longer list
    longer = get_n_last_nodes(longer, short_len)

    # Check for intersection
    while longer and shorter:
        if longer == shorter:
            return longer
        else:
            longer = longer.next
            shorter = shorter.next
    
    return None

def intersection_old(h1, h2): # pragma: no cover

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2:
        count += 1

        if not flag and (h1.next is None or h2.next is None):
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)

        if h1:
            h1 = h1.next
        if h2:
            h2 = h2.next

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        shorter = h2_orig
        longer = h1_orig

    while longer and shorter:

        while long_len > short_len:
            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            # The nodes match, return the node
            return longer
        else:
            longer = longer.next
            shorter = shorter.next

    return None