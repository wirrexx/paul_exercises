print(" A simple return statement example in Python")


def square():
    i = 2
# an infinite loop using the while loop to generate the squares
    while True:
        yield i*i
        i += 1


# Calling the above-created function using the 'for-loop' function.
for val in square():
    # using the 'if condition' to print the square, and the 'break' function to stop the loop.
    if val > 60:
        break
    print(val)


# Case 2
print("To illustrate functions that can return another function")

# Creating a user-defined function that shall return another function.


def adderCreate(a):
    # craeting a UDF inside a UDF to showcase how the return statement can be implemented in various ways
    def adder(b):
        return a + b

    return adder


# taking input from the user of the program.
num1 = int(input(" Please enter a number: "))
# variale created to store the value obtained from the UDF created above.
add_int = adderCreate(num1)
num2 = int(input(" Please enter a number: "))
# printing the output
print("The output from the adderCreate() function is", add_int(num2))

# Another function to return a value


def extra(s):
    return s * 66
# craeting a UDF


def FuncSample():

    # returning a different function inside a UDF
    return extra


# storing the function in res
output = FuncSample()
# taking input from the user of the program.
num1 = int(input(" Please enter a number: "))
print("\nThe output  is:", output(num1))
