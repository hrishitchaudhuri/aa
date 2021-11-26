"""Module for prime related functions"""
import math
import random

def extended_gcd(num_1, num_2):
    """
    Returns a tuple (r, i, j) such that r = gcd(num_1, num_2) = i*num_1 + j*num_2
    """
    x_0 = 0
    y_0 = 1
    lx_0 = 1
    ly_0 = 0
    orig_a = num_1
    orig_b = num_2

    while num_2 != 0:
        quot = num_1 // num_2
        (num_1, num_2) = (num_2, num_1 % num_2)
        (x_0, lx_0) = ((lx_0 - (quot * x_0)), x_0)
        (y_0, ly_0) = ((ly_0 - (quot * y_0)), y_0)
    if lx_0 < 0:
        lx_0 += orig_b
    if ly_0 < 0:
        ly_0 += orig_a
    return num_1, lx_0, ly_0


def inverse(orig, mod):
    """
    Returns the inverse of orig % mod under multiplication.
    """

    (divider, inv, _) = extended_gcd(orig, mod)

    if divider != 1:
        raise ValueError(orig, mod, divider)

    return inv


def pseudoprime(num):
    """
    Runs Fermat's pseudo-prime test on base 2.
    """
    if pow(2, num-1, num) != 1:
        return False
    return True


def trial_division(num):
    """
    Tests primality via trial by division.
    """
    for check in range(math.ceil(math.sqrt(num))):
        if num % check == 0:
            return False
    return True


def miller_rabin_primality_testing(num, error):
    """
    Runs the Miller-Rabin test.
    """
    if num < 2:
        return False

    diff = num - 1
    rem = 0

    while not diff & 1:
        rem += 1
        diff >>= 1

    for _ in range(error):
        rand = random.randint(1, num - 1)

        check = pow(rand, diff, num)
        if check in (1, num - 1):
            continue

        for _ in range(rem - 1):
            check = pow(check, 2, num)
            if check == 1:
                return False
            if check == num - 1:
                break
        else:
            return False

    return True
