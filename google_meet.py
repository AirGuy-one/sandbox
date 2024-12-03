def some():
    def inner(func):
        print('1')

    return inner


@some()
def another():
    print('1')

another()
