import time, datetime, urllib.request, json

url24h = 'https://data.sensor.community/static/v2/data.24h.json'
today = datetime.datetime.now()
exactImportTime = datetime.datetime(today.year, today.month, today.day, 17, 0, 0)
awaitingTime = exactImportTime - today
time.sleep(awaitingTime.total_seconds())

today = datetime.datetime.now()
with urllib.request.urlopen(url24h) as url:
    data24h = json.load(url)
with open('output/24h/data24h_{}-{}-{}_{}h{}.json'.format(today.year, today.month, today.day, today.hour, str(today.minute).zfill(2)), 'w') as outfile:
    json.dump(data24h, outfile)