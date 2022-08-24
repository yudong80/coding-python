stock = { 
    '못': 125, 
    '나사못': 35,
    '나비너트': 8, 
    '와셔': 24,
}
order = ['나사못', '나비너트', '클립']

def get_batches(count, size):
    return count // size

found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))

print(next(found))
print(next(found))
