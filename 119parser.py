import requests
import xml.etree.ElementTree as ET
from xml.etree import ElementTree as ET
import json
import os.path
import time


def parseNewData():
    ## Parsing raw xml data from 119 website
    url = "http://210.241.127.68:8080/DTS/caselist/xml"
    obj = ""
    header = {"Content-Type": ""}
    response = requests.post(url, data=obj, headers=header)
    
    with open('data.xml', 'w') as f:
        f.write(response.text)
    
    tree = ET.parse('data.xml')
    root = tree.getroot()
    xmlList = ['CS_KIND','KIND','CS_CODE','IN_TIME','COUNTRY_NAME','TOWN_NAME','ADDR','DEPT_NAME','PERSION_COUNT','CAR_COUNT','STATUS','CS_X','CS_Y']
    
    ## Get old data from json file
    if os.path.exists('119Result.json'):
        jsonFile = open('119Result.json',)
        jsonData = json.load(jsonFile)
    else:
        jsonData = {}
    
    
    ## Parse xml data to dict data, Check if already in json file
    for p in root.findall('.//case'):
    #    if p.find('CS_NO').text in jsonData:
    #        continue
        tmpDict = {}
        for title in xmlList:
            tmpDict[title] = p.find(title).text
        jsonData[p.find('CS_NO').text] = tmpDict
#    print(jsonData)
    
    if jsonData == {}:
        return
    ## Append new data to json file
    with open("119Result.json", "w", encoding='utf8') as outfile:
        json.dump(jsonData, outfile,ensure_ascii=False)


if __name__ == '__main__':
    while True:
        parseNewData()
        time.sleep(1200)
