"""理解 *args、**kwargs

- *args、**kwargs 是可变参数列表(Variable Arguments)
- *args = position arguments
- **kwargs = keyword arguments
- *args 必须位于 **kwargs 之前
"""

def test_args(first, *args, **kwargs):
    print(f'Required argument: {first}')
    for v in args:
        print(f'Optional argument(*args): {v}')
    for k, v in kwargs.items():
        print(f'Optional argument(**kwargs): {k} = {v}')

test_args(1, 2, 3, 4, k1=5, k2=6)


"""
*args、**kwargs 不仅可以在函数定义中使用(将参数pack的过程)，
也可在函数调用时使用(将参数unpack的过程)
"""

args = [1, 2, 3, 4, 5]
kwargs = {
    'first': 10,
    'second': 20,
    'third': 30,
    'fourth': 40,
    'fifth': 50
    }

def test_args2(first, second, third, fourth, fifth):
    print(f'First argument: {first}')
    print(f'Second argument: {second}')
    print(f'third argument: {third}')
    print(f'fourth argument: {fourth}')
    print(f'fifth argument: {fifth}')

test_args2(*args)
test_args2(**kwargs)
