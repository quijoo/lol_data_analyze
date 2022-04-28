import time
def getOpp(k, l):
    me = l[k-1]
    counter = 0
    value = -1
    # print('-----------------------------------')
    for i in range(0, len(l)):
        # print(l[i], me)
        if roleDefine(l[i][1], l[i][0]) == roleDefine(me[1], me[0]) and ((k<=5 and i+1>5) or (k>5 and i+1 <=5)):
            value = i+1
            break
    return value
def safeValue(dic, s1, s2, default_value = ''):
    try:
        dic[s1] = s2
    except:
        dic[s1] = default_value
        print("Wrong in access <{}>".format(s1))
    return dic


class tokenGameMap:
    pool = dict()
    def add(self, gameid, index):
        self.pool[gameid] = index
    def getIndex(self, gameid):
        if gameid in self.pool:
            token = self.pool[gameid]
            return  token
        else:
            return -1

def roleDefine(role, lane):
    res = "-1"
    if role == "SOLO" and (lane == "BOTTOM" or lane == "TOP"):
        res = "TOPSOLO"
    elif role == "DUO_CARRY":
        res = "BOTTOM"
    elif role == "DUO_SUPPORT":
        res = "SUPPORT"
    elif lane == "JUNGLE":
        res = "JUNGLE"
    elif lane == "MIDDLE":
        res = "MIDDLE"
    else:
        res = "-1"
    return res