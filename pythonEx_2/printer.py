def printer_error(s):
    count = 0
    letters = 'abcdefghijklm'

    for char in s: 
        if char not in letters: 
            count += 1

    error_rate = f"{count}/{len(s)}"

    return error_rate 


s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

value = (printer_error(s))
print(value)