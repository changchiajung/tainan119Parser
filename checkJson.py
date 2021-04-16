import json
import os

def deptAdd(d,deptResult):
    if d in deptResult:
        deptResult[d] += 1
    else:
        deptResult[d] = 1

if __name__ == '__main__':
    if os.path.exists('119Result.json'):
        jsonFile = open('119Result.json',)
        jsonData = json.load(jsonFile)
    else:
        jsonData = {}
    
    deptResult={}
    for row in jsonData:
        depts = jsonData[row]["DEPT_NAME"]
        if ',' in depts:
            for d in depts.split(","):
                deptAdd(d,deptResult)
        else:
            deptAdd(depts,deptResult)
    print("total num: {}".format(len(jsonData)))
    print(deptResult)
