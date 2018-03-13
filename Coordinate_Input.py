#七参数的输入
def Coordinate_Input(num):
    
    before=[]
    after=[]
    
    for i in range(num):
        print("请输入第一坐标系下的第%s个坐标：" % str(i+1))
	    temp=list(map(double,input().split()))
	    before.append(temp)

    for i in range(num):
        print("请输入对应的第二坐标系下的第%s个坐标" % str(i+1))
        temp=list(map(double,input().split()))
        after.append(temp)

    return(before,after)

if __name__=="__main__":
    num=int(input("请输入坐标对数："))

    before=[]
    after=[]
    before,after=Coordinate_Input(num)
    print(before,after)