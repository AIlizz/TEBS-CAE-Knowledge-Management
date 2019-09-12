def test():
    name = "huijie sister"
    action = 'hello'
    while True:
        name = input("what's your name?")
        if name == 'huijie sister':
            print('success!')
            break

def test1(name = 'huijie sister'):
    for i in range(10):
        print()
    if True:
        pass
    return 1

test1()
