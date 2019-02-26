# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.
#
# For example:
#
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
#
# 1+1+1+1+1+1+1+1+1+1
#
# 5 + 1+1+1+1+1
#
# 5+5
#
# 10
#
# With 1 coin being the minimum amount.

def rec_coin(target, coins):
    min_coins = target
    # Base Case
    if target in coins:
        return 1

    else:
        for i in [c for c in coins if c <=target]:

            num_coins = 1 + rec_coin(target -i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

# print(rec_coin(60,[1,5,10,25]))


def rec_coin_dynam(target, coins, known_results):
    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1

    elif known_results[target] > 0:
        return known_results[target]

    else:
        for i in [c for c in coins if c<=target]:
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                known_results[target] = min_coins

    return min_coins

known_results = [0]*(60+1)
print(rec_coin_dynam(60,[1,5,10,25], known_results) )