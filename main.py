import json
import urllib.request,urllib.parse
import os
'''
@:param:cases
@:Description:返回每个人所有提交了的题目的平均分
@:return:list
'''
def average(cases):
    res=[]
    for i in range(0,271):
        sum=0
        for j in range(0,len(cases[i])):
            sum+=cases[i][j]['final_score']
        sum/=len(cases[i])
        res.append(sum)
    print("平均分：")
    for i in range(0,271):
        print(res[i])
    return res
'''
@:param:cases
@:Description:返回每个人的平均debug时间
@:return:list
'''
def debugTime(cases):
    return
'''
@:param:cases
@:Description:返回每个人的每道题的平均提交次数
@:return:list
'''
def uploadNum(cases):
    return
'''
@:param:cases
@:Description:返回每个人的提交过的题目总数
@:return:list
'''
def uploadQues(cases):
    return
'''
@:param:cases
@:Description:返回每个人满分题目总数
@:return:double
'''
def acNum(cases):
    return
'''
@:param:cases
@:Description:返回每个人第一次提交和最后一次提交的时间差(单位：天)
@:return:int
'''
def allTime(cases):
    return
'''
@:param:cases
@:Description:返回每个人的评价代码行数
@:return:int(向下取整)
'''
def avrLine(cases):
    return
def main():
    f=open('test_data.json',encoding='utf-8')
    res=f.read()
    data=json.loads(res)
    #print(data)
    # cases=data[0]
    # print(cases)
    userIds=[]
    cases=dict()
    sum=0
    for i in data:
        userIds.append(i)
    for i in range(0,271):
        cases[i]=(data[userIds[i]]['cases'])
    for i in range(0,len(cases[0])):
        sum+=cases[0][i]['final_score']
    print(cases[0][4]['upload_records'][0]['upload_time'])
    print(sum/len(cases[0]))
    # for i in range(0,271):
    #     print('{0}:{1}'.format(userIds[i],cases[i]))
    print("id:")
    for i in userIds:
        print(i)
    average(cases)
    # for i in cases:
    #     print(cases[i])
    # for case in cases:
    #     print(case["case_id"],case["case_type"])
    #     print()
    #     filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
    #     print(filename)
    #     urllib.request.urlretrieve(case["case_zip"],filename)
if __name__ == '__main__':
    main()