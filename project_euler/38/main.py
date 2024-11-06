
def is_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')

# OOPS: pandigital is all digits included
def conc_product(n, max_d=9):
    buff = ""
    for i in range(1, max_d + 1):
        buff += str(n * i)

    return buff
    
def naive_iterate():
    max_p = 1
    for n in range(1, 10000):
        max_d = 2
        while True:
            p = conc_product(n, max_d)
            if len(p) > 9:
                break

            p_i = int(p)
            if p_i > max_p and is_pandigital(p):
                print(f'New max: {p_i}; n: {n}, d: {max_d}')

                max_p = p_i

            max_d += 1
            


naive_iterate()