import datetime

time = "Jan 15, 2023 - 12:05:33"
python_time = datetime.datetime.strptime(time, '%b %d, %Y - %H:%M:%S')
new_format = datetime.datetime.strftime(python_time, '%d.%m.%Y, %H:%M')
print(python_time.month)
print(new_format)
