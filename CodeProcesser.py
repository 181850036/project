class CodeProcesser:
    '''
    本类用来对学生和题目进行分组，并计算不同组数的题目难度
    参数说明:
    .cGroup:index(0,5)， 五个题目组 第五组只有199题，其他组200题
    .uGroup:index(0,5)， 五个学生组 人数分别为53，53,44,67,56
    '''
    def __init__(self,userIds,cases):
        self.cases=cases
        self.userIds=userIds
        self.cGroup=[[],[],[],[],[]]
        self.uGroup=[[],[],[],[],[]]

    '''
    @:param:cases
    @:Description:将所有人按照所做题目分组
    @:return:list(float)
    '''
    def group(self):
        index=0
        cases=self.cases
        #第一遍，从完成所有题目的人中进行，能得到5组题目 其中有一组199道题
        for i in range(0,271):
            if len(cases[i])==200:
                tmp=[]
                for j in range(0,200):
                    tmp.append(cases[i][j]['case_id'])
                tmp.sort()
                exist=False
                for k in range(0,index):
                    if tmp==self.cGroup[k]:
                        exist=True
                if not exist:
                    self.cGroup[index]=tmp
                    index+=1
            elif len(cases[i])==199:
                tmp = []
                for j in range(0, 199):
                    tmp.append(cases[i][j]['case_id'])
                tmp.sort()
                self.cGroup[4]=tmp
        #第二遍，把user归组
        for i in range(0, 271):
            foundIn0To4=False
            tmp = []
            for j in range(0, len(cases[i])):
                tmp.append(cases[i][j]['case_id'])
            tmp.sort()
            for groupIndex in range(0,4):
                belongThisGroup=True
                for k in tmp:
                    if not k in self.cGroup[groupIndex]:
                        belongThisGroup=False
                if belongThisGroup:
                    foundIn0To4=True
                    self.uGroup[groupIndex].append(self.userIds[i])
            if not foundIn0To4:
                self.uGroup[4].append(self.userIds[i])
        #以下打印各组题目、各组学生以及数量
        for i in self.cGroup:
            print(i)
        for i in range(0,5):
            print(len(self.cGroup[i]))
        for i in self.uGroup:
            print(i)
        for i in range(0, 5):
            print(len(self.uGroup[i]))
    '''
    @:param:cases
    @:Description:返回5个组的平均得分
    @:return:list(float)
    '''
    def AvgPerGroup(self):
        res=[]
        #前四组200道
        for group in range(0,4):
            sum=0
            for userid in range(0,271):
                if self.userIds[userid] in self.uGroup[group]:
                    for case in self.cases[userid]:
                        sum+=case['final_score']
            sum=sum/len(self.uGroup[group])/200
            res.append(sum)
            print(sum)
        sum=0
        #第五组199道
        for userid in range(0,271):
            if self.userIds[userid] in self.uGroup[4]:
                for case in self.cases[userid]:
                    sum+=case['final_score']
        sum=sum/len(self.uGroup[4])/199
        res.append(sum)
        print(sum)
        return res

