# get value of nth node from end
# start with 2 pointers -> 1st and nth (From beginning)
# Move both 1 by 1. As soon as 2nd pointer hits the end, 1st one is nth from end


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    #assign right node to nth node
    for i in range(n-1):
        if not right_pointer.nextNode:
            raise LookupError("n is larger than linkedlist size")

        right_pointer = right_pointer.nextNode

    # as long as right node is not None
    while right_pointer.nextNode:
        left_pointer = left_pointer.nextNode
        right_pointer = right_pointer.nextNode

    return left_pointer




from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e



####

class TestNLast(object):

    def test(self,sol):

        assert_equal(sol(2,a),d)
        print('ALL TEST CASES PASSED')

# Run tests
t = TestNLast()
t.test(nth_to_last_node)
