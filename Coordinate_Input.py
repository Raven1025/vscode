#七参数的输入
def Coordinate_Convert():
    coordinate_before=[]
    coordinate_after=[]

    num=int(input("请输入坐标对的个数："))

    for counter in range(num):
        coordinate_before.append([])
        coordinate_after.append([])
    
    #if __name__=="__main__":
    for counter in range(num):
        temp=input('请输入坐标系1下的第%s个坐标：'% str(counter+1))
        coordinate_before[counter]=list(map(float,temp.strip().split()))
        print (coordinate_before[counter])

    for counter in range(num):
        temp=input('请输入坐标系2下的第%s个坐标：'% str(counter+1))
        coordinate_after[counter]=list(map(float,temp.strip().split()))
        print (coordinate_after[counter])
        

    print(coordinate_before)
    print(coordinate_after)

    return n,coordinate_before,coordinate_after

if __name__=='__main__':
    Coordinate_Convert()