def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

#1
def normalize(numbers):
    total = sum(numbers)    # 여기서 소진이 되어 버림!
    result = []
    for value in numbers:   # 여기는 그냥 pass됨
        percent = 100 * value / total
        result.append(percent)
    return result

#2
def normalize_copy(numbers):
    numbers_copy = list(numbers) # 메모리를 과도하게 복사할 문제가 있음(가비지 컬렉팅?)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:   # 여기는 그냥 pass됨
        percent = 100 * value / total
        result.append(percent)
    return result

#3 
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self): # 이터러블 컨테이너
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits('my_numbers.txt')
percentages = normalize(visits)
print(percentages) 
assert sum(percentages) == 100

