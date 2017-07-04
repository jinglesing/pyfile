#coding=utf-8
import os
#变量保存到文件
filename = r"D:\python\readandread\2017.7.3.txt"
#读取文件并判断是否存在
if os.path.exists(filename):#判断文件是否纯在
    fd = open(filename,"w")
    fd.close()
else:
    print u"文件存在"    
    
#pickle使用------------将（数据格式）字符串--对象更复杂
#1.写入文件
import pickle
lst = [1,2,3,["a","b"]]
lst ={"a":"b","c":"d"}
print lst
result = pickle.dumps(lst)
open(filename,"w").write(result)
#同一个文件不能有写又读


#2.读取文件 tell seek
content = open(filename).read()
fd = open(filename)
print fd.tell(),"start"
content = fd.read()
print fd.tell(),"end"
fd.seek(0)
print fd.tell(),"after seek"
lst = pickle.loads(content)
print lst,type(lst)



#json的使用 --列表字典元祖


# import json
# print "json》》》》》》》》》》》》》"
# lst = [1,2,3,["a","b"]]
# print lst
# result = json.dumps(lst)
# open(filename,"w").write(result)
#同一个文件不能有写又读
#2.读取文件
# content = open(filename).read()#fp.read(size)
# lst = json.loads(content)
# print lst,type(lst)

#3. str()\\eval()--将字符串转为列表或者字典
print type(lst)
newlst = str(lst)
print type(newlst)
lst1 = eval(newlst)
print lst1,type(lst1)


#文件open\flie\readlines\close
#r:读取、w：写入、a:追加 +:读写 b:二进制
# read(size)\readline(size)\fp.write()/fp.writelines(seq)/fp.close()
# fp.flush()把缓冲区的内容写入硬盘

#3.文件读写a 和   w rb r(二进制会丢失)rb+，wb+
# open(filename,"a").write("12345333333333")
# content2 = open(filename."rb").read()
# print repr(content2)
#w+有什么用？写完可以读

# fd= open(filename,"w+")
# fd.write("aaaaaaaaaaaaaaa")
# fd.seek(0)
# print fd.read()
# fd.close()

#绝对路径、相对路劲
import os
print os.getcwd()#得到工作路径，变化的值1.自己中途改变2、被父程序改变----------》不可靠的、不安全的
filename = os.path.join(os.getcwd(),"2017.7.3.txt")
print filename
filename = "2017.7.3.txt"
print os.path.exists(filename)#工作路径和文件不在一个目录
os.chdir(r"D:\python")
print os.path.exists(filename)

#解决办法--解决绝对路径、运行目录容易改变的问题，所以不能用相对路径
import sys
filename =os.path.join(sys.path[0],'2017.7.3.txt')#sys.path当前文件所在路径----------------》可靠的
print filename
print os.path.exists(filename)
#函数








