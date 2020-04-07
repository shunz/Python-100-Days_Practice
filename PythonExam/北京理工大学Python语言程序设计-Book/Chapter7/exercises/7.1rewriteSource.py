"""Python源文件改写

编写程序，读取一个Python源程序文件，将文件中所有除保留字外的小写字母换成大写字母，生成后的文件
要能够被Python解释器正确执行
"""

import keyword

stopwords = '\t\n\r:()'
functionwords = '.('
word = []
output = ''
lastAvailable = ['from', 'import']
last = False

def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    return string

def parse(string):
    global word
    global output
    global last
    for i in string:
        if i in stopwords:
            wd = ''.join(word)
            res = isKeyWord(wd)
            if res == False:
                if i not in functionwords and last == False:
                    wd = wd.upper()
            if wd in lastAvailable:
                last = True
            else:
                last = False
            output += wd
            output += i
            word = []
        else:
            word.append(i)

def isKeyWord(string):
    if string in keyword.kwlist:
        return True
    return False

def outPutFile():
    file = open('7.1test_out.py', 'w', encoding='utf-8')
    file.write(output)

string = readFile('7.1test.py')
parse(string)
outPutFile()
