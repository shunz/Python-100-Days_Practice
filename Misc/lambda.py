"""匿名函数 Lambda 练习

- lambda的使用场景是用来写一些小体量的一次性函数，避免污染外层作用域，同时简化代码
- 所谓匿名，即不再使用 def 语句标准形式定义一个函数
- lambda的主体是一个表达式，而不是一个代码块，仅能在表达式中封装有限的逻辑
- lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数??
- lambda函数的语法只包含一个语句：
    - lambda [arg1 [,arg2,…… argN]] : expression
- lambda函数实际生成了一个lambda对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）
- lambda 是为了减少单行函数的定义而存在的。
- 但是值得注意的是，lambda的使用会在一定程度上降低代码的可读性，如果不是非常熟悉python的人或许会对此感到不可理解。
"""

sum1 = lambda arg1=0, arg2=0 : arg1 + arg2

print(sum1())
print(sum1(1,2))


sum2 = lambda *args : sum(args)
print(sum2(1,2,3,4,5))


g = [lambda a:a*2, lambda b:b*3]
print(g[0](5))
print(g[1](10))


dic = lambda **kwargs : kwargs
print(f'dic is: {dic(a=1, b=2, c=3)}')

dic_reverse = lambda **kwargs : {v: k for k, v in kwargs.items()}
print(f'reversed dic is: {dic_reverse(a=1, b=2, c=3)}')


split_kv = lambda **kwargs : f'Keys&Values pairs in dic: {[(k, v) for k, v in kwargs.items()]}\n\
Keys in dic: {[k for k in kwargs]}\n\
Values in dic: {[v for v in kwargs.values()]}'
print(split_kv(a=1, b=2, c=3))



# Lambda 表达式有何用处？如何使用？ —— 涛吴的问答
"""
https://www.zhihu.com/question/20125256/answer/14058285

简单来说，编程中提到的 lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，
也就是指匿名函数。这一用法跟所谓 λ 演算（题目说明里的维基链接）的关系，有点像原子弹和质能方程的关系，
差别其实还是挺大的。

不谈形式化的 λ 演算，只说有实际用途的匿名函数。先举一个普通的 Python 例子：将一个
list 里的每个元素都平方：

map( lambda x: x*x, [y for y in range(10)] )

这个写法要好过

def sq(x):
    return x * x

map(sq, [y for y in range(10)])

因为后者多定义了一个（污染环境的）函数，尤其如果这个函数只会使用一次的话。而且第一种写法实际上更易读，
因为那个映射到列表上的函数具体是要做什么，非常一目了然。如果你仔细观察自己的代码，会发现这种场景其实很
常见：你在某处就真的只需要一个能做一件事情的函数而已，连它叫什么名字都无关紧要。Lambda 表达式就可以用
来做这件事。进一步讲，匿名函数本质上就是一个函数，它所抽象出来的东西是一组运算。这是什么意思呢？类比

a = [1, 2, 3]和f = lambda x : x + 1

你会发现，等号右边的东西完全可以脱离等号左边的东西而存在，等号左边的名字只是右边之实体的标识符。如果你能
习惯 [1, 2, 3] 单独存在，那么 lambda x : x + 1 也能单独存在其实也就不难理解了，它的意义就是给「某
个数加一」这一运算本身。现在回头来看 map() 函数，它可以将一个函数映射到一个可枚举类型上面。沿用上面给出
的 a 和 f，可以写：

map(f, a)

也就是将函数 f 依次套用在 a 的每一个元素上面，获得结果 [2, 3, 4]。现在
用 lambda 表达式来替换 f，就变成：

map( lambda x : x + 1, [1, 2, 3] )

会不会觉得现在很一目了然了？尤其是类比

a = [1, 2, 3]
r = []
for each in a:
    r.append(each+1)

这样的写法时，你会发现自己如果能将「遍历列表，给遇到的每个元素都做某种运算」的过程从一个循环里抽象出来成为
一个函数 map，然后用 lambda 表达式将这种运算作为参数传给 map 的话，考虑事情的思维层级会高出一些来，需
要顾及的细节也少了一点。Python 之中，类似能用到 lambda 表达式的「高级」函数还有 reduce、filter 等等，
很多语言也都有这样的工具（不过这些特性最好不要在 Python 中用太多，原因详见
http://www.zhihu.com/question/19794855/answer/12987428 的评论部分）。这种能够接受一个函数作为
参数的函数叫做「高阶函数」（higher-order function），是来自函数式编程（functional programming）
的思想。

和其他很多语言相比，Python 的 lambda 限制多多，最严重的当属它只能由一条表达式组成。这个限制主要是为了防
止滥用，因为当人们发觉 lambda 很方便，就比较容易滥用，可是用多了会让程序看起来不那么清晰，毕竟每个人对于
抽象层级的忍耐 / 理解程度都有所不同。
"""



