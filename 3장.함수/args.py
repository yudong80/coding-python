def safe_division_e(numerator, denominator, /,
    ndigits=10, *,
    ignore_overflow=False,
    ignore_zero_division=False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

r1 = safe_division_e(22, 7)
r2 = safe_division_e(22, 7, 5)
r3 = safe_division_e(22, 7, ndigits=2)
print(r1)
print(r2)
print(r3)