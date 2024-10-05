def modify_tuple(internal_list, internal_string):
    internal_string = internal_string + ' lastname'
    internal_list[0] = 100


ex_string = 'name'
ex_list = [1, 2, 3]
modify_tuple(ex_list, ex_string)
print(ex_string, ex_list)
