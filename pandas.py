"""pandas 删除指定行"""

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
df = pd.DataFrame(np.arange(20).reshape(5,4),columns = ['a','b','c','d'],index = range(4,9))

#假设我们只想要b列值为5和13所在行
df[df.b.isin([5,13])]

#但是如果我们想要除了这两行以外的数据怎么办？原理是先把b取出来并转换为列表，然后再从列表中把不需要的行值去掉，然后再在df中使用isin()
test = list(df.b)
test.remove(5)
test.remove(13)
df[df.b.isin(test)]


"""pandas中根据列的值选取多行数据"""
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

data = pd.read_excel(r'C:\Users\MECHREVO\Desktop\新建 Microsoft Excel 工作表.xlsx')
data
	a	b	c	d
1	m	1	one	f
2	m	2	two	f
3	m	3	one	m
4	f	3	five	m
5	f	3	five	f
6	f	5	three	m
7	m	5	one	m
8	f	2	two	m
9	m	1	five	m
10	f	1	three	m

# 选取等于某些值的行记录 用 == 
data.loc[data['c']=='one']
# 选取某列是否是某一类型的数值 用 isin
data.loc[data['b'].isin(['1','3'])]
# 多种条件的选取用 &
data.loc[(data['a']=='m')&(data['d']=='m')]#选取a列和d列同时为m的行
# 选取不等于某些值的行记录 用 ！=
data.loc[data['c']!= 'five']
# isin返回一系列的数值,如果要选择不符合这个条件的数值使用~
data.loc[~data['c'].isin(['one','two'])]

	a	b	c	d
4	f	3	five	m
5	f	3	five	f
6	f	5	three	m
9	m	1	five	m
10	f	1	three	m

"""pandas.DataFrame中删除包涵特定字符串所在的行"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import re
dt_test = pd.read_excel(r'C:\Users\MECHREVO\Desktop\test.xlsx')#导入示例数据
dt_test
	a	b	c	d
3	1	exp111	33l	6
4	2	exp12h	df4	yy89
5	3	4	5	mm5
6	4	5	6	9

#我们要删除b列元素含有'exp'的所有行，当数据量较大时直接使用drop方法显然不合适，那么可以使用如下的方法。
dt_test = dt_test.astype(str)#将所有元素转换为str
y=dt_test[dt_test['b'].str.contains('exp')]#找到b列中含有'exp'的所有行
test1 = list(y.b)#将含有'exp'的所有元素以列表形式取出
test2 = list(dt_test.b)#将原数据框中b列所有元素以列表形式取出
ret = list(set(test2) ^ set(test1))#以list
result = dt_test[dt_test.b.isin(ret)]
result

	a	b	c	d
5	3	4	5	mm5
6	4	5	6	9
