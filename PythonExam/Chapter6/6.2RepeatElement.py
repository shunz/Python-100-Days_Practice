"""重复元素判定

接受列表作为参数，如果一个元素在列表中出现了不止一次，则返回True，但不要改变原来列表的值。
同时编写调用这个函数和测试结果的程序
"""

def isRepeated(ls):
    #if ls != list(set(ls)):  
    if len(ls) != len(set(ls)):  
        return True
    else:
        return False

ls1 = [1,2,3,1,2,3]
ls2 = [1,2,3,4,5,6]

print(isRepeated(ls1))
print(isRepeated(ls2))
