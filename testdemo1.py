# coding: utf-8

# a1=[('b',5),('a',1),('c',3),('d',4)]
# 降序排列 reverse=True
# b1=sorted(a1,reverse=True)
# print(b1)
#
# test = 'pythonp'
# a = test.strip('p')
# print(a[::-1])
#
# m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict = {k:v for v,k in m.items()}
# print(dict)
#
# x=[1,3,2,1]
# x.index(1)
# print(x.index(1))

# x=['abc','abd','xmn','lio','qqa','skt','rng','xqg']
# for i in x:
#     if i.count('a')>0:
#         print(i)
#
# a=[i for i in x if i.count('b')>0]
# print(a)
#
# n=[]
# for t in x:
#     if t.startswith('x'):
#         n.append(t)
#         print(n)
# #
# c=[i for i in x if i[0]=='l']
# print(c)

def fac(n):
    if n ==1:
        return 1
    else:
       return n*fac(n-1)

if __name__ == '__main__':
    print(fac(5))

# from functools import reduce
# num = reduce(lambda x,y : x+y ,range(1,101))
# print(num)
#
# import re
# p = re.compile('blue|white|red')
# print(p.sub('colour','white kin')) #colour kin
# print(p.sub('colour','blue socks and red shoes and white kin'))
#
x=[]
for i in range(10):
    x.append(i)
print(x)
print(range(4))


