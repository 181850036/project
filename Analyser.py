from CodeProcesser import CodeProcesser
class Analyser:
    '''
    待完成 对数据进行处理
    '''

    def __init__(self, avg, AcNum,uploadNum,allTime,avgDebugTime,userId,cases):
        self.avg = avg
        self.AcNum = AcNum
        self.uploadNum=uploadNum
        self.allTime=allTime
        self.avgDebugTime=avgDebugTime
        self.userId=userId
        self.cases=cases
    '''满分题目得分，满分40'''
    def AcWeight(self):
        AcNum=self.AcNum
        res=[]
        codeProcesser = CodeProcesser(self.userId,self.cases)
        for i in range(0,271):
            if(self.userId[i] in codeProcesser.uGroup[4]):
                res.append(AcNum[i]/199*40)
            else:
                res.append(AcNum[i]/200*40)
        return res

    '''平均分得分，满分30'''
    def avgWeight(self):
        res=[]
        top = max(self.avg)
        for i in range(0,271):
            res.append(self.avg[i]/top*30)

        return res

    '''平均提交次数得分，满分10'''
    def uploadTimesWeight(self):
        minTime = 10000
        avgAll = 0
        for i in range(0, 271):
            avgAll += self.uploadNum[i]
        avgAll /= 271
        for i in range(0,271):
            if(self.uploadNum[i]<minTime and self.uploadNum[i]>=avgAll and self.AcNum[i]>=100):
                minTime=self.uploadNum[i]
        res=[]
        #print(minTime)
        for i in range(0,271):
            if(self.AcNum[i]==0 or self.uploadNum[i]==0):
                res.append(0)
            elif(self.uploadNum[i]<=avgAll):
                res.append(10)
            else:
                res.append(avgAll/self.uploadNum[i]*10)
        #print(res)
        #print(max(res))
        return res

    '''平均debug时间得分，满分20'''
    def avgDebugTimeWeight(self):
        minTime = 10000
        avgAll=0
        for i in range(0,271):
            avgAll+=self.avgDebugTime[i][0]
        avgAll/=271
        for i in range(0, 271):
            if (self.avgDebugTime[i][0] < minTime and self.avgDebugTime[i][0] > 0 and self.AcNum[i] >= 100 and self.avgDebugTime[i][0]>avgAll):
                minTime = self.avgDebugTime[i][0]
        res = []
        #print(minTime)
        for i in range(0, 271):
            if (self.AcNum[i] == 0 or self.avgDebugTime[i][0]==0):
                res.append(0)
            elif(240<self.avgDebugTime[i][0]<=avgAll):
                res.append(20)
            elif(self.avgDebugTime[i][0]<300):
                res.append(10)
            else:
                res.append(avgAll / self.avgDebugTime[i][0] * 20)
        #print(max(res))
        #print(res)
        return res
    def ultimateScore(self):
        analyser=Analyser
        res=[0]*271

        avgDebugTimeWeight=analyser.avgDebugTimeWeight(self)
        avgWeight=analyser.avgWeight(self)
        AcWeight=analyser.AcWeight(self)
        uploadTimesWeight=analyser.uploadTimesWeight(self)
       # print("252"+" "+str(AcWeight[252])+" "+str(avgWeight[252])+" "+str(avgDebugTimeWeight[252])+" "+str(uploadTimesWeight[252]))
        for i in range(0,271):
            res[i]=res[i]+avgDebugTimeWeight[i]+avgWeight[i]+AcWeight[i]+uploadTimesWeight[i]
        return res