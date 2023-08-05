class FullListError(Exception):
    def __init__(self):
        super().__init__("List is full! Next element cannot be added")


class NoSuchElementError(Exception):
    def __init__(self, element):
        self.element = element
        super().__init__(f"{self.element} is not found in List.")


class NoSuchIndexError(Exception):
    def __init__(self, idx, last_idx):
        self.idx = idx
        self.last_idx = last_idx
        super().__init__(f"{self.idx} is out of range! The last index is {self.last_idx}")


class PushIncorrectTypeError(Exception):
    def __init__(self, input_type, allowed_type):
        self.input_type = input_type
        self.allowed_type = allowed_type
        super().__init__(f"Cannot push {self.input_type} because of its type. The only allowed is {self.allowed_type}.")


class PopOnEmptyListError(Exception):
    def __init__(self):
        super().__init__(f"Cannot pop because list is empty!")