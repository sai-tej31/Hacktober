#Imma implement it
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        itr = self.head
        llist=''
        while itr:
            llist += str(itr.data)+'-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llist)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_at_beginning(self,data):
        self.head = Node(data,self.head)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_at_index(self,index,data):
        if index<0 or index >= self.get_length():
            raise Exception("Check the index Bruh")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break 
            itr = itr.next
            count += 1
    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Check the index Bruh")

        if index == 0:
            self.head = self.head.next
            return
        count =0
        itr =self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_values(self,data_list):
        self.head =None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next
        return
    def remove_by_value(self, data):
        if data == self.head.data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        return

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

