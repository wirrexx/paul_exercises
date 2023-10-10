global_var = "I am global variable."

def local_fun():
    local_var = "I am local variable."
    print("Inside global", global_var)
    print("inside local", local_var)

local_fun()


