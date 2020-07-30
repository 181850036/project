import json
from Analyser import Analyser
from DataProcesser import DataProcesser
from CodeProcesser import CodeProcesser
import math
from scipy import stats
import numpy as np
def verify(ultimateScore):
    """
    kstest方法：KS检验，参数分别是：待检验的数据，检验方法（这里设置成norm正态分布），均值与标准差
    结果返回两个值：statistic → D值，pvalue → P值
    p值大于0.05，为正态分布
    H0:样本符合
    H1:样本不符合
    如何p>0.05接受H0 ,反之
    """
    u = np.mean(ultimateScore)  # 计算均值
    std = np.std(ultimateScore)  # 计算标准差
    print(u,std)
    res=stats.kstest(ultimateScore, 'norm', (u, std))
    print(res)
def main():
    f=open('test_data.json',encoding='utf-8')
    res=f.read()
    data=json.loads(res)
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
                ultimateScore[i] = ultimateScore[i] / (avgPerGroup[j] / hardest)
    '''打印中间数据'''
    for i in range(0,len(userIds)):
        print("id: "+str(userIds[i])+" 完成数:" +str(acNum[i])+" 平均分:"+str(avg[i])+" 平均提交次数:"+str(uploadNum[i])+
              " 历时:"+str(alltime[i])+" 平均debug时间:"+str(avgDebugTime[i][0])+"秒"+" 总分:"+str(ultimateScore[i]))
    print(max(ultimateScore))
    res=[0]*10
    '''分组'''
    for i in range(0,271):
        if(ultimateScore[i]%10!=0):
            res[math.floor((ultimateScore[i]-ultimateScore[i]%10)//10)]+=1
        elif(ultimateScore[i]==0):
            res[0]+=1
        else:
            res[math.floor((ultimateScore[i])) // 10-1] += 1
    print("分数区间:",end="")
    print(res)
    ultimateScore.sort()
    print("最终得分:",end="")
    print(ultimateScore)
    verify(ultimateScore)
if __name__ == '__main__':
    main()
