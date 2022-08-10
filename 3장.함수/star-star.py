# ** 연산자는 파이썬이 딕셔너리에 들어있는 값을 함수에 전달하되
# 각 값에 대응하는 키를 키워드로 사용하도록 명령한다.
def remainder(number, divisor):
    return number % divisor

kwargs = { 'number': 20, 'divisor': 7 }
k1 = { 'number': 20 }
k2 = { 'divisor': 7 }
assert remainder(20, 7) == 6
assert remainder(**kwargs) == 6
assert remainder(**k1, **k2) == 6