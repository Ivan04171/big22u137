from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.data=iter(items)
        self.ignore_case=kwargs.get('ignore_case',False)
        self.unique_items=set()

    def __next__(self):
        while True:
            item=next(self.data)
            nekto = item.lower() if self.ignore_case else item
            if nekto not in self.unique_items:
                self.unique_items.add(nekto)
                return item

    def __iter__(self):
        return self
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_iter = Unique(data)
print(*unique_iter)
data = gen_random(10, 1, 3)
unique_iter = Unique(data)
print(*unique_iter)
data = ['a', 'A','b', 'B', 'a', 'A', 'b', 'B']
unique_iter = Unique(data)
print(*unique_iter)
unique_iter_ignore_case = Unique(data, ignore_case=True)
print(*unique_iter_ignore_case)