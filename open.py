#coding=utf-8
import os
from nt import lstat
from __builtin__ import str
#变量保存到文件
filename = r"D:\python\readandread\2017.7.3.txt"
#读取文件并判断是否存在
if os.path.exists(filename):#判断文件是否纯在
    fd = open(filename,"w")
    fd.close()
else:
    print u"文件存在"    
    
#pickle使用------------将列表转换成字符串----对象更复杂
#1.写入文件
import pickle
lst = [1,2,3,["a","b"]]
lst ={"a":"b","c":"d"}
print lst
result = pickle.dumps(lst)
open(filename,"w").write(result)
#同一个文件不能有写又读
#2.读取文件
content = open(filename).read()
lst = pickle.loads(content)
print lst,type(lst)

#json的使用 --列表字典元祖
import json
print "json》》》》》》》》》》》》》"
lst = [1,2,3,["a","b"]]
print lst
result = json.dumps(lst)
open(filename,"w").write(result)
#同一个文件不能有写又读
#2.读取文件
content = open(filename).read()
lst = json.loads(content)
print lst,type(lst)

#3. str()\\eval()
print type(lst)
newlst = str(lst)
print type(newlst)
lst1 = eval(newlst)
print lst1,type(lst1)







