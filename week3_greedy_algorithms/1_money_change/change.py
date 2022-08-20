def change(money):
    # write your code here
    denominations = [1, 5, 10]
    num_coins = 0

    while money > 0:
        max_coin = 0
        for coin in denominations:
            if coin <= money and coin > max_coin:
                max_coin = coin
        money = money - max_coin
        num_coins = num_coins + 1

    return num_coins


if __name__ == "__main__":
    m = int(input())
    print(change(m))
