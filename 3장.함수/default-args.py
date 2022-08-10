# default 객체가 공유되는 문제 발생!
import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print(f'Foo: {foo}')
print(f'Bar: {bar}')