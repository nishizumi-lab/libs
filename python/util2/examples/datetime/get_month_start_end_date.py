# -*- coding: uTf-8 -*-
from util2.datetime.datetime import Datetime

FIRST_DATE = "2019/04/01"
LAST_DATE = "2019/04/30"
DATE_FORMAT = '%Y/%m/%d'
MONTH_NUM = 3

dtex = Datetime()
dates = dtex.month_first_last_date(
    FIRST_DATE, LAST_DATE, MONTH_NUM, date_format=DATE_FORMAT)

print(dates['first_dates'])
#[datetime.datetime(2019, 4, 1, 0, 0), datetime.datetime(2019, 5, 1, 0, 0),
# datetime.datetime(2019, 6, 1, 0, 0), datetime.datetime(2019, 7, 1, 0, 0)]

print(dates['last_dates'])
#[datetime.datetime(2019, 4, 30, 0, 0), datetime.datetime(2019, 5, 31, 0, 0),
# datetime.datetime(2019, 6, 30, 0, 0), datetime.datetime(2019, 7, 31, 0, 0)]

print(dates['first_dates_string'])
# ['2019/05/01', '2019/06/01', '2019/07/01']

print(dates['last_dates_string'])
# ['2019/05/31', '2019/06/30', '2019/07/31']
