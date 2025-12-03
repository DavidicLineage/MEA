def mea_order(n):
    a = list(range(1, n+1))
    result = []
    while a:
        m = len(a) // 2
        if len(a) % 2 == 1:
            result.append(a.pop(m))
        else:
            result.append(a.pop(m-1))
            result.append(a.pop(m-1))
        if not a:
            break
        result.append(a.pop(0))
        result.append(a.pop())
    return result

def mea_inverse(n):
    π = mea_order(n)
    inv = [0] * n
    for pos, value in enumerate(π, start=1):
        inv[value - 1] = pos
    return inv
