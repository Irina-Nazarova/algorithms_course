def mortgage(budget_limit: int, cost_houses: list) -> int:
    """
    :param budget_limit: 1000
    :param cost_houses: [320, 900, 200]
    :return: 2 - displays as many houses as possible
    """
    cost_houses.sort()
    count = 0
    for i in cost_houses:
        if i <= budget_limit:
            count += 1
            budget_limit -= i
    return count


