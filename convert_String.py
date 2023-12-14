text = ['the_stealth_warrior', 'the-stealth-warrior']


def to_camel_case(text):
    result = []

    for char in text:
        # Split the string by underscores
        words = char.replace('-', '_').split('_')
        words = [word.capitalize() for word in words]  # Capitalize each word
        result.append(words[0].lower() + ''.join(words[1:]))

    return result


text = ['the_stealth_warrior', 'the-stealth-warrior']
x = to_camel_case(text)

for item in x:
    print(item)
