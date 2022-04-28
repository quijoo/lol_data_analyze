import threading
import copy
import time
import hashlib

class urlPool:
    urls = []
    pos = 0
    def __init__(self, file):
        self.file = file
        self.lock = threading.Lock()
        with open(file, "r") as f:
            for line in f.readlines():
                
                url = line.replace("\n", "").split(" ")[0]
                status = line.replace("\n", "").split(" ")[1]
                # print(status, url)
                if status != "1":
                    self.urls.append([url, 0])
        self.lens = len(self.urls)

        svaeFileThread = threading.Thread(target=self.save)
        svaeFileThread.start()
    

    def hash(self, file):
        md5_1 = hashlib.md5()
        with open(file, 'rb') as f:
            while(1):
                data = f.read(bytes)
                if data:
                    md5_1.update(data)
                else:
                    break
        ret = md5_1.hexdigest()
        return ret

    def save(self):
        md5 = ""
        while(1):
            time.sleep(2)
            self.lock.acquire()
            tmp = hash(self.file)
            if md5 == tmp:
                break
            else:
                md5 = tmp

            with open(self.file, "w") as f:
                for item in self.urls:
                    if item[1] == 0:
                        f.write("{} {}\n".format(item[0], item[1]))
            
            self.lock.release()

                
    def getUrl(self):
        self.lock.acquire()
        res = self.urls[self.pos][0]
        # print(self.lens, self.urls)
        self.urls[self.pos][1] = 1
        self.pos = (self.pos + 1)%self.lens
        self.lock.release()
        return  res



if __name__ == "__main__":
    urlss = urlPool("data.urls")
    for i in range(0, 5):
        print(urlss.getUrl())
        


         