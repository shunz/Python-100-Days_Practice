'''
使用列表

- 数值类型(int, float)是标量类型，无可访问的内部结构
- 字符串类型是一种结构化的、非标量类型，有一系列属性和方法
- 列表也是一种机构化的、非标量类型，它是值的有序序列，每个值可通过索引标识
- 将元素放在[]中定义列表，元素用,分隔
- 可用for循环对元素进行遍历，也可用[]或[:]运算符取出一个或多个元素

'''

list1 = [1, 3, 5, 7, 100]

# 乘号表示列表元素的重复
list2 = ['hello'] * 3

print(len(list1))

# 下标(索引)运算
print(list1[0])
print(list1[-1])
print(list1[-3])
list1[2] = 300
print(list1)

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)

# 通过enumerate函数处理列表后再遍历，可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(f'列表list1第{index + 1}个元素是：{elem}')


# 向列表添加元素
list1.append(200)
list1.insert(1, 400)

# 合并两个列表
list1.extend([1000,2000])


# 从列表移除元素
if 3 in list1:
    list1.remove(3)

# 从指定位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)

# 清空列表元素
list1.clear()

# 列表也可做切片操作，实现复制或取部分创建新列表
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
f2 = fruits[1:4]

# 通过完整切片复制列表
f3 = fruits[:]
f4 = f3[-3:-1]

# 通过反向切片获得倒置列表
f5 = f3[::-1]

# 对列表排序(默认按字母表排序)
list3 = ['orange', 'apple', 'zoo', 'internationalization', 'waxberry']
list4 = sorted(list3)
list5 = sorted(list3, reverse = True)

# 通过key关键字参数指定根据字符串长度进行排序
list6 = sorted(list3, key=len)

# 直接对列表进行排序
list3.sort(reverse=True)



'''
生成式和生成器
'''

# 使用列表的生成式语法创建
f1 = [x for x in range(1, 10)]
f2 = [x + y for x in 'ABCDE' for y in '1234567']
print(f1)
print(f2)

# 用这种语法创建后元素已经准备就绪，所以需要耗费较多的内存空间
f3 = [x ** 2 for x in range(1, 1000)]
import sys
print(sys.getsizeof(f3))
print(f3)

# 以下代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据，但他不占用额外的空间存储数据
# 每次需要数据的时候通过内部的运算得到数据(需要花费额外的时间)
f4 = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f4)) # 相比生成式，生成器不占用存储数据的空间
print(f4)
# for val in f4:
#    print(val)


# 另一种定义生成器的方式：
# 通过 yield 关键字将一个普通函数改造成生成器函数
# 例：实现一个生成斐波拉契数列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a 

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()





