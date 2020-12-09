def cockroach_racing(team_first, team_second):
    """
    :param team_first: 4 9 5
    :param team_second: 9 4 9 8 4
    :return: 4 9 - проверяет наличие участника команды team_first в team_second
    """

    arr = [1002]*1002

    for i in team_second:
        arr[i] = i

    result = []

    for k in team_first:
        if k == arr[k]:
            if k not in result:
                result.append(k)

    print(*result)



