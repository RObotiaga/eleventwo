
def all_title(string):
    new_string =''
    for i in string:
        new_string+= i.title()
    return new_string
print(all_title('колбаса'))