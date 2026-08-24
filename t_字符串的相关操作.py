import s_Hub as s
#编码：本质上就是数字与语言文字的对照表
'''常见编码方式：
ascii：【在算法中应用广泛】
    美国标准信息交换码，用一个字节表示一个字符，最多表示128个字符，后扩展至 256 种
gb2312：中国国家标准信息交换码，用两个字节表示一个字符，最多表示 65536 个字符
gbk：汉字内码扩展规范，对gb2312的扩展，用两个字节表示一个字符，最多表示 65536 个字符
Unicode：【字符之间转换更快】【占用空间大】【万国码】
    用两个字节或四个字节表示一个字符，最多可以表示 10^6 个字符
utf-8：【节省空间】【字符之间转换速度较慢，慢于Unicode】
    属于可变长编码，是对Unicode编码的压缩和优化，用1-3 bytes表示一个字符
''' 

#字符串的编码与解码
# encode() 编码 将其他字符串转换为 unicode编码
# decode() 解码 将 unicode编码转换为其他的编码形式

# exmample：
str1="hello"
print(str1,type(str1)) #以字符形式进行处理的
str1_encode=str1.encode()
print(str1_encode,type(str1_encode)) # >>> b'hello' bytes类型
# tips：<encode()将字符串编码转化为字节类型，在python里字节类型以b'…'的形式显示，
# 所以是b‘hello‘>
str1_encode_decode=str1_encode.decode()
print(str1_encode_decode,type(str1_encode_decode)) # >>> hello str类型

# 总结：对于 bytes 类型，说明它是经过编码的，对于 str 类型，说明它是经过解码的。
# 格式：
# encode(编码格式,错误处理方式)
# decode(编码格式,错误处理方式
s.printLine()

# 字符串的相关操作
'''
+ 字符串的拼接
* 重复输出字符串
[] 通过索引获取字符串中单个字符
[:] 截取字符串中的一部分，默认第一个字符索引为0，最后一个字符索引为-1，
    切片时最后一个索引不取
in 成员运算符，如果字符串中包含给定的字符返回 True
not in 成员运算符，如果字符串中不包含给定的字符返回 True
r/R 原始字符串，所有的字符串都是直接按照字面的意思来使用，
    没有转义特殊或不能打印的字符
'''

# 字符串的切片
# 格式 变量名[起始位置:结束位置:步长]
'''所有字符串切片都遵循包前不包后原则'''
str2="123456789"
print(str2[-1:-5]) # >>> ''  # 注意：步长默认1，为正数时从左往右
print(str2[-1:-5:-1]) # >>> '987' # 步长为负数时从右往左，
#                       且切片时最后一个索引不取
# 关于步长：可以理解为 n 个字符为一组，取第一个发现的字符，在轮换下一组

# 字符串的格式化
# 略 详见本地文件：“字符串格式化.py“

# 字符串的查找
'''
find : 检测某一个子字是否包含在字符串中 true：返回这个子字符串开始下标 false：-1
        find([子字符串]，<开始下标>，<结束下标>)
index : 检测某一个子字是否包含在字符串中 true：返回这个子字符串开始下标 false：抛出异常
        index([子字符串]，<开始下标>，<结束下标>)
'''
del str1,str2,str1_encode,str1_encode_decode
name="WuBinbin"
print(name,f"result:{name.find("i")}") # >>> 3
print(name,f"result:{name.index('in')}") # >>> 3
#若找到，则返回第一个找到的子字符串开始下标
print(name,f"result:{name.find('in',5)}") # >>> 6
#通过设置切片可以限制查找范围
print(name,f"result:{name.find('in',5,6)}") # >>> -1
#若未找到，则返回-1 结束查找
try:
    print(name,f"result:{name.index('in',5,6)}") # >>> ValueError:substring not found
except ValueError as v:
    print("ValueError:%s" % v)


s.printLine()
# 字符串的子字符计数
'''
count zn.计数 : 返回某个字符在字符串中出现的次数，否则返回 0
count([子字符串]，<开始下标>，<结束下标>)
'''
# name="WuBinbin"
print(name,f"result:{name.count('i')}") # >>> 2
print(name,f"result:{name.count('a')}") # >>> 0


s.printLine()