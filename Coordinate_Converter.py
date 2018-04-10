#工程测量中的七参数转换程序

import numpy as np
from Coordinate_Input import Coordinate_Input

#用户输入并储存数据
num,coordinate_before,coordinate_after=Coordinate_Input()


#转化为np数组求解矩阵
coordinate_before=np.array(coordinate_before)
coordinate_after=np.array(coordinate_after)

#形成系数矩阵
coefficient_matrix=np.zeros((1,7))

for i in range(num):
    temp=np.array([(coordinate_before[i][0],0,(-1)*coordinate_before[i][2],coordinate_before[i][1]),
                  (coordinate_before[i][1],coordinate_before[i][2],0,(-1)*coordinate_before[i][0]),
                  (coordinate_before[i][2],(-1)*coordinate_before[i][1],coordinate_before[i][0],0)],
                  dtype=float
                 )
    temp1=np.concatenate((np.eye(3),temp),axis=1)
    coefficient_matrix=np.concatenate((coefficient_matrix,temp1),axis=0)
coefficient_matrix=coefficient_matrix[1:]
print (coefficient_matrix,coefficient_matrix.shape)