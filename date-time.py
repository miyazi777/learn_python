from datetime import datetime
from datetime import timedelta

# 指定日
str_date = '2016-10-20 12:32:56'
# 日付へ変換
one_day = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
# 5日前
five_day = one_day - timedelta(days=5)
# 文字列に変換
print_date = five_day.strftime('%Y-%m-%d %H:%M:%S')
# 表示
print(print_date)   # 2016-10-15 12:32:56
