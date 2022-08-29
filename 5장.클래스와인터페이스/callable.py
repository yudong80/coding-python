# defaultdict(default_factory)에서 default_factory()는 __missing__(self) 때 호출된다.
from collections import defaultdict

class CountMissing:
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return 0

current = {'초록': 12, '파랑': 3}
increments = {
    ('빨강', 5), ('파랑', 17), ('주황', 9)}

counter = CountMissing()
result = defaultdict(counter, current)  # callable object
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
