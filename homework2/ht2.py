from datetime import datetime, timedelta



a = datetime(2017, 3, 5)
print(a) # datetime.datetime(2017, 3, 5, 0, 0)

dt_n = datetime.now().strftime('%d %m %Y')
dt_y = datetime.today() - timedelta(days=1)
dt_t = datetime.today() + timedelta(days=1)
dt_m = datetime.today() + timedelta(6*30)

print(f"now {dt_n}, yesterday {dt_y.strftime('%d %m %Y')}, tomorrow {dt_t.strftime('%d %m %Y')}, mounth {dt_m.strftime('%d %m %Y')}")


date_str = '01/01/17 12:10:03.234567'
dt = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(dt)

