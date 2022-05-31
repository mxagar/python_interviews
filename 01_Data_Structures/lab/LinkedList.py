from ListNode import Node

class LinkedList:
    def __init__(self):
        self.head_node = None

    # Insertion at Head: O(1)
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list

    # Check if head is None: O(1)
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    # Supplementary print function: O(n)
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(1, 10):
    list.insert_at_head(i)
list.print_list()
