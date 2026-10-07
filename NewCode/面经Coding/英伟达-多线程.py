"""
N 线程顺序循环打印：信号量数组，每个线程对应一个信号量。初始只放开线程 0。
线程打印完成，释放下一个线程信号量`(tid+1)%N`；计数器用原子变量保证线程安全。
到达上限唤醒全部信号量退出，避免死锁。
"""

import threading

class TurnPrint:
    def __init__(self, n_thread: int, max_print: int):
        # n_thread：线程总数；max_print：最多打印到这个数字
        self.n = n_thread
        self.max_num = max_print

        # Condition = 内置互斥锁 + 等待队列，用于线程间等待/唤醒
        self.cond = threading.Condition()

        # 共享变量 turn：标记当前轮到哪个线程打印
        # 所有共享变量读写都必须在cond锁保护下，防止竞态条件
        self.turn = 0
        # cur_num：下一个要打印的数字
        self.cur_num = 1

    def worker(self, tid: int):
        """
        tid: 当前线程编号
        每个线程循环执行：等待轮到自己 -> 打印 -> 更新轮次 -> 唤醒其他线程
        """
        while True:
            # with cond：自动获取内部锁；代码块结束自动释放锁（异常也会释放）
            with self.cond:
                # ====================== 重点 ======================
                # while 判断，不能用 if！为了防止【虚假唤醒】
                # 虚假唤醒：线程被唤醒，但条件依然不满足
                # 条件：当前不是本线程，且还没打印完，则继续wait阻塞
                # wait()行为：释放锁，线程进入等待队列；被唤醒后重新抢锁，抢到锁才返回
                while self.turn != tid and self.cur_num <= self.max_num:
                    self.cond.wait()

                # 退出条件：数字已经打印完毕
                if self.cur_num > self.max_num:
                    # 唤醒所有等待线程，让它们检测退出条件，防止死锁
                    self.cond.notify_all()
                    return

                # 轮到当前线程执行打印
                print(f"Thread {tid} prints {self.cur_num}")
                self.cur_num += 1

                # 更新轮次：切换到下一个线程，模n实现循环
                self.turn = (self.turn + 1) % self.n

                # notify_all：唤醒所有在这个cond上wait的线程
                # 唤醒后所有线程争抢锁，抢到锁后再次进入while判断条件
                # 缺点：惊群效应；优点：代码简单安全，面试首选
                self.cond.notify_all()


if __name__ == "__main__":
    N = 3       # 3个线程
    MAX = 6     # 打印数字1~6
    tp = TurnPrint(N, MAX)
    threads = []

    # 创建并启动所有线程
    for i in range(N):
        t = threading.Thread(target=tp.worker, args=(i,))
        threads.append(t)
        t.start()

    # join：主线程阻塞，等待所有子线程全部执行完成
    for t in threads:
        t.join()
