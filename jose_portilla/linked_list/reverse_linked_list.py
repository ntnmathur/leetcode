class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


# a --> b --> c --> d
# current = a
# next_node = b # save the next
#
# set current.nextnode = previous
#
# move forward
# previous = current
# current = next_node (that was saved)


def reverse(head):
    current = head
    previous = None
    saved_next_node = None

    while current:
        saved_next_node = current.nextnode
        current.next_node = previous

        previous = current
        current = saved_next_node

    return previous