

def format(num):

    L=""

    while num >0:
        rem = num % 1000
        num = num / 1000
        print L

        L = str(rem)+','+L

    return L
















print format(12345)


