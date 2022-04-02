# script accompanying https://www.youtube.com/watch?v=Wim9WJeDTHQ
def per(n, i=0):
    s = str(n)

    l = len(s)

    if l == 1:
        return i

    r = 1

    for x in s:
        r *= int(x)

    print(r)

    return per(r, i+1)


n = 277777788888899
result = per(n)

print('{} steps'.format(result))
