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
print ('系数矩阵A：',coefficient_matrix,coefficient_matrix.shape)

#系数矩阵求逆，计算各相关变量。
coordinate_after=coordinate_after.reshape((3*num,1))
coefficient_matrix=np.matrix(coefficient_matrix)
result=np.array(np.dot(coefficient_matrix.I,coordinate_after))
result=result.tolist()
print('变量列表为',result)


variable_name=['deltaX','deltaY','deltaZ','a1','a2','a3','a4']
variable=dict(zip(variable_name,result))
print('变量为',variable)



