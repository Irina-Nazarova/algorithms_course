def polindrome(word: str):
    """
    :param data: "A man, a plan, a canal: Panama" -str
    :return: True
    """
    word1 = (
        word.replace(":", "")
        .replace(",", "")
        .replace(" ", "")
        .replace(".", "")
        .lower()
    )
    word2 = word1[::-1]

    if word1 == word2:
        return True
    else:
        return False


polindrome("A man, a plan, a canal: Panama")
