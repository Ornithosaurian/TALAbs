from ListNode import ListNode


class DoubleLinkedList:
    def __init__(self):

        self.head = None
        self.tail = None

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

    def add_list_item(self, item):

        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

        return

    def remove_first_list_item(self):

        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if previous_node is not None:
                previous_node.next = next_node
                if next_node is not None:
                    next_node.previous = previous_node
            else:
                self.head = next_node
                if next_node is not None:
                    next_node.previous = None

            return

        return

    def remove_middle_list_item(self):

        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_id == int(self.list_length() / 2):

                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None

                return

            current_node = next_node
            current_id = current_id + 1

        return

    def remove_last_list_item(self):

        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_id == self.list_length():

                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None

                return

            current_node = next_node
            current_id = current_id + 1

        return

    def add_first_list_item(self, item):

        item = ListNode(item)

        if self.head is None:
            self.head = item

            return

        self.head.previous = item
        item.next = self.head
        self.head = item

        return

    def add_middle_list_item(self, item, position):

        item = ListNode(item)

        if position < 1:
            print("Can't be less than 1")

        elif position == 1:
            item.next = self.head
            self.head.previous = item
            self.head = item

        else:
            current_node = self.head

            for i in range(1, position - 1):

                if current_node is not None:
                    current_node = current_node.next

            if current_node is not None:
                item.next = current_node.next
                item.previous = current_node
                current_node.next = item

            else:
                print("Previos node is null")


    def serch_list_item_index(self, data):

        current_item = self.head
        count_index = 0

        while current_item is not None:
            count_index+=1

            if current_item.data==data:
                return count_index

            current_item = current_item.next

