from functools import wraps

def decorator_function(org_function):
    @wraps(org_function)    
    def wrapper(*args, **kwargs):
        print(f'{org_function.__name__} 이 실행 전')
        return org_function(*args, **kwargs)
    return wrapper

@decorator_function
def print_message(message):
    """ message를 출력 """
    print(message)

print_message('Hello')
help(print_message)