"""文本字符分析

编写程序接收字符串，按字符出现频率的降序打印字母。
分别尝试录入一些中英文文章片段，比较不同语言之间字符频率的差别

- 输入
    - 输入字符串
- 处理
    - 将字符串分解为逐个字符(字母、汉字)
    - 统计每个字符的出现频率
    - 按降序排列
— 输出
    - 按降序打印字符出现次数
"""

def main():
    s = input('请输入一串字符(直接按回车结束输入)：')
    analyze(s)

def analyze(str):
    d = {}
    for i in str:
        if ord(i) < 97 and i.encode('utf-8').isalpha():  # 如果是大写英文字符
            i = chr(ord(i) + 32)  # 转为小写英文
        d[i] = d.get(i, 0) + 1

    for k, v in sorted(list(d.items()), key=lambda x: x[1], reverse=True):
        print(f'{k:<3}{v:>4}')
        
main()


