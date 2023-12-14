# skapa en dict. med key = färger och value : frukter
fruits = {
    'red': ['apple', 'cherry', 'strawberry'],
    'orange': ['orange', 'mango', 'peach'],
    'yellow': ['banana', 'lemon']
}

# lägg till en ny key = färg och ett nytt value : frukt
fruits['green'] = ['watermelon']
fruits.update({'green': ['watermelon']})


# ta bort yellow
fruits.pop('yellow')

# för key, value i fruits.item()
for color, colored_fruits in fruits.items():
    # skriv ut färg + fruits:
    print(color + ' fruits:')
    # för frukter i value
    for fruit in colored_fruits:
        print('- ' + fruit)
