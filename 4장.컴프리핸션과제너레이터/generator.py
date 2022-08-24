def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1           

address = '컴퓨터(영어: computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관'
it = index_words_iter(address)
print(next(it))
print(next(it))

def index_file(handle):
    offset = 0
    for line in handle: # 한줄 단위로 
        if line:
            yield offset
        for index, letter in enumerate(line): # enumerate로도 됨
            if letter == ' ':
                yield index + 1


import itertools
with open('address.txt', 'r', encoding='utf-8') as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10) #it, start, stop 
    print(list(results))
