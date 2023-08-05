from Exceptions import FullListError, NoSuchIndexError, NoSuchElementError, PushIncorrectTypeError, PopOnEmptyListError
from Node import Node


class LinkedList:
    _size = 0
    _free_spots = 0
    _allowed_type = None

    def __init__(self, size, head=None):
        self._free_spots = self._size = size
        self.head = head

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr:
            v = self.curr.data
            self.curr = self.curr.next
            return v
        else:
            raise StopIteration()

    def push(self, value):
        if self._free_spots == 0:
            raise FullListError
        elif self.head is None:
            self._allowed_type = type(value)
        elif type(value) is not self._allowed_type:
            raise PushIncorrectTypeError(type(value), self._allowed_type)

        new_value = Node(value)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_value
        else:
            self.head = new_value
        self._free_spots -= 1

    def pop_by_index(self, idx):
        if self.head is None:
            raise PopOnEmptyListError
        if idx >= self._size:
            raise NoSuchIndexError(idx, self._size)
        elif idx == 0:
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        for k, v in enumerate(self):
            if k == idx:
                prev.next = curr.next
                self._free_spots += 1
                return v

            prev = curr
            curr = curr.next

    def pop_by_value(self, value):
        if self.head is None:
            raise PopOnEmptyListError

        curr = self.head
        prev = None

        if curr.data is value:
            self.head = curr.next
            self._free_spots += 1
            return value
        for _, v in enumerate(self):
            if v == value:
                prev.next = curr.next
                self._free_spots += 1
                return value
            prev = curr
            curr = curr.next

        raise NoSuchElementError(value)

    def pop_all_occurrences(self, value):
        if self.head is None:
            raise PopOnEmptyListError

        curr = self.head
        removed_iter = 0
        it = 0

        while curr:
            if curr.data is value:
                self.head = curr.next
                self._free_spots += 1
                removed_iter += 1
                curr = curr.next
            elif curr.next is None:
                if removed_iter == 0:
                    raise NoSuchElementError(value)
                else:
                    return value
            elif curr.next.data is value:
                curr.next = curr.next.next
                self._free_spots += 1
                removed_iter += 1
            else:
                curr = curr.next
            it += 1

    def print_all(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print("None")
