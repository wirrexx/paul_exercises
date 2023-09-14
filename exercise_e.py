myNum = 123
myFloat = 43.23
complexNumber = 4-2j
isMarried = True
message = "'How are you?'"

messageA = (f"Is {myNum} and instance of Int?: {(isinstance(myNum, int))}")
messageB = (f"Is {myFloat} and instance of bool?: {(isinstance(myFloat, bool))}")
messageC = (f"Is {complexNumber} and instance of complex?: {(isinstance(complexNumber, complex))}")
messageD = (f"Is {isMarried} and instance of bool?: {(isinstance(isMarried, bool))}")
messageE = (f"Is {message} and instance of float?: {(isinstance(message, float))}")

print(messageA)
print(messageB)
print(messageC)
print(messageD)
print(messageD)
print(messageE)