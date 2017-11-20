#coding:utf-8
import os
import mock

"""
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
# class directory_content():
#
#     def print_directory_content(self,spath):
#         for sChild in os.listdir(spath):
#             sChildPath = os.path.join(spath, sChild)
#             if os.path.isdir(sChildPath):
#                 self.print_directory_content(sChildPath)
#             else:
#                 print sChildPath
#
# directory_content().print_directory_content(u"D:\程序员软件\pythoncode")


# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print l
#
# f(2)
# f(3,[3,2,1])
# f(3)
# f(4)
# f(3)
# f(3,[3,2,1])
#
# num = lambda x,y:x+y
# print num(1,2)

#最大公约数
import sys

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
print gcd(5,6)