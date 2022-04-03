from SingleLinkedList import SingleLinkedList
from ListNode import ListNode 
from DoubleLinkedList import DoubleLinkedList

node1 = ListNode(1)
node2 = ListNode(8.2)
node3 = ListNode("sgjhzd")
node4 = ListNode(15)
node5 = ListNode(78)
node6 = ListNode("dfkjvdljv")
node7 = ListNode(1)

# track_for_single = SingleLinkedList()
# print("track length: %i" % track_for_single.list_length())

# for current_item in [node1, node2, node3, node4, node5, node6, node7]:
#     track_for_single.add_list_item(current_item)
#     print("track length: %i" % track_for_single.list_length())
#     track_for_single.output_list()

# print("-----------")
# track_for_single.remove_first_list_item()
# print("track length: %i" % track_for_single.list_length())
# track_for_single.output_list()
# print("-----------")
# track_for_single.remove_middle_list_item()
# print("track length: %i" % track_for_single.list_length())
# track_for_single.output_list()
# print("-----------")
# track_for_single.remove_last_list_item()
# print("track length: %i" % track_for_single.list_length())
# track_for_single.output_list()

track_for_double = DoubleLinkedList()

print("track length: %i" % track_for_double.list_length())

for current_item in [node1, node2, node3, node4, node5, node6, node7]:
    track_for_double.add_list_item(current_item)
    print("track length: %i" % track_for_double.list_length())
    track_for_double.output_list()

print("-----------")
track_for_double.remove_first_list_item()
print("track length: %i" % track_for_double.list_length())
track_for_double.output_list()
print("-----------")
track_for_double.remove_middle_list_item()
print("track length: %i" % track_for_double.list_length())
track_for_double.output_list()
print("-----------")
track_for_double.remove_last_list_item()
print("track length: %i" % track_for_double.list_length())
track_for_double.output_list()
