# 进程池的使用

import os,time
from multiprocessing import Pool


def demo(name):
    print("当前进程的id是%s,任务名是%s"%(os.getpid(),name))
    time.sleep(1)
    return name


def main():
    pool = Pool(4)
    name_list = ["吃饭","睡觉","打豆豆"]
    # for name in name_list:
        # 给进程池添加任务
        # 并行（异步）
        # pool.apply_async(demo, args=(name,))
        # 串行（同步）
        # pool.apply(demo,args=(name,))
    result = pool.map(demo, name_list)
    pool.close()
    pool.join()
    print("进程结束")
    print(result)


if __name__ == '__main__':
    main()