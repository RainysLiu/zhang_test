import threading
import time
import os
from multiprocessing import Process

def sing(name, song_name):
    print("唱歌的进程id为%s，父id为%s" %(os.getpid(),os.getppid()))
    for x in range(6):
        print("%s在唱%s" % (name, song_name))
        time.sleep(1)
    print("唱歌线程结束")


def dance(name, dance_name):
    print("跳舞的进程id为%s，父id为%s" %(os.getpid(),os.getppid()))
    for x in range(6):
        print("%s在跳%s" % (name, dance_name))
        time.sleep(1)
    print("跳舞线程结束")


def main():
    name = "周杰伦"
    song_name = "青花瓷"
    dance_name = "青花瓷古典舞"
    # sing(name, song_name)
    # dance(name, dance_name)
    print("主进程的id为%s" % os.getpid())
    process_args = [[sing, song_name], [dance, dance_name]]
    # 创建子线程
    all_process = [Process(target=arg[0], args=(name, arg[1]))for arg in process_args]
    # 启动线程
    for p in all_process:
        p.start()
    # 主线程等待子线程结束后再执行
    for p in all_process:
        p.join()
    print("主进程结束")


if __name__ == '__main__':
    main()