"""from datetime import datetime
current_=datetime.now()
print(current_)
print(current_.strftime('%y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))

from datetime import datetime, date
current_=datetime.now().today()
now = datetime.now()
#print(today)
#print(now)
print(current_.strftime("%d/%m/%y %I:%M:%S %p"))


%d----->  DAY IN THE MONTH

%m----->  month in the year

%y----->   year

%h----->   hour

%m----->   minute

%s----->   second

%I----->   12 hour clock

%p----->    AM OR PM



import calendar

#print(calendar.calendar(2026))
print(calendar.month(2026,9))
print(calendar.weekday(2026,9,24))
print(calendar.isleap(2026))


Data Analysis
------------------

------>Data Analysis is the process of inspecting,cleaning,transform and modelling data to discover useful insights,support decision making,and identify
pattern it is widely used in industries such as finance,healthcare,marketing,and technology.

Types of Data Analysis

-------------------------
1.Descriptive Analysis-- summarizind data
(ex: average sales per month)

2.Diagonstic Analysis-- understanding causes
(ex: why sales dropped)

3.Predictive Analaysis--- forecasting future outcomes
(es: predicting customer churn)

4. prescriptive Analysis-- suggesting actions based on data
(ex:  best maeketing staragey)

Numpy
----------------
---->numpy is an library in python which is known as  numerical python.
----> this numpy have different diamentinal arrys such as 1D,2D,3D.
---->to used the numpy we have to import library as import numpy as np.
ex:
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

Indexing in array:
-------------------
---->as we used indexing in the list or tuple,here the way it works.
---->by calling index position from array,we will the get the value
-----> and negative indexing alse will work.

ex:negative indexing:
    
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[-1])

ex:normal indexing:

import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[1])

ex:slicing:
    
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[:2])

ex:
    
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())

ex:2D:
import numpy as np
arr_1 = np.array([1,2,3],[4,5,6])
print(arr_1)

import numpy as np
arr_1 = np.array([1,2,3],[4,5,6],[7,8,9])
print(arr_1)
print(arr_1.reshape(2,3))


ex:3D:

import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr_1)
print(arr_1.reshape(4,3))

Pandas
----------------
----> pandas is an powerfull python library and this is built on the top numpy.
---->by using pandas data manipulation will be done.
---->pandas have data structured likes series and dataframes.
-----> to use this we have import the library.

import pandas as pd

ex:
import pandas as pd
Data = pd.Series(
     data=[2000,4000,7000],
    index = ['earphone','charger','mobiles']
)
print(Data)

ex:"""

import pandas as pd
df = {
    "Product": [ 'laptop','mobiles','earphones','charger'],
    "Brand" :  ['Mac','Realme','Iphone'],
    "Price" :  [5700,1500,2500],
    "stocks" :  [5,15,9],
    "Sales"  :  ['Amazon','Offline','Flipkart']
}
data = pd.DataFrame(df)
print(data)
     
     
































