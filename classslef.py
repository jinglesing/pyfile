#encoding=utf-8
'''



'''
class mywife():
    def __init__(self,age):
        self.age = age
        self.sex = 'female'
        self.high ='165'
        self.money = '1000000'
        self.edu = "本科"
    def singing(self):
        return "后来"
    def work(self):
        return "扫地"
    def program(self):
        return "coding"
    def __str__(self):
        return "%s,%s,%s,%s,%s" % (self.age,self.sex,self.high,self.money,self.edu)
    
meinv = mywife(22)
print type(mywife)
print type(meinv)
print meinv
print meinv.singing()

    
        
    