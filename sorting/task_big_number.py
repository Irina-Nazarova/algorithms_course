def big_number(array):
    """
    :param array: 10 24 100 51
    :return: 512410100
    """
    return sorted(array, key=lambda x: (x * 4)[:4], reverse=True)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        array = f.readline()
        print("".join(big_number(array)))