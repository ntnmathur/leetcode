def permute(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]

    return out


print(permute('abc'))

# >>> s = 'string'
# >>> s[:1]
# 's'
# >>> s[2:]
# 'ring'
# >>> s[:0]
