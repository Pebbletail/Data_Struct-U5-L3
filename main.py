#Luke Brudnok
#2/5/25

from DLLClass import DoublyLinkedList
from SLLClass import SinglyLinkedList

def create_DLL():
    linkedList = DoublyLinkedList()
    values = ["A", "B", "C", "D"]
    for val in values:
        linkedList.tail_insert(val)
    
    return linkedList

def create_SLL():
    linkedList = SinglyLinkedList()
    values = ["A", "B", "C", "D"]
    for val in values:
        linkedList.tail_insert(val)
    
    return linkedList

def reverse_LL(linkedList):
    if len(linkedList) == 0:
        return
    else:
        node = linkedList.head_remove()
        reverse_LL(linkedList)

        linkedList.tail_insert(node)

    return linkedList




def main():
    singlyLinked = create_SLL()
    print(f" initial singly linked: {singlyLinked}")
    reversedSL = reverse_LL(singlyLinked)

    print(f" reversed singly linked: {reversedSL}\n\n")

    doublyLinked = create_DLL()
    print(f" initial doubly linked: {doublyLinked}")
    reversedDL = reverse_LL(doublyLinked)

    print(f" reversed doubly linked: {reversedDL}")

if __name__ == "__main__":
    main()