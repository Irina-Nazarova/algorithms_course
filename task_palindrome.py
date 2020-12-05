def polindrome(words: str):
    """
    :param data: "A man, a plan, a canal: Panama" -str
    :return: True
    """
    word_reverse = (
        words.replace(":", "")
        .replace(",", "")
        .replace(" ", "")
        .replace(".", "")
        .lower()
    )

    slice_words = word_reverse[::-1]

    if word_reverse == slice_words:
        return True
    else:
        return False


polindrome("A man, a plan, a canal: Panama")
