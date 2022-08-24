stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total={}

for key in list(stock.keys()):
    if key in prices.keys():
        b = stock.pop(key) * prices.pop(key)
        total.update({key:b})
print(total)
print('Total summ: ', sum(total.values()))

