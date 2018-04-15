

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = ''.join(sorted(skus))
    discounts = {'AAA': 130, 'BB': 45}
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    price, skus = calculate_price(skus, discounts)
    both = calculate_price(skus, prices)

    price += both[0]
    skus = both[1]

    if skus:
        return -1
    return price

def calculate_price(skus, prices):
    price = 0

    for key in prices.iterkeys():
        price += skus.count(key) * prices[key]
        skus = skus.replace(key, '')
    
    return price, skus
