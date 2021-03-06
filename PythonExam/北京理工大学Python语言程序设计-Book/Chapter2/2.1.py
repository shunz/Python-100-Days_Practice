"""2.1 基本的温度转换程序

- 要点：这是一个程序设计教学中的经典案例，用于理解基本的Python语法元素
1. 分析问题
    - 角度1：由用户输入温度值，利用程序进行温度转换
    - 角度2：通过语音识别、图像识别自动监听获得温度信息发布渠道（电视、收音机）等给出的温度播报源数据，再由程序转换输出给用户，无需用户输入
    - 角度3：由程序定期从温度信息发布网站获得温度值，再转换成用户熟悉的方式
    - 上述3种角度对问题计算部分的不同理解会产生不同的IPO描述、算法和程序
    - 「利用计算机解决问题」需要结合计算机技术的发展水平和人类对问题的思考成都，在特定技术和社会条件下，分析出一个问题最经济、最合理的计算部分，进而用程序实现
2. 划分边界
    - 在上一步「确定问题计算部分」的基础上，选择第一种理解角度，然后进一步明确问题的输入数据、输出数据和对数据处理的要求
    - Input：带华氏或摄氏标志的温度值（例如：82F、28C）
    - Process：根据温度标志选择适当的温度转换算法
    - Output：带摄氏或华氏标志的温度值
3. 设计算法
    - 转换算法
        - C = （F - 32) / 1.8
        - F = C * 1.8 + 32
    - 扩展：算法（Algorithm）
        - 算法是数学和计算领域的概念，指完成特定计算的一组有序操作
        - IPO中的Process也称为算法
        - 算法的理解有广义和狭义之分
4. 编写程序
    - 根据IPO描述和算法设计，编写温度转换的程序代码（略）
5. 调试测试
    - 使用IDLE等工具调试，测试是否能正确运行或运行逻辑没有错误
6. 升级维护
    - 随着问题使用场景、输入和输出要求因素的变化，不断的维护和升级程序
    - 与人一样，任何程序都有生命周期。促使程序生命结束的事件有很多，例如：平台更换、使用方式变化、算法改进等
"""

def temptrans():
    temp = input('请输入带有符号的温度值(比如82F/C)：')
    if temp[-1] in ['f', 'F']:
        c = (eval(temp[0:-1]) - 32) / 1.8
        print(f'转换后的温度是{c:.2f}°C')
    elif temp[-1] in ['c', 'C']:
        f = 1.8 * eval(temp[0:-1]) + 32
        print(f'转换后的温度是{f:.2f}°F')
    else:
        print('输入格式错误')
        temptrans()

temptrans()
