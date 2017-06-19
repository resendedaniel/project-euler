import datetime
start = datetime.datetime.strptime("1901-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2000-12-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

print(sum([1 for d in date_generated if d.day == 1 and d.weekday() == 6]))

# neat
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        print(datetime.datetime(y,m,1))
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print count


df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5]})
pd.to_datetime(df)