class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
            
    def swap ( self , a, b ) :
        
        find_a = self.head
        find_b = self.head
        prev_a = self.head
        prev_b = self.head
        
        while ( find_a.data != a ) :
            prev_a = find_a
            find_a = find_a.next
        
        while ( find_b.data != b ) :
            prev_b = find_b
            find_b = find_b.next
        
        prev_a.next = find_b
        prev_b.next = find_a

        temp = find_a.next
        find_a.next = find_b.next
        find_b.next = temp

llist = LinkedList()
llist.head = Node ( 1 )
llist.head.next = Node ( 2 )
llist.head.next.next = Node ( 3 )
llist.swap ( 2 , 3 )
llist.printList()