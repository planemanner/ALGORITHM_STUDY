
def gcd_basic(a, b):
    # 대소에 관계없이.
    if a == 0:
        return b
    return gcd_basic(b % a, a)


def pollard_rho(n):
    # 구현은 추후에...
    pass