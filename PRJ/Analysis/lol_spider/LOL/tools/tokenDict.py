import threading
import time
import random


# map(str:token, [int:times, long:time])
class tokenItem:
    def __init__(self, token):
        self.time = 0
        self.token = token
        self.times = 0

        self.totalTimes = 0
    def __str__(self):
        return "Token Status : {},{}".format(self.token, self.totalTimes)


class TokenPool:
    def __init__(self, tokenList):
        self.tokenPool = []

        self.speed = 90/120
        self.ind = 0
        self.lock = threading.Lock()
        for token in tokenList:
            self.tokenPool.append(tokenItem(token))
        
    def getToken(self):
        
        self.lock.acquire()
        while(1):
            ind = random.randint(0,len(self.tokenPool)-1)
            # first time using token
            if self.tokenPool[ind].time == -1:
                self.tokenPool[ind].time = time.time()
                self.tokenPool[ind].times += 1
                self.lock.release()
                return self.tokenPool[ind].token, ind
            elif time.time() - self.tokenPool[ind].time > 20:
                self.tokenPool[ind].time = time.time()
                self.tokenPool[ind].times = 0
                continue
            elif self.tokenPool[ind].times <= self.speed * (time.time() - self.tokenPool[ind].time) * .986:
                self.tokenPool[ind].times += 1
                self.lock.release()
                return self.tokenPool[ind].token, ind
            else:
                pass
    def getToken_1(self, ind):
        ind = int(ind)
        self.lock.acquire()
        while(1):
            time.sleep(0.01)
            # first time using token
            if self.tokenPool[ind].time == -1:
                self.tokenPool[ind].time = time.time()
                self.tokenPool[ind].times += 1
                self.lock.release()

                return self.tokenPool[ind].token
            elif time.time() - self.tokenPool[ind].time > 20:
                self.tokenPool[ind].time = time.time()
                self.tokenPool[ind].times = 0
                continue
            elif self.tokenPool[ind].times <= self.speed * (time.time() - self.tokenPool[ind].time) * .986:
                self.tokenPool[ind].times += 1
                self.lock.release()
                return self.tokenPool[ind].token
            else:
                continue
# a = TokenPool([
#         "token_1",
#         "token_2",
#         "token_3",
#         "token_4",
#         "token_5",
#     ])

# def func_1():
#     start = time.time()
#     for i in range(0,100):
#         # print("In thread_1, {}".format(a.getToken()))
#         a.getToken()
#     end = time.time()
#     print(end - start)


if __name__ == "__main__":
    t = []
    k = 6
    for i in range(0, k):    
        t.append(threading.Thread(target=func_1))

    for i in range(0, k):    
        t[i].start()



