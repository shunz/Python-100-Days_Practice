# 函数递归的调用过程
# 递归本身是一个函数，需要函数定义方式描述
# 函数内部，采用分支语句对输入参数进行判断
# 基例和链条，分别编写对应代码

def fact(n):
    if n == 0: # 基例
        return 1
    else: # 链条
        return n * fact(n-1)

print(fact(10))