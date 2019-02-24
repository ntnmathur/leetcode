def balance_check(s):
    if len(s)%2 != 0:
        return False

    opening_brackets = set('{([')
    bracket_set = set([ ('{','}'), ('(',')'), ('[',']')])
    stack = []

    for elem in s:
        if elem in opening_brackets:
            stack.append(elem)

        else:
            if len(stack) == 0:
                return False

            last_opening_bracket = stack.pop()
            if (last_opening_bracket, elem) not in bracket_set:
                return False
    return len(stack) == 0

print(balance_check('[]'))

print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
