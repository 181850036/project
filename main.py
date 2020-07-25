import json
import urllib.request,urllib.parse
import os
'''
@:param:cases
@:Description:预处理，返回每人平均分
@:return:list
'''
def Avg(cases):
    res=[]
    for i in range(0,271):
        score=0 #得分
        for j in range(0,len(cases[i])):
            score+=cases[i][j]['final_score']
        score/=len(cases[i])
        res.append(score)
    return res
'''
@:param:cases
@:Description:返回每个人每次的平均debug时间(每道题的完成时间除以每道题的提交次数-1)
@:return:list(int)
'''
def DebugTime(cases):

    return
'''
@:param:cases
@:Description:返回每个人所有提交题目的平均提交次数
@:return:list(int)
'''
def UploadTimes(cases):
    res=[]
    for i in range(0,271):
        times=0
        for j in range(0,len(cases[i])):
            times+=len(cases[i][j]['upload_records'])
        times/=len(cases[i])
        res.append(times)
    return res
'''
@:param:cases
@:Description:返回每个人的提交过的题目总数
@:return:list(int)
'''
def uploadNum(cases):
    return
'''
@:param:cases
@:Description:返回每个人满分题目总数
@:return:list(int)
'''
def AcNum(cases):
    res = []
    for i in range(0, 271):
        num = 0  # 完成数
        for j in range(0, len(cases[i])):
            if cases[i][j]['final_score'] == 100:
                num += 1
        res.append(num)
    return res
'''
@:param:cases
@:Description:返回每个人第一次提交和最后一次提交的时间差(单位：天,小时,分钟,秒)
@:return:list(list(int,int,int,int))
'''
def AllTime(cases):
    res=[]
    for i in range(0,271):
        tmp=[]
        for j in range(0,len(cases[i])):
            for k in cases[i][j]['upload_records']:
                tmp.append(k['upload_time'])
        tmp.sort()
        if len(tmp)>1:
            diff=int(tmp[-1])-int(tmp[0])
            diff=int(diff/1000)
            sec=diff % 60
            diff=int(diff/60)
            min=diff % 60
            diff=int(diff/60)
            hour=diff %24
            day=int(diff/24)
            tmp=[]
            tmp.append(day)
            tmp.append(hour)
            tmp.append(min)
            tmp.append(sec)
        else:
            tmp=[0,0,0,0]
        res.append(tmp)
    return res
'''
@:param:cases
@:Description:返回每个人所有题目的平均完成时间,符合要求题目数量(单位：秒,道)
@:return:list(list(float,int))
'''
def AvgDebugTime(cases):
    res=[]
    for i in range(0,271):
        tmp=[]
        num=0
        time=0
        for j in range(0, len(cases[i])):
            #此处计算满分题目的debug时间，从首次提交到最后一次提交所用时间，若超过12h则视为有间断，不计算
            if cases[i][j]['final_score']==100 and len(cases[i][j]['upload_records'])>1:
                timeDiff=int(cases[i][j]['upload_records'][-1]['upload_time'])-int(cases[i][j]['upload_records'][0]['upload_time'])
                timeDiff=int(timeDiff/1000)
                if(timeDiff<43200):
                    time+=timeDiff
                    num+=1
        #print(time,num)
        if num==0:
            res.append([0,0])
        else:
            res.append([time/num,num])
    print(res)
    return res
def main():
    f=open('test_data.json',encoding='utf-8')
    res=f.read()
    data=json.loads(res)
    userIds=[]
    # cases为每个人的每道题目完成情况 len为271
    cases=dict()
    sum=0
    for i in data:
        userIds.append(i)
    for i in range(0,271):
        cases[i]=(data[userIds[i]]['cases'])
    for i in range(0,len(cases[0])):
        sum+=cases[0][i]['final_score']
    #获得所有人做过题目的平均得分、完成题目总数、平均提交次数和总共历时
    avg=Avg(cases)
    acNum=AcNum(cases)
    uploadNum=UploadTimes(cases)
    alltime=AllTime(cases)
    avgDebugTime=AvgDebugTime(cases)
    # for i in range(0,len(userIds)):
    #     print("id: "+str(userIds[i])+" 完成数:" +str(acNum[i])+" 平均分:"+str(avg[i])+" 平均提交次数:"+str(uploadNum[i]))
if __name__ == '__main__':
    main()