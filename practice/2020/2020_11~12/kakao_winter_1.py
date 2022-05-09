import requests

statusQuery = 'MALFUNCTIONING'
# statusQuery = 'STOP'
parentId = 7

URL = "https://jsonmock.hackerrank.com/api/iot_devices/search"
params = {'status': statusQuery, 'page': parentId}
res = requests.get(URL, params=params)
pa = res.json()['total_pages']
total = 0
cnt = 0
for i in range(pa + 1):
    URL = "https://jsonmock.hackerrank.com/api/iot_devices/search"
    params = {'status': statusQuery, 'page': i}
    res = requests.get(URL, params=params)
    da = res.json()['data']
    for d in da:
        try:
            if d['parent']['id'] == parentId:
                total += d['operatingParams']['rotorSpeed']
                cnt += 1
        except:
            pass
if cnt == 0:
    result = 0
else:
    result = int(total / cnt)
print(result)