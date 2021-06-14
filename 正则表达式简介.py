import re

#正则表达式简介
#怎样验证一个字符串是日期YYYY-MM-DD格式？
#正则表达式：一些由字符和特殊符号组成的字符串，它们描述了重复模式，能够匹配多个字符串

def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None

date1 = "2021-02-03"

date2 = "202-01-04"

date3 = "2022/05/05"

date4 = "20210707"

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))


