"""在工作中我们会遇到要从大量excel表提取数据的情况，也许这还是你的日常工作，如果你想打开每张表提取你想要的数据然后汇总，那么你一天的 工作都会被excel淹没。
下面我们将使用python自动化批量处理excel，只需一段程序，只需要几分钟你就可以从海量数据表中提取你想要的数据 并汇总输出至指定文件夹。 """

#这里我们以4张表为例进行演示，当然实际工作中也许是400、4000张表，原理和方法一样（如果是4万张表那就得看数据量大小和电脑性能了）。
#首先看看需要处理的表
import numpy as np
import pandas as pd
import os
excel = pd.read_excel(r'D:\test_excel\test1.xlsx')
excel
id	UV	PV	PRICE	ITEMS
0	1	200	400	100	1
1	2	300	500	300	3
2	3	400	600	500	5
3	4	500	700	700	7
4	5	600	800	900	9
5	6	700	900	1100	11
6	7	800	1000	1300	13
7	8	900	1100	1500	15
8	9	1000	1200	1700	17
9	10	1100	1300	1900	19
#我们要处理4张这样的表，各张表的index和columns一样，目的是求所有表ITEMS和PRICE的和，每张表UV最大值、PV平均值
dir_str = r'D:\test_excel'  #指定存放文件地址
file_name = os.listdir(dir_str)#返回指定目录下的所有文件和目录名
file_dir = [os.path.join(dir_str, x) for x in file_name]#得到所有文件路径
# print(file_dir)

def foo(): #求所有表中items和price总和
    l=0
    p=0
    m_uv = []
    m_pv = []
    for i in range(len(file_dir)):
        
        single_outer_i = pd.read_excel(file_dir[i])

        l_total = single_outer_i['ITEMS'].sum()
        p_total = single_outer_i['PRICE'].sum()
        m_uv_i = single_outer_i['UV'].max()
        m_pv_i = single_outer_i['PV'].mean()
       # m_uv_i = str(m_uv_i)
        l = l+l_total
        p = p+p_total
        
        m_uv.append(m_uv_i)
        m_pv.append(m_pv_i) 
    m_uv.append(0)
    m_pv.append(0)
        #print(type(m_uv_i))
#     print(m_uv)    
#     print(l)
#     print(p)

    
    df = pd.DataFrame(np.zeros(20).reshape(5,4),columns = ['s_items','s_price','m_uv','m_pv'],index = [
    'test1','test2','test3','test4','t_test'
])
    df.loc['t_test':,'s_items'] = l
    df.loc['t_test':,'s_price'] = p
    df['m_uv'] = m_uv
    df['m_pv'] = m_pv
    df.to_excel(r'D:\total_test.xlsx')

foo()
