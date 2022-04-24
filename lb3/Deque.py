from ListNode import ListNode
from DoubleLinkedList import DoubleLinkedList


class Deque:

    track_for_double = DoubleLinkedList()

    def test(self):
        self.track_for_double.output_list()

    def enqueue_first(self, smth):
        self.track_for_double.add_first_list_item(smth)
        return

    def enqueue_last(self, smth):
        self.track_for_double.add_list_item(smth)
        return

    def dequeue_first(self):

        if self.track_for_double.list_length() == 0:
            raise Exception("Queque empty")

        temp = self.track_for_double.get_first()
        self.track_for_double.remove_first_list_item()

        return temp

    def dequeue_last(self):

        if self.track_for_double.list_length() == 0:
            raise Exception("Queque empty")

        temp = self.track_for_double.get_last()
        self.track_for_double.remove_last_list_item()

        return temp

    def peek_first(self):

        if self.track_for_double.list_length() == 0:
            raise Exception("Queque empty")

        return self.track_for_double.get_first()

    def peek_last(self):

        length = self.track_for_double.list_length()

        if length == 0:
            raise Exception("Queque empty")

        return self.track_for_double.get_last()

    def count(self):
        return self.track_for_double.list_length()
