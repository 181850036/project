from CodeProcesser import CodeProcesser
from decimal import Decimal
class DataProcesser:

    '''
    本类用来预处理所需要的数据
    参数说明:
    .userIds:index （0，271） 全体学生的id
    .cases:index （0，271） 全体学生的做题情况
    .invalidNum:index （0，271） 全体学生的无效题目数量 在初始化时已经将cases中这部分题目得分设为0
    .avgPerGroup:index （0,5） 五个组别的平均得分
    '''
    def __init__(self,data):
        #全部学生的Id
        self.userIds = []
        #全部学生的做题信息
        self.cases = dict()
        #无效题目数量
        self.invalidNum=[0]*271
        for i in data:
            self.userIds.append(i)
        for i in range(0, 271):
            self.cases[i] = (data[self.userIds[i]]['cases'])
            for j in range(0,len(self.cases[i])):
                if not self.isValid(self.cases[i][j]):
                    self.invalidNum[i]+=1
                    self.cases[i][j]['final_score']=0
        codeProcesser=CodeProcesser(self.userIds,self.cases)
        codeProcesser.group()
        avgPerGroup=codeProcesser.AvgPerGroup()
    '''
    @:param:case
    @:Description:若此题得分为面向用例则无效，判别方式是若最终满分，且后四次得分递增，间隔时间短于1分钟
    @:return:list(float)
    '''
    def isValid(self,case):
        if case['final_score']==100:
            if len(case['upload_records'])>=4:
                if case['upload_records'][-1]['score']-case['upload_records'][-2]['score']==case['upload_records'][-2]['score']-case['upload_records'][-3]['score']\
                    and case['upload_records'][-1]['score']-case['upload_records'][-2]['score']==case['upload_records'][-3]['score']-case['upload_records'][-4]['score']\
                    and case['upload_records'][-1]['upload_time']-case['upload_records'][-2]['upload_time']<60000\
                    and case['upload_records'][-2]['upload_time']-case['upload_records'][-3]['upload_time']<60000\
                    and case['upload_records'][-3]['upload_time']-case['upload_records'][-4]['upload_time']<60000:
                        return False
        #print("wuhu!")
        return True

    '''
    @:param:cases
    @:Description:预处理，返回每人平均得分
    @:return:list(float)
    '''
    def Avg(self):
        cases=self.cases
        res = []
        for i in range(0, 271):
            score = 0  # 得分
            for j in range(0, len(cases[i])):
                score += cases[i][j]['final_score']
            score /= len(cases[i])
            res.append(score)
        # for i in range(0, 271):
        #     res[i] = Decimal(res[i]).quantize(Decimal('0.0'))
        return res

    '''
    @:param:cases
    @:Description:返回每个人所有提交题目的平均提交次数
    @:return:list(float)
    '''
    def UploadTimes(self):
        cases=self.cases
        res = []
        for i in range(0, 271):
            times = 0
            for j in range(0, len(cases[i])):
                times += len(cases[i][j]['upload_records'])
            times /= len(cases[i])
            res.append(times)
        # for i in range(0,271):
        #     res[i]=Decimal(res[i]).quantize(Decimal('0.0'))
        return res

    '''
    @:param:cases
    @:Description:返回每个人满分题目总数
    @:return:list(int)
    '''

    def AcNum(self):
        cases=self.cases
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

    def AllTime(self):
        cases=self.cases
        res = []
        for i in range(0, 271):
            tmp = []
            for j in range(0, len(cases[i])):
                for k in cases[i][j]['upload_records']:
                    tmp.append(k['upload_time'])
            tmp.sort()
            if len(tmp) > 1:
                diff = int(tmp[-1]) - int(tmp[0])
                diff = int(diff / 1000)
                sec = diff % 60
                diff = int(diff / 60)
                min = diff % 60
                diff = int(diff / 60)
                hour = diff % 24
                day = int(diff / 24)
                tmp = []
                tmp.append(day)
                tmp.append(hour)
                tmp.append(min)
                tmp.append(sec)
            else:
                tmp = [0, 0, 0, 0]
            res.append(tmp)
        return res

    '''
    @:param:cases
    @:Description:返回每个人所有题目的平均debug时间,符合要求题目数量(单位：秒,道)
    @:return:list(list(float,int))
    '''

    def AvgDebugTime(self):
        cases=self.cases
        res = []
        for i in range(0, 271):
            num = 0
            time = 0
            for j in range(0, len(cases[i])):
                # 此处计算满分题目的debug时间，从首次提交到最后一次提交所用时间，若超过6h则视为有间断，不计算
                if cases[i][j]['final_score'] == 100 and len(cases[i][j]['upload_records']) > 1:
                    timeDiff = int(cases[i][j]['upload_records'][-1]['upload_time']) - int(
                        cases[i][j]['upload_records'][0]['upload_time'])
                    timeDiff = int(timeDiff / 1000)
                    if (timeDiff < 21600):
                        time += timeDiff
                        num += 1
            # print(time,num)
            if num == 0:
                res.append([0, 0])
            else:
                res.append([time / num, num])
        # for i in range(0, 271):
        #     res[i][0] = Decimal(res[i][0]).quantize(Decimal('0.0'))
        return res