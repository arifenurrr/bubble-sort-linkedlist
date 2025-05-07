from ds import *

def bubble_sort(theSeq):
    if isinstance(theSeq, list):
        for i in range(len(theSeq) - 1):
            for j in range(len(theSeq) - i - 1):
                if theSeq[j] > theSeq[j + 1]:
                    theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
        return theSeq

    elif isinstance(theSeq, LinkedList):
        changed = True
        while changed:
            changed = False
            prev, curr = None, theSeq.head
            while curr and curr.next:
                if curr.data > curr.next.data:
                    theSeq.swap_nodes(prev, curr)
                    changed = True
                    curr = theSeq.head if prev is None else prev.next
                else:
                    prev, curr = curr, curr.next
        return theSeq

    else:
        raise TypeError("Unsupported data type for sorting")



