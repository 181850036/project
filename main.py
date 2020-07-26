import json
from Analyser import Analyser
from DataProcesser import DataProcesser

def main():
    f=open('test_data.json',encoding='utf-8')
    res=f.read()
    data=json.loads(res)
    #获得所有人做过题目的平均得分、完成题目总数、平均提交次数、总共历时和
    dataProcesser=DataProcesser(data)
    avg=dataProcesser.Avg()
    acNum=dataProcesser.AcNum()
    uploadNum=dataProcesser.UploadTimes()
    alltime=dataProcesser.AllTime()
    avgDebugTime=dataProcesser.AvgDebugTime()
    userIds=dataProcesser.userIds
    print(dataProcesser.invalidNum)
    #for i in range(0,len(userIds)):
    #    print("id: "+str(userIds[i])+" 完成数:" +str(acNum[i])+" 平均分:"+str(avg[i])+" 平均提交次数:"+str(uploadNum[i])+" 历时:"+str(alltime[i])+" 平均debug时间:"+str(avgDebugTime[i][0])+"秒")
if __name__ == '__main__':
    main()