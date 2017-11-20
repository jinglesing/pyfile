class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print "calling normal_method({0},{1})".format(args,kwargs)
    @classmethod
    def class_method(*args,**kwargs):
        print "calling class_method({0},{1})".format(args,kwargs)
    @staticmethod
    def static_method(*args,**kwargs):
        print "calling static_method({0},{1})".format(args,kwargs)
    @property
    def some_property(self,*args,**kwargs):
        print "calling some_property getter({0},{1},{2})".format(self,args,kwargs)
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print "calling some_property setter({0},{1},{2})".format(self,args,kwargs)
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print "calling some_other_property getter({0},{1},{2})".format(self,args,kwargs)
        return self._some_other_property

o = MyClass()
o.normal_method
# <bound method MyClass.normal_method of <__main__.MyClass instance at 0x7fdd2537ea28>>

o.normal_method()
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>,),{})

o.normal_method(1,2,x=3,y=4)
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>, 1, 2),{'y': 4, 'x': 3})



o.class_method
# <bound method classobj.class_method of <class __main__.MyClass at 0x7fdd2536a390>>

o.class_method()
# class_method((<class __main__.MyClass at 0x7fdd2536a390>,),{})

o.class_method(1,2,x=3,y=4)
# class_method((<class __main__.MyClass at 0x7fdd2536a390>, 1, 2),{'y': 4, 'x': 3})



o.static_method
# <function static_method at 0x7fdd25375848>

o.static_method()
# static_method((),{})

o.static_method(1,2,x=3,y=4)
# static_method((1, 2),{'y': 4, 'x': 3})
