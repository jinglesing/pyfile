#coding:utf-8
'''
将一句话的单词进行倒置，标点不倒置。比如 I like beijing. 经过函数后变为：beijing. like I 
'''


# def fun(str):
#     L = string.split()#把字符串转化成一个单词的列表
#     L.reverse()#列表倒置
#     s = " ".join(L)#把列表转换为字符串输出
#     return s
#
# if __name__ == "__main__":
#     string = raw_input()
#     print fun(string)


# while True:
#     try:
#         test = input().split()
#         print(" ".join(test[::-1]))
#     except:
#         break
    


# 2.输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”


    


# input_1 =raw_input("please input first string\n")
# print '\n'
# input_2 = raw_input("please input second string\n")
# print '\n'
# input_2 = set(input_2)
# for en_char in input_2:
#     input_1 = input_1.replace(en_char,"")
# print input_1

# 输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来



# 大富翁游戏，玩家根据骰子的点数决定走的步数，即骰子点数为1时可以走一步，
# 点数为2时可以走两步，点数为n时可以走n步。求玩家走到第n步（n<=骰子最大点数且是方法的唯一入参）时，总共有多少种投骰子的方法
if __name__ == '__main__':
    dp = [0]*(6+1)
    print dp
    dp[1] = 1

    for i in range(2, 6+1):
        dp[i] = sum(dp[:i]) + 1
    while 1:
        try:
            n = int(raw_input())
        except:
            break
    print dp[n]

    # 给你六种面额
    # 1、5、10、20、50、100
    # 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0
    # ~10000
    # 的非负整数）的不同组合的个数。
    链接：https: // www.nowcoder.com / questionTerminal / 178
    b912722ac42a2865057a66d4e7de2
    来源：牛客网

    N = input('')
    N = int(N)
    penny = [1, 5, 10, 20, 50, 100]
    matrix = [[0 for i in range(6)] for j in range(N + 1)]
    matrix[0] = [1, 1, 1, 1, 1, 1]
    for i in range(N + 1):
            matrix[i][0] = 1
        for j in range(1, 6):
                if i - penny[j] > 0:
                        matrix[i][j] = sum(matrix[i - penny[j]][0:j + 1])
            if (i - penny[j]) == 0:
                    matrix[i][j] = 1
                 
    print(sum(matrix[i][:]))