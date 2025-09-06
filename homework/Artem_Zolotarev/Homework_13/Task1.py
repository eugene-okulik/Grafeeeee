from datetime import datetime, timedelta
import re
import os


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(data_path, 'r', encoding='UTF-8') as new_file:
        for line in new_file.readlines():
            yield line


expression = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}'
lst = []
for data_line in read_file():
    match = datetime.strptime(re.search(expression, data_line).group(), "%Y-%m-%d %H:%M:%S.%f")
    lst.append(match)

now = datetime.now()
date1, date2, date3 = lst
print(date1 + timedelta(days=7))
print(datetime.isoweekday(date2))
days = now - date3
print(days.days)
