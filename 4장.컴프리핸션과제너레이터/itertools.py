import itertools

it = itertools.chain([1,2,3], [4,5,6])
print(list(it))

it = itertools.cycle([1,2])
result = [next(it) for _ in range(3)]
print(result)

it1, it2, it3 = itertools.tee(['하나','둘'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

keys = ['하나', '둘', '셋']
values = [1, 2]
it = itertools.zip_longest(keys, values, fillvalue='None')
print(list(it))

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(itertools.islice(keys, 5)))
print(list(itertools.takewhile(lambda x: x<7, values)))
print(list(itertools.dropwhile(lambda x: x<7, values)))
print(list(itertools.filterfalse(lambda x: x % 2 == 0, values)))
print('합계: ', list(itertools.accumulate(values)))
print('product: ', list(itertools.product([1, 2], ['a', 'b'])))