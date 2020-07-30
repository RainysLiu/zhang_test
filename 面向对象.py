
class AA:
    __slots__ = ('user', '__password', 'ip')

    def __init__(self):
        self.__password = "123456"
        self.user = "zhang"

    @property
    def passwd(self):
        return self.__password

    @passwd.setter
    def passwd(self, value):
        self.__password = value

    def set_ip(self):
        self.ip = '1231445'

    def get_info(self):

        print(self.user, self.passwd, self.ip)


aa = AA()
print(aa.user)
aa.user = 'liu'
print(aa.user)

# print(aa.passwd)
aa.passwd = '456789'
print(aa.passwd)

# aa.ip = '10.45.33.456'
# print(aa.ip)

aa.set_ip()
aa.get_info()


with open('git_test.py', 'r',encoding='utf8') as file:
    res = file.read()
    print(res)

f = open('git_test.py', 'r', encoding='utf8')
res = f.read()
print(res)
f.close()

class Test:
    def test(self):
        pass
def test():
    pass
print(test)
print(type(Test().test))