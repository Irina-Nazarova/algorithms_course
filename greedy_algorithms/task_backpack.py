def backpack_space(cost_weight: list, weight_limit: int) -> str:
    """
    :param cost_weight: [(0, 25, 50), (1, 30, 40), (2, 10, 80), (3, 2, 3)]
    :param weight_limit: 36
    :return: '1 2 3' displays in sorted order the numbers of items from the backpack
    """

    backpack = []

    cost_weight.sort(
        key=lambda x: (-x[1], x[2])
    )
    for i in cost_weight:
        if i[2] <= weight_limit:
            backpack.append(i)
            weight_limit -= i[2]
    backpack.sort(
        key=lambda x: x[0]
    )

    for i in backpack:
        print(i[0], end=" ")



