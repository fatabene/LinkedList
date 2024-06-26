import copy


class Node:
    def __init__(self, data, link=None):
        self._data = data
        self._link = link

    def count_nodes(self):
        if self._link is None:
            # base case: return something
            return 1
        else:
            # make a recursive call and return something
            return 1 + self._link.count_nodes()

    def contains(self, item):
        # Base case: Item found
        if self._data == item:
            return True
        # Base case: Reached the end of the list
        elif self._link is None:
            return False
        else:
            # make a recursive call and return something
            return self._link.contains(item)

    def __iter__(self):
        # Yield the data of the current node
        yield self._data
        # If there is a next node
        if self._link is not None:
            # Yield each one of the elements from the linked list that follows
            yield from self._link

    def __reversed__(self):
        # If there is a next node
        if self._link is not None:
            # Yield each one of the elements from the linked list that follows
            yield from reversed(self._link)
        # Yield the data of the current node
        yield self._data

    def add_last(self, item):
        if self._link is None:
            # base case: add the new node
            self._link = Node(item)
        else:
            # recursive call
            self._link.add_last(item)

    def reverse_nodes(self):
        if self._link is None:
            return self
        else:
            node = self._link.reverse_nodes()
            self._link._link = self
            return node

    def copy_nodes(self):
        if self._link is None:
            return Node(self._data)
        else:
            return Node(self._data, self._link.copy_nodes())

    def operate_on_nodes(self, fun):
        if self._link is None:
            self._data = fun(self._data)
        else:
            self._data = fun(self._data)
            self._link.operate_on_nodes(fun)

    def remove_node(self, item):
        if self._data == item:
            return self._link
        elif self._link is None:
            return self
        else:
            self._link = self._link.remove_node(item)
            return self


class LinkedList:
    def __init__(self):
        self._head = None

    def add_first(self, item):
        self._head = Node(item, self._head)

    def __len__(self):
        # If the list is empty
        if self._head is None:
            # An empty list has length 0
            return 0
        else:
            # Call the recursive method count_nodes in the Node class
            return self._head.count_nodes()

    def __contains__(self, item):
        # If the list is empty
        if self._head is None:
            # An empty list does not contain any element
            return False
        else:
            # Call the recursive method contains in the Node class
            return self._head.contains(item)

    def __iter__(self):
        # If the list is not empty
        if self._head is not None:
            # Use the head node as an iterator: indirect call to __iter__
            yield from self._head

    def __reversed__(self):
        # If the list is not empty
        if self._head is not None:
            # Use the head node as an iterator: indirect call to __iter__
            yield from reversed(self._head)

    def add_last(self, item):
        # If the list is empty
        if self._head is None:
            # Adding last to an empty list is the same as adding first
            self.add_first(item)
        else:
            # Call the recursive method in the Node class
            self._head.add_last(item)

    def reverse(self):
        if self._head is not None:
            # Call the recursive method in the Node class
            new_head = self._head.reverse_nodes()
            self._head._link = None
            self._head = new_head

    def __copy__(self):
        if self._head is not None:
            return self._head.copy_nodes()

    def operate(self, fun=lambda x: x):
        if self._head is not None:
            self._head.operate_on_nodes(fun)

    def remove(self, item):
        if self._head is not None:
            self._head = self._head.remove_node(item)


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(5):
        ll.add_last(i)

    ll.reverse()
    ll.remove(2)

    for element in ll:
        print(element, end=' ')
    print()

    for element in reversed(ll):
        print(element, end=' ')
    print()

    for i in range(10):
        print(i in ll, end=' ')
    print()

    print(len(ll))

    ll2 = copy.copy(ll)

    for element in ll2:
        print(element, end=' ')
    print()

    ll.operate(lambda x: 2 * x + 1)

    for element in ll:
        print(element, end=' ')
    print()

    for element in ll:
        print('->', element, end=' ')