# 什么时候使用Lambda函数？
"""
https://foofish.net/lambda.html

Python 中定义函数有两种方法，一种是用常规方式 def 定义，函数要指定名字，第二种是用 lambda 定义，不需要指定名字，
称为 Lambda 函数。

Lambda 函数又称匿名函数，匿名函数就是没有名字的函数，函数没有名字也行？当然可以啦。有些函数如果只是临时一用，而且它
的业务逻辑也很简单时，就没必要非给它取个名字不可。

好比电影里面的群众演员，往往他们的戏份很少，最多是衬托主演，跑跑龙套，他们需要名字吗？不需要，因为他们仅仅只是临时出镜，
下次可能就用不着了，所以犯不着费心思给他们每个人编个号取个名字，毕竟取个优雅的名字是很费劲的事情。

先来看个简单 lambda 函数

>>> lambda x, y : x+y
<function <lambda> at 0x102bc1c80>
x 和 y 是函数的两个参数，冒号后面的表达式是函数的返回值，你能一眼看出这个函数就是是在求两个变量的和，但作为一个函数，
没有名字如何使用呢？这里我们暂且给这个匿名函数绑定一个名字，这样使得我们调用匿名函数成为可能

>>> add = lambda x, y : x+y
>>> add
<function <lambda> at 0x102bc2140>
>>> add(1,2)
3
它等同于常规函数

>>> def add2(x, y):
...     return x+y
...
>>> add2
<function add2 at 0x102bc1c80>
>>> add2(1,2)
3
如果定义匿名函数，还要给它绑定一个名字的话，有点画蛇添足，通常是直接使用 lambda 函数。那么 lamdba 函数的正确使用场景在哪呢？

1、函数式编程

尽管 Python 算不上是一门纯函数式编程语言，但它本身提供了很多函数式编程的特性，像 map、reduce、filter、sorted
这些函数都支持函数作为参数，lambda 函数就可以应用在函数式编程中。

请看题：一个整数列表，要求按照列表中元素的绝对值大小升序排列，你会怎么做？思考一分钟往下看

>>> list1 = [3,5,-4,-1,0,-2,-6]
>>> sorted(list1, key=lambda x: abs(x))
[0, -1, -2, 3, -4, 5, -6]
排序函数 sorted 支持接收一个函数作为参数，该参数作为 sorted 的排序依据，这里按照列表元素的绝对值进行排序，当然，
我也可以用普通函数来实现：

>>> def foo(x):
...     return abs(x)
...
>>> sorted(list1, key=foo)
[0, -1, -2, 3, -4, 5, -6]
只不过是这种方式代码看起来不够 Pythonic 而已。

2、闭包

闭包本身是一个晦涩难懂的概念，它可以专门单独用一篇文章来介绍，不过在这里我们可以简单粗暴地理解为闭包就是一个定义在函数
内部的函数，闭包使得变量即使脱离了该函数的作用域范围也依然能被访问到。

来看一个用 lambda 函数作为闭包的例子。

>>> def my_add(n):
...     return lambda x:x+n
...
>>> add_3 = my_add(3)
>>> add_3(7)
10
这里的 lambda 函数就是一个闭包，在全局作用域范围中，add_3(7) 可以正常执行且返回值为10，之所以返回10是因为在
my_add 局部作用域中，变量 n 的值在闭包的作用使得它在全局作用域也可以被访问到。

换成常规函数也可以实现闭包，只不过是这种方式稍显啰嗦。

>>> def my_add(n):
...     def wrapper(x):
...         return x+n
...     return wrapper
...
>>> add_5 = my_add(5)
>>> add_5(2)
7
那么是不是任何情况 lambda 函数都要比常规函数更清晰明了呢？看这个例子：

f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
这是一个返回某个集合的所有子集的 lambda 函数，你看明白了吗？我是很难一眼看出来

zen of python 中有这样一句话是 Explicit is better than implicit(明了胜于晦涩)。记住，如果用 lambda 函数不
能使你的代码变得更清晰时，这时你就要考虑使用常规的方式来定义函数。
"""


# 《python中的lambda函数用法》
"""
https://zhuanlan.zhihu.com/p/58579207

由于lambda语法是固定的，其本质上只有一种用法，那就是定义一个lambda函数。在实际中，根据这个lambda函数应用场景的不同，
可以将lambda函数的用法扩展为以下几种：

1.将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加
法功能的函数。例如，执行add(1,2)，输出为3。

2.将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：time.sleep=lambda x:None。这样，
在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。

3.将lambda函数作为参数传递给其他函数。
函数的返回值也可以是函数。例如return lambda x, y: x+y返回一个加法函数。这时，lambda函数实际上是定义在某个函数内部的函
数，称之为嵌套函数，或者内部函数。对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量，这个特性是
闭包(Closure)编程的基础，在这里我们不展开。


部分Python内置函数接受函数作为参数,典型的此类内置函数有这些:

- filter函数 此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表
[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。

- sorted函数 此时lambda函数用于指定对列表中所有元素进行排序的准则。例如
sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距
离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

- map函数 此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的
元素分别加1，其结果[2, 3, 4]。

- reduce函数 此时lambda函数用于指定列表中两两相邻元素的结合条件。例如
reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表
[1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，
其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。

- 另外，部分Python库函数也接收函数作为参数，例如gevent的spawn函数。此时，lambda函数也能够作为参数传入。
"""
