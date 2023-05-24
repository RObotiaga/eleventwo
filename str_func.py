def all_title(string):
    """
    вся строка заглавными символами
    :param string:
    :return:
    """
    new_string = ''
    for i in string:
        new_string += i.title()
    return new_string


def all_word_title(string):
    """
    каждое слово начинается с заглавной
    :param string:
    :return:
    """
    new_string = ''
    for i in string.split(' '):
        new_string += i.title()
        new_string += ' '
    return new_string
