
import threading

# 线程安全
from copy import deepcopy, copy

count = 10
# 创建线程锁
lock = threading.Lock()

def demo(num):
    global count
    for x in range(100000):
        # 操作变量之前进行加锁
        lock.acquire()
        count += num
        count -= num
        # 操作变量之后进行解锁
        lock.release()
    print("%s线程结束后的值为%s" %(threading.current_thread().name, count))


def main():
    t1 = threading.Thread(target=demo, args=(4,))
    t2 = threading.Thread(target=demo, args=(5,))
    t3 = threading.Thread(target=demo, args=(5,))
    t4 = threading.Thread(target=demo, args=(5,))
    t5 = threading.Thread(target=demo, args=(5,))
    t6 = threading.Thread(target=demo, args=(5,))
    t7 = threading.Thread(target=demo, args=(5,))
    t8 = threading.Thread(target=demo, args=(5,))
    t9 = threading.Thread(target=demo, args=(5,))
    t10 = threading.Thread(target=demo, args=(5,))
    threadings =[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    # 启动线程
    for t in threadings:
        t.start()
    for t in threadings:
        t.join()
    print("线程结束")

if __name__ == '__main__':
    main()

    a = 1
    # b = a
    # print(id(a), id(b))
    # b = 10
    # print(a, b)
    # print(id(a), id(b))
    #
    # a = [[1]]
    # b = deepcopy(a)
    # # b = copy(a)
    # print(id(a), id(b))
    # b[0].append(10)
    # print(a, b)
    # print(id(a), id(b))

    # a_list = []
    #
    # b_list = a_list

