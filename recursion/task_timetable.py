def optimal_time_table(timetable: list) -> list:
    """
    :param timetable: [(9.0, 10.0), (9.3, 10.3), (10.0, 11.0), (10.3, 11.3)]
    :return: [(9.0, 10.0), (10.0, 11.0)]
    schedule with the largest number of lessons.
    """

    timetable.sort(key=lambda x: (x[1], x[0]))
    new_timetable = []
    i = 0

    while i < len(timetable):
        if i == 0:
            new_timetable.append(timetable[i])
            i += 1
            continue

        if new_timetable[-1][1] <= timetable[i][0]:
            new_timetable.append(timetable[i])
        i += 1

    return new_timetable





