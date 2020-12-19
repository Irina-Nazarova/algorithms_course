def stock_profit(stock_prices):
    """
    :param stock_prices: [7 1 5 3 6 4]
    :return: 7 - You need to display a number equal to the maximum possible profit for these days.
    """

    stock = "empty"
    stock_salary = 0
    for i in range(len(stock_prices) - 1):
        if stock == "empty":
            if stock_prices[i] < stock_prices[i + 1]:
                stock = stock_prices[i]

        else:
            if stock_prices[i] > stock_prices[i + 1]:
                stock_salary += stock_prices[i] - stock
                stock = "empty"

    return stock_salary


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        arr = f.read().split("\n")
        stock_prices = [int(i) for i in arr[0].split()]
        stock_prices.append(0)
        stock_salary = stock_profit(stock_prices)
        print(stock_salary)
