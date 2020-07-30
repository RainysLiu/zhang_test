import threading
import time
import os
from beautful_soup3 import test_return_value

@test_return_value
def sing(name, song_name):
    print("唱歌的进程id为%s" % os.getpid())
    for x in range(6):
        print("%s在唱%s"%(name,song_name))
        time.sleep(1)
    print("唱歌线程结束")

@test_return_value
def dance(name, dance_name):
    print("唱歌的进程id为%s" % os.getpid())
    for x in range(6):
        print("%s在跳%s" % (name, dance_name))
        time.sleep(1)
    print("跳舞线程结束")

@test_return_value
def main():
    name = "周杰伦"
    song_name = "青花瓷"
    dance_name = "青花瓷古典舞"
    print("主进程的id为%s"%os.getpid())
    # process_args = [[sing, song_name],[dance, dance_name]]
    # # 创建子线程
    # # for arg in process_args:
    # #     print("1111",arg[0])
    # #     print("2222",arg[1])
    # all_threadings = [threading.Thread(target=arg[0],args=(name,arg[1])) for arg in process_args]
    all_threadings = []
    all_threadings.append(threading.Thread(target=sing, args=(name, song_name)))
    all_threadings.append(threading.Thread(target=dance, args=(name, dance_name)))
    # 启动线程
    for t in all_threadings:
        t.start()
    # 主线程等待子线程结束后再执行
    for t in all_threadings:
        t.join()
    print("主进程结束")

if __name__ == '__main__':
    # dance('zhang', '菊花台')
    main()
