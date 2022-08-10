def divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('잘못된 입력')

x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('wrong')
else:
    print(f'결과는 {result}')
