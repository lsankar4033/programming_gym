def pandigitals(num_digits):
    remaining_digits = set(range(1, num_digits + 1))
    return _pandig_recur([[]], remaining_digits)


def _pandig_recur(partials, remaining_digits):
    if len(remaining_digits) == 0:
        return partials

    result = []
    for d in remaining_digits:
        result += _pandig_recur([p + [d] for p in partials], remaining_digits.difference(set([d])))

    return result


def digits_to_num(ds):
    return int("".join([str(d) for d in ds]))


def _extract_elts(ds, m, e):
    return (digits_to_num(ds[0:m + 1]), digits_to_num(ds[m + 1:e + 1]), digits_to_num(ds[e + 1:]))


def is_valid_mult(ds, m, e):
    m1, m2, p = _extract_elts(ds, m, e)
    return m1 * m2 == p


def set_key(m1, m2):
    keyl = [m1, m2]
    keyl.sort()
    return tuple(keyl)


if __name__ == '__main__':
    print("generating pandigitals")
    pds = pandigitals(9)
    print(f"generated all {len(pds)} 9-pandigitals")

    psum = 0
    seen_factors = set()  # tuples of (smaller factor, larger factor)
    for pd in pds:
        for m in range(7):
            for e in range(m + 1, 8):
                if is_valid_mult(pd, m, e):
                    m1, m2, p = _extract_elts(pd, m, e)

                    key = set_key(m1, m2)

                    if key not in seen_factors:
                        print(f"took {m1} x {m2} = {p}")
                        seen_factors.add(key)
                        psum += p
                        print(f"psum: {psum}")

    print(f"psum = {psum}")
