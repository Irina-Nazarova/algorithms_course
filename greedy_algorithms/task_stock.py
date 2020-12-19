def stock_profit(stock_prices):
    """
    :param stock_prices: [7 1 5 3 6 4]
    :return: 7 - Нужно вывести число, равное максимально возможной прибыли за эти дни.
        Если акций нет на руках: Покупаю если сегодня цена меньше чем завтpа. continue
        Если акция есть на руках: Продаю если цена завтра меньше чем сегодня. continue
        В остальных случаях ничего не предпринимаю.
    """
    stock = "empty"
    stock_salary = 0
    for i in range(len(stock_prices) - 1):
        # Купленных акций нет
        if stock == "empty":
            if stock_prices[i] < stock_prices[i + 1]:
                # Если цена сегодня меньше чем завтра - покупаем
                stock = stock_prices[i]

        # Купленные акции есть
        else:
            # Решаем, что сегодня делать с акцией
            # Если завтра она стоит меньше - продаем
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

