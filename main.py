from functools import wraps
from time import perf_counter

from LinkedList import LinkedList


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = perf_counter()
        res = func(*args, **kwargs)
        end_time = perf_counter()

        total = end_time - start_time
        print(f"Time of execution - {total} \t- {timeit_wrapper.__name__}")
        return res

    return timeit_wrapper


LL2 = LinkedList(1000)
lst = []


@timeit
def calculate_insertion_my_array():
    for i in range(0, 1000):
        LL2.push(i)


@timeit
def calculate_insertion_default_array():
    for i in range(0, 1000):
        lst.append(i)


@timeit
def calculate_removing_in_reverse_order_in_my_array():
    for i in range(999, -1, -1):
        LL2.pop_by_index(i)


@timeit
def calculate_removing_in_reverse_order_in_default_array():
    for i in range(999, -1, -1):
        lst.remove(i)


def test_of_linked_list():
    LL = LinkedList(5)
    LL.push(2)
    LL.push(5)
    LL.push(8)
    LL.print_all()
    LL.pop_by_value(2)
    LL.print_all()
    LL.push(6)
    LL.push(6)
    LL.push(7)
    LL.print_all()
    LL.pop_by_value(6)
    LL.print_all()
    LL.push(8)
    LL.print_all()
    LL.pop_by_index(0)
    LL.print_all()
    LL.pop_by_value(7)
    LL.print_all()
    LL.push(5)
    LL.print_all()
    LL.pop_all_occurrences(8)
    LL.print_all()
    LL.push(1)
    LL.print_all()
    LL.pop_all_occurrences(5)
    LL.print_all()
    LL.pop_all_occurrences(1)
    LL.print_all()


if __name__ == '__main__':
    calculate_insertion_my_array()
    calculate_insertion_default_array()
    calculate_removing_in_reverse_order_in_my_array()
    calculate_removing_in_reverse_order_in_default_array()

    test_of_linked_list()
