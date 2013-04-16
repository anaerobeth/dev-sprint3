lst = ['Blake', 'Tracy', 'Ilya', 'Beth', 'Beth', 'Beth']

def has_duplicates(lst):
    duplicates = {}
    for person in lst:
        if person in duplicates:
            return False
        else:
            duplicates[person] = 1
    return True

print has_duplicates(lst)
