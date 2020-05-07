
g = 1504170715041707
p = 4503599627370517

g3 = 8912517754604

if __name__ == '__main__':
    cur = g3
    min_g = g3
    sum_g = 1513083232796311

    while cur != g:
        cur += g
        cur = cur % p
        if cur < min_g:
            print(f'Found coin: {cur}')
            min_g = cur
            sum_g += cur

    print(f'Found sum: {sum_g}')
