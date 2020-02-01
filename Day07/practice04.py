'''
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值
'''

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2



while True:
    ls_str = input('请输入一个数字列表(以,分隔)：').split(',')
    print(ls_str)
    print(max2(ls_str))
    print('直接使用内置的max和min函数找出列表中最大和最小元素')
    print(f'最大元素：{max(ls_str)}')
    print(f'最小元素：{min(ls_str)}')
    
    # 字符串列表转数字列表 way1
    ls_int = []
    for n in ls_str:
        ls_int.append(int(n))
    print(ls_int)
    print(max2(ls_int))
    
    # 字符串列表转数字列表 way2
    ls_int2 = [int(x) for x in ls_str]
    print(ls_int2)

    # 字符串列表转数字列表 way3
    ls_int3 = list(map(int, ls_str))
    print(ls_int3)

    # 字符串列表转数字列表 way4
    ls_int4 = []
    for i, v in enumerate(ls_str):
        ls_int4.append(int(v))
    print(ls_int4)

    # 字符串列表转数字列表 way5
    ls_int5 = ls_str[:]
    for i, v in enumerate(ls_int5):
        ls_int5[i] = int(v)
    print(ls_int5)
