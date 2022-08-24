# send 쓰지 말자!
def generator_for_send():
    while True:
        get_value = yield
        print(f'value {get_value} get')
        yield get_value

gen = generator_for_send()
values = [1, 2, 3, 4]
for send_value in values:
    next(gen)
    gen.send(send_value)

