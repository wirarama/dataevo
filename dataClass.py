import random as rd
import datetime as dt
class dataClass:
    start = ''
    end = ''
    form = '%Y-%m-%d %H:%M:%S'
    out = None
    last = []
    lasth = -1
    n = 5
    cuaca = 1
    def __init__(self,n,file='Data.csv',
                 start='2013-01-01 00:00:00',
                 end='2014-01-01 00:00:00'):
        self.start=start
        self.end=end
        for x in range(n):
            self.last.append(0)
        self.out = open(file,'w')
        self.out.write('date,light,temp,voltage,current,humidity\n')
        self.randRow()
    def randRow(self):
        d = dt.datetime.strptime(self.start,self.form)
        e = dt.datetime.strptime(self.end,self.form)
        while d<e:
            d += dt.timedelta(seconds=1)
            self.lasth = d.hour
            rw = self.randCol(d)
            rwstr = ",".join(rw)
            self.out.write(rwstr+"\n")
    def randCol(self,d):
        out = []
        out.insert(0,d.strftime(self.form))
        col = self.colmaker(d.hour)
        i = 0
        for x in col:
            cl = self.resexcept(x,i)
            out.append(str(cl))
            i+=1
        self.last[0] = float(out[1])
        self.last[1] = float(out[2])
        return out
    def resexcept(self,x,i):
        cl = rd.uniform(x[0],x[1])
        if i == 1 and cl>36:
            cl = rd.uniform(36,37)
        if cl<0:
            cl = 0
        return cl
    def colmaker(self,h):
        #if mendung...
        if h != self.lasth:
            p = rd.randint(1,100)
            if p > 70:
                self.cuaca = 0
            else:
                self.cuaca = 1
        out = []
        for x in range(self.n):
            out.append(0)
        if h in [17,18]:
            out[0] = [self.last[0]-35,self.last[0]-30]
        elif h in [19]:
            if self.last[0] < 100:
                out[0] = [self.last[0]-4,self.last[0]]
            else:
                out[0] = [self.last[0]-50,self.last[0]-40]
        elif h in [13,14,15,16]:
            if self.cuaca == 1:
                out[0] = [self.last[0]-15,self.last[0]-10]
            else:
                out[0] = [self.last[0]-35,self.last[0]-5]
        elif h in [4,5,6]:
            out[0] = [self.last[0]+30,self.last[0]+35]
        elif h in [8,9]:
            if self.cuaca == 1 and self.last[0] < 100000:
                out[0] = [self.last[0]+20,self.last[0]+35]
            else:
                out[0] = [self.last[0]-0,self.last[0]+5]
        elif h in [11,12]:
            if self.cuaca == 1 and self.last[0] < 812000:
                out[0] = [self.last[0]+25,self.last[0]+40]
            else:
                out[0] = [self.last[0]-0,self.last[0]+5]
        else:
            out[0] = [self.last[0]-2,self.last[0]+2]
        #other cols
        if self.last[0]>1000 and self.last[0]<=1999:
            out[1] = [self.last[0]/100+20,self.last[0]/100+26]
            out[2] = [self.last[0]/1000,self.last[0]/1000+4]
            out[3] = [self.last[0]/1000,self.last[0]/1000+2]
            if self.cuaca == 1:
                out[4] = [self.last[0]/30,self.last[0]/20]
            else:
                out[4] = [self.last[0]/22,self.last[0]/20]
        elif self.last[0]>1999:
            out[1] = [32,38]
            if self.last[1] >= 36:
                out[2] = [0,3]
                out[3] = [2,4]
            else:
                out[2] = [1,2]
                out[3] = [0,2]
            out[4] = [30,40]
        else:
            out[1] = [27,29]
            out[2] = [0,3]
            out[3] = [2,4]
            out[4] = [30,40]
        return out