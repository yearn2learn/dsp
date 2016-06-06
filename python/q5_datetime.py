# Hint:  use Google to find python function

from datetime import datetime

def dateDiff(start, stop, format='%m-%d-%Y'):
  date1 = datetime.strptime(start, format).date()
  date2 = datetime.strptime(stop, format).date()
  result = (date2 - date1).days
  print('There are %s days between %s and %s.' % (result, date1, date2))

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
dateDiff(date_start, date_stop)
# There are 937 days between 2013-01-02 and 2015-07-28.

####b)  
date_start = '12312013'  
date_stop = '05282015'  
dateDiff(date_start, date_stop, '%m%d%Y')
# There are 513 days between 2013-12-31 and 2015-05-28.

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
dateDiff(date_start, date_stop, '%d-%b-%Y')
# There are 7850 days between 1994-01-15 and 2015-07-14.
