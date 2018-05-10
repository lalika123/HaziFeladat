class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    head=None
    def appendFront(self,data):
        new_e=Node(data)
        new_e.next=self.head
        self.head=new_e

    def appendBack(self,data):
        new_e=Node(data)
        if self.head is None:
            self.head=new_e
        else:
            current_item=self.head
            while current_item.next is not None:
                current_item=current_item.next
            current_item.next=new_e

    def remove(self,element):
        tmp=self.head
        previous=None
        while tmp is not None:
            if tmp.data==element:
                if previous is None:
                    self.head=self.head.next
                else:
                    previous.next=tmp.next
            previous=tmp
            tmp=tmp.next

    def show(self):
        tmp=self.head
        print("a lista elemei: ")
        while tmp is not None:
            print(tmp.data,'-> ',end="")
            tmp=tmp.next
        print("None")

s=LinkedList()
s.appendFront(23)
s.appendFront(42)
s.appendBack(11)
s.appendBack(77)
s.show()