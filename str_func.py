
def all_title(string):
    """
    делает все символы в строке заглавными
    """
    new_string =''
    for i in string:
        new_string+= i.title()
    return new_string
