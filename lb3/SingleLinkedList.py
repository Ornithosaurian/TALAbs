from ListNode import ListNode


class SingleLinkedList:
    def __init__(self):

        self.head = None
        self.tail = None

        return
    
    def add_list_item(self, item):
        
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
            
        return
    
    def list_length(self):
        
        count = 0
        current_node = self.head
        
        while current_node is not None:
            
            count = count + 1
            current_node = current_node.next
            
        return count

    def output_list(self):
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def remove_middle_list_item(self):

        current_id = 1
        current_node = self.head
        previous_node = None
        
        while current_node is not None:
            if current_id == int(self.list_length()/2):
 
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

                    return
            
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        
        return
    
    def remove_first_list_item(self):

        current_node = self.head
    
        while current_node is not None:
                    
            self.head = current_node.next

            return
            
        return

    def remove_last_list_item(self):

        current_id = 1
        current_node = self.head
        previous_node = None
        
        while current_node is not None:
            if current_id == self.list_length():
 
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

                    return
            
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        
        return
