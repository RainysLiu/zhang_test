# encoding = utf-8

class A(object):
    def func(self):
        print('A')
class B(A):
    def func(self):
        super().func()
        print('B')
class C(A):
    def func(self):
        super().func()
        print('C')
class D(B,C):
    def func(self):
        super().func()
        # super(D,self).func()
        print('D')

D().func()




