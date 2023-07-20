def pow(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base

        return 1 / result if exponent < 0 else result