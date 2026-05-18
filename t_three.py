class FlatIterator:

    def __init__(self, list_of_list):
        self.iterator = iter(list_of_list)
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.stack:
                try:
                    item = next(self.stack[-1])
                    if isinstance(item, list):
                        self.stack.append(iter(item))
                    else:
                        return item
                except StopIteration:
                    self.stack.pop()
            else:
                try:
                    item = next(self.iterator)
                    if isinstance(item, list):
                        self.stack.append(iter(item))
                    else:
                        return item
                except StopIteration:
                    raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
