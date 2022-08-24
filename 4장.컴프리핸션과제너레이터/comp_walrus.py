stock = { 
    '못': 125, 
    '나사못': 35,
    '나비너트': 8, 
    '와셔': 24,
}
order = ['나사못', '나비너트', '클립']

def get_batches(count, size):
    return count // size

# old school
result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

# walrus used
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name,0), 8))}
print(found)


# walrus +1 
result = {name: tenth for name, count in stock.items() 
          if (tenth := count // 10) > 0}
print(result)

# walrus +2
half = [(last := count //2) for count in stock.values()] # last 변수가 누출됨
print(f'{half}의 마지막 원소는 {last}')

