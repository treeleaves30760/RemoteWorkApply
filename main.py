from urllib import request
import urllib.parse
from urllib.request import *
dataTime = {"historicalDataEndDate" : '2021/09/20', "historicalDataStartDateFormatted" : '08/01/2021', 'historicalDataStartDate' : '2021/08/01'}
dataTime = urllib.parse.urlencode(dataTime).encode('utf8')
url = 'https://cn.investing.com/equities/apple-computer-inc-historical-data' + '?' + str(dataTime)[2:-1]
print(url)
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', }
response = Request(url, headers = header)
content = str(urlopen(response).read()).split("\\n")

start = 0
end = 0
gets = 0
datas = []
dataTag = ["date", "price", "open", "high", "low", "vol", "change"]
for i in range(len(content)):
    if not gets and "<table " in content[i] and " id=\"curr_table\"" in content[i]:
        start = i
        gets = 1
    if gets and "</table>" in content[i]:
        end = i + 1
        break
firstget = 0
i = start
# print(content[start: end])
while(i < end + 1):
    if "<td" in content[i]:
        dicts = {}
        dstart = 0
        dend = 0
        for ind in range(6):
            dgets = 0
            dstart = content[i + ind].find("data-real-value=\"") + 17
            for k in range(dstart + 1, len(content[i + ind])):
                if content[i + ind][k] == "\"":
                    dend = k
                    break
            # print(content[i + ind][dstart : dend])
            if ind == 0:
                dicts[dataTag[ind]] = str(content[i + ind][dstart : dend])
            else:
                dicts[dataTag[ind]] = float(content[i + ind][dstart : dend])
        dicts["id"] = len(datas)
        datas.append(dicts)
        i += 6
    else:
        i += 1
print(datas)
print(len(datas))