

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = ''.join(sorted(skus))

    prices = (('AAAAA', 200), ('AAA', 130), ('BB', 45), ('A', 50), ('B', 30), ('C', 20), ('D', 15), ('E', 40))

    price, skus = calculate_price(skus, prices)

    if skus:
        return -1
    return price

def calculate_price(skus, prices):
    price = 0

    for key, value in prices:
        price += skus.count(key) * value
        skus = skus.replace(key, '')
    
    return price, skus
