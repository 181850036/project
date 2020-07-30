import json
from Analyser import Analyser
from DataProcesser import DataProcesser
from CodeProcesser import CodeProcesser
import math
def main():
    f=open('test_data.json',encoding='utf-8')
    res=f.read()
    data=json.loads(res)
    #获得所有人做过题目的平均得分、完成题目总数、平均提交次数、总共历时和
    dataProcesser=DataProcesser(data)
    avg=dataProcesser.Avg()
    acNum=dataProcesser.AcNum()
    for i in range(0,271):
        if(acNum[i]>200):
            acNum[i]=200
    uploadNum=dataProcesser.UploadTimes()
    alltime=dataProcesser.AllTime()
    avgDebugTime=dataProcesser.AvgDebugTime()
    userIds=dataProcesser.userIds
    codeProcesser=CodeProcesser(dataProcesser.userIds,dataProcesser.cases)
    codeProcesser.group()
    for i in range(0,271):
        acNum[i]-=dataProcesser.invalidNum[i]
        if(acNum[i]<0):
            acNum[i]=0
    analyser=Analyser(avg, acNum,uploadNum,alltime,avgDebugTime,userIds,dataProcesser.cases)
    ultimateScore = analyser.ultimateScore()
    ug = codeProcesser.uGroup
    avgPerGroup = codeProcesser.AvgPerGroup()
    hardest = min(avgPerGroup)
    '''根据每组题目难度平衡分数'''
    for i in range(0, 271):
        for j in range(0, 5):
            if (userIds[i] in ug[j]):
                ultimateScore[i] = ultimateScore[i] / (hardest / avgPerGroup[j])
    for i in range(0,len(userIds)):
        print("id: "+str(userIds[i])+" 完成数:" +str(acNum[i])+" 平均分:"+str(avg[i])+" 平均提交次数:"+str(uploadNum[i])+
              " 历时:"+str(alltime[i])+" 平均debug时间:"+str(avgDebugTime[i][0])+"秒"+" 总分:"+str(ultimateScore[i]))
    # for i in range(0,271):
    #     print(ultimateScore[i])

    print(max(ultimateScore))
    res=[0]*11
    for i in range(0,271):
        res[math.floor((ultimateScore[i])//10)-1]+=1
    print(res)
if __name__ == '__main__':
    main()