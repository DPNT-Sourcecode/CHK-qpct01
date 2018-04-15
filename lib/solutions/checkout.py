

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = ''.join(sorted(skus))

    prices = (('AAAAA', 200), ('AAA', 130), ('BB', 45), ('HHHHHHHHHH', 80), ('HHHHH', 45), ('KK', 150), ('PPPPP', 200), ('QQQ', 80), ('VVV', 130), ('VV', 90), ('A', 50), ('B', 30), ('C', 20), ('D', 15), ('E', 40), ('F', 10), ('G', 20), ('H', 10), ('I', 35), ('J', 60), ('K', 80),
              ('L', 90), ('M', 15), ('N', 40), ('O', 10), ('P', 50), ('Q', 30), ('R', 50), ('S', 30), ('T', 20), ('U', 40), ('V', 50), ('W', 20), ('X', 90), ('Y', 10), ('Z', 50))

    price, skus = buy_n_get_one_for_free(2, skus, 20, 'F')

    both = buy_one_group_get_one_for_free(skus, 80, 'EE', 'B')
    price += both[0]
    skus = both[1]

    both = buy_one_group_get_one_for_free(skus, 120, 'NNN', 'M')
    price += both[0]
    skus = both[1]

    both = buy_one_group_get_one_for_free(skus, 150, 'RRR', 'Q')
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

def buy_n_get_one_for_free(n, skus, price, product):
    group = product * (n + 1)
    count = skus.count(group)
    return count * price, skus.replace(group, '')