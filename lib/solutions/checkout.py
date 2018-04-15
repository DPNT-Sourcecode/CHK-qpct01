

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    discounts = {'AAA': 130, 'BB': 45}
    prices = { 'A': 50, 'B': 30, 'C': 20, 'D': 15}

    price = 0
    count_aaa = skus.count('AAA')

    return count_aaa
