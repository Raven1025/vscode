#-*- coding:utf-8 -*-
import numpy as np

def Coordinate_Output(variable_matrix):
    #输入待转换坐标
    coordinate_tochange=list(map(float,input("Enter the coordinate to change:").strip().split()))
    print(coordinate_tochange)

    #形成转换矩阵并与系数矩阵相乘
    temp1=np.array(coordinate_tochange)
    temp2=np.array([(temp1[0],0,(-1)*temp1[2],temp1[1]),
                    (temp1[1],temp1[2],0,(-1)*temp1[0]),
                    (temp1[2],(-1)*temp1[1],temp1[0],0)],
                    dtype=float
                    )
    temp2=np.concatenate((np.eye(3),temp2),axis=1)
    print ('待转换的坐标为',temp1,'系数矩阵A为',temp2)
    coordinate_afterchange=np.dot(temp2,variable_matrix)
    print('转换后坐标为',coordinate_afterchange)

if __name__=='__main__':
    variable_matrix=[[2844211.51842746], [-762548.8866621036], [-33617.19309716266], [24.90383173332222], [27.789900141536528], [941.1726466505137], [-23234.417487434155]]
    Coordinate_Output(variable_matrix)