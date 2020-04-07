"""用递归反转字符串"""

def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]

print('\n' + reverse('三皇五帝夏商周，春秋战国秦两汉，三国两晋南北朝，隋唐五代和十国，辽宋夏金元明清'))
