myNum = 123
myFloat = 43.23
complexNumber = 4-2j
isMarried = True
message = "'How are you?'"

# messageA = f"Is {myNum} an instance of Int?: {isinstance(myNum, int)}"
# messageB = f"Is {myFloat} an instance of bool?: {isinstance(myFloat, bool)}"
# messageC = f"Is {complexNumber} and instance of complex?: {isinstance(complexNumber, complex)}"
# messageD = f"Is {isMarried} an instance of bool?: {isinstance(isMarried, bool)}"
# messageE = f"Is {message} an instance of float?: {isinstance(message, float)}"

messageA2 = "is ",str(myNum),"an instance of Int?: ", isinstance(myNum, int)
messageA3 = "is ",str(myFloat),"an instance of bool?: ", isinstance(myFloat, bool)
messageA4 = "Is", str(complexNumber), "an instance of complex?: ", isinstance(complexNumber, complex)
messageA5 = "Is", isMarried, "an instance of bool?: ", isinstance(isMarried, bool)
messageA6 = "Is", message, "an instance of float?: ", isinstance(isMarried, float)

print(messageA2)
print(messageA3)
print(messageA4)
print(messageA5)
print(messageA6)
# print(messageA)
# print(messageB)
# print(messageC)
# print(messageD)
# print(messageD)
# print(messageE)