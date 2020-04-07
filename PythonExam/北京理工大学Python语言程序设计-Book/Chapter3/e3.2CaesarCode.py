def encode(plaincode):
    # plaincode = input('请输入明文：')
    cipher = ''
    for c in plaincode:
        if ord('a') <= ord(c) <= ord('z'):
            # print(chr(ord('a')+(ord(c)-ord('a')+3)%26), end='')
            cipher += chr(ord('a')+(ord(c)-ord('a')+3)%26)
        elif ord('A') <= ord(c) <= ord('Z'):
            # print(chr(ord('A')+(ord(c)-ord('A')+13)%26), end='')
            cipher += chr(ord('A')+(ord(c)-ord('A')+13)%26)
        else:
            # print(c, end='')
            cipher += c
    return cipher


def decode(cipher):
    plaincode = ''
    for c in cipher:
        if ord('a') <= ord(c) <= ord('z'):
            # print(chr(ord('a')+(ord(c)-ord('a')-3)%26), end='')
            plaincode += chr(ord('a')+(ord(c)-ord('a')-3)%26)
        elif ord('A') <= ord(c) <= ord('Z'):
            # print(chr(ord('A')+(ord(c)-ord('A')-13)%26), end='')
            plaincode += chr(ord('A')+(ord(c)-ord('A')-13)%26)
        else:
            # print(c, end='')
            plaincode += c
    return plaincode


