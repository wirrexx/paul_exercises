x, y , z = "Red", "Green", "Blue" # Dont do this, for readability!


#Do this, For readability! Easier to debug as Variables are more seperated.
x = "Red"
y = "Green"
z = "Blue"

myAge = None
bar = None


# Using bool() casting på olika datatyper

print(bool())
print(bool(""))  #Empty string = false  Written string = true
print(myAge)
print(bar)


def calculate_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else: 
        return "odd"
    
try:
    num = int (input("Enter A number: "))
    result = calculate_odd_even(num)
    print(f"{num} is {result}")
except ValueError:
    print("Enter an Integer!")
