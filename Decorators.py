from functools import wraps

def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
                print('before function execution')
                func(*args,**kwargs)
                print('after function execution')
        return wrapper

def chaining_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
                print("{} function is running".format(func.__name__))
                func(*args,**kwargs)
        return wrapper


x = decorator(lambda : print("function execution"))
x()
print("\n")

# above and below are the same thing different syntax
@chaining_decorator
@decorator
def y():
        print("y function executing")

y()
print("\n")

@decorator
def z(name):
        print(name)
z("samarth")

print("\n")

class class_decorator():
        def __init__(self,func):
                self.func = func
        
        def __call__(self, *args, **kwargs):
                print("before function execution")
                return self.func(*args,**kwargs)
        
@class_decorator
def func():
        print("decorated by a class")
func()
print("\n")
