

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = ''.join(sorted(skus))

    prices = (('AAAAA', 200), ('AAA', 130), ('BB', 45), ('A', 50), ('B', 30), ('C', 20), ('D', 15), ('E', 40), ('F', 10))

    price, skus = buy_one_group_get_one_for_free(skus, 80, 'EE', 'B')
    
    both = buy_one_group_get_one_for_free(skus, 20, 'FF', 'F')
    price += both[0]
    skus = both[1]

    both = calculate_price(skus, prices)
    price += both[0]
    skus = both[1]

    if skus:
        return -1
    return price

def calculate_price(skus, prices):
    price = 0

    for key, value in prices:
        price += skus.count(key) * value
        skus = skus.replace(key, '')
    
    return price, skus

def buy_one_group_get_one_for_free(skus, price, group, free):
    count = skus.count(group)
    skus = skus.replace(group, '')
    skus = skus.replace(free, '', count)
    return count * price, skus

def buy_two_get_one_for_free(skus, price, product):