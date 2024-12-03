def outer(x):
    def inner():
        return x
    return inner

closure_func = outer(10)
print(closure_func.__closure__)  # (<cell at ...>,)
print('some')
