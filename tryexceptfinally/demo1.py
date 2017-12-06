#coding=utf-8
import json
man   = []
other = []
try:
    data = open("sketch.txt")
    print type(data)
    # print data.
    for each_line in data:

        try:
            (role,line_spoken) = each_line.split(":",1)
            line_spoken = line_spoken.strip()
            if role == "张":
                man.append(line_spoken)
            elif role == "李":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print ("文件不存在！")
print json.dumps(man,encoding="UTF-8",ensure_ascii=False)
print type(man)
print other