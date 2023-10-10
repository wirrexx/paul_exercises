# Decorator func
def helloDec():
    return "Hello decorators"


def outer_func(func):
    # behavior of the inner function
    def inner_func():
        print("this is my decoration before passed function")
        message = func()
        print(message)
        print("this is my decoration after passed function")
        return "I am an inner function" + str (func) 
    
    return inner_func

receivedFunc = outer_func(helloDec)

print(receivedFunc())