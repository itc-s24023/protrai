#24023
#現在の時刻と2024年6月のカレンダーを表示する「time_cal.py」
#

import calendar as cal
print(cal.month(2024,6))

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y年%m月%d日　%H:%M:%S"))



