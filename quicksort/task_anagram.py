def anagram(word_first: list, word_second: list):
    """
    :param word_first: moshkapa - ['a', 'a', 'h', 'k', 'm', 'o', 'p', 's']
    :param word_second: pomashka - ['a', 'a', 'h', 'k', 'm', 'o', 'p', 's']
    :return: True
    """
    word_first = sorted(list())
    word_second = sorted(list())
    result = True
    i = 0
    while i <= len(word_first) - 1 and result:
        if word_first[i] != word_second[i]:
            result = False
        i += 1
    return result



