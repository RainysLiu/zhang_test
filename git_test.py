# 士兵突击

class Gun(object):
    def __init__(self, modle):
        # 枪的型号
        self.modle = modle
        # 子弹数量
        self.bullte_count = 0

    def add_bullte(self, count):
        self.bullte_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullte_count < 0:
            print("%s没有子弹了"%self.modle)
        # 发射
        else:
            self.bullte_count -= 1
            print("【%s】突突突...发射成功，还剩 %d 颗子弹" %(self.modle,self.bullte_count))

class Soldier(object):
    def __init__(self, name):
        self.name = name
        # 新兵没有枪
        self.gun = None

    def fire(self):
        if self.gun == None:
            print("士兵 %s 还没有枪" %self.name)
            return
        print("士兵【%s】喊口号:冲啊..." %self.name)
        self.gun.add_bullte(10)
        self.gun.shoot()


gun = Gun("98k")
gun.add_bullte(10)
gun.shoot()

liuang = Soldier("刘昂")
# print(liuang.gun)
liuang.gun = gun
# print(liuang.gun)
liuang.fire()