

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    discounts = {'AAA': 130, 'BB': 45}
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    price = 0
    for key in discounts.iterkeys():
        price += skus.count(key) * discounts[key]
        skus = skus.replace(key, '')
    
    for key in prices.iterkeys():
        price += skus.count(key) * discounts[key]
        skus = skus.replace(key, '')

    return price
