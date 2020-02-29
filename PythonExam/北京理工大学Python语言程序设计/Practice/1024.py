# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

num = int(input())
# 确定个十百千各自位置上的0~9对应罗马字母
c = {
    'g': ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
    's': ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
    'b': ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
    'q': ('', 'M', 'MM', 'MMM')
}
roman = []
# 用整除和取余获得个十百千对应的数字
roman.append(c['q'][num // 1000])
roman.append(c['b'][(num // 100) % 10])
roman.append(c['s'][(num // 10) % 10])
roman.append(c['g'][num % 10])

print(''.join(roman))