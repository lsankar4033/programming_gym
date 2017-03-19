md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def acc(lis):
    total = 0
    for x in lis:
        total += x
        yield total


def leap_year(y):
    if y % 100 is 0:
        return y % 400 is 0
    else:
        return y % 4 is 0


def days(m, y):
    if leap_year(y) and m is 1:
        return 29
    else:
        return md[m]


def fm_sundays_in_year(sd, y):
    y_md = [days(m, y) for m in xrange(12)]
    y_md_acc = list(acc(y_md))[0:-1]  # Remove last month

    total = 1 if sd is 6 else 0
    total += len(filter(lambda a: (a + sd) % 7 is 6, y_md_acc))

    new_sd = (sum(y_md) + sd) % 7

    return [new_sd, total]


if __name__ == "__main__":
    [start_day, _] = fm_sundays_in_year(0, 1900)

    total = 0
    for y in xrange(1901, 2001):
        [start_day, t] = fm_sundays_in_year(start_day, y)
        total += t

    print total
