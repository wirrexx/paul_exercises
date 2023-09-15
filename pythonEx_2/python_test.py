number = -120 
numberNew = number * -1 #abs räknar ut som -1
print (numberNew)


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
