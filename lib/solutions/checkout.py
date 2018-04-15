

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    discounts = {'AAA': 130, 'BB': 45}
    prices = { 'A': 50, 'B': 30, 'C': 20, 'D': 15}


    return price, skus

def calculate_prices():
    price = 0
    for discount in discounts.iterkeys():
        price += skus.count(discount) * discounts[discount]
        skus = skus.replace(discount, '')
    return price, skus