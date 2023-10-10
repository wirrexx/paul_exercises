def getParity(num, parity):
    if parity == 'Odd':
        boolean = bool(num %2 != 0)
        return boolean
    elif parity == 'Even':
        boolean = bool(num %2 == 0)
        return boolean
    else:
        return 'Parity indicated is unknown'


print(getParity(1, 'Odd'), getParity(1, 'Even'))
print(getParity(657842, 'Odd'), getParity(657842, 'Even'))
print(getParity(0, 'Odd'), getParity(0, 'Even'))
print(getParity(-2, 'number'))