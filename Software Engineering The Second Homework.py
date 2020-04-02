def getmax(a, b):
    return a if a > b else b

def Computer(nums):
    Max = nums[0]
    temp = 0
    for i in nums:
        temp = getmax(temp+i, i)
        if temp > Max:
            Max = temp
    return Max if Max >= 0 else 0

str_l = input("请输入一组数据：")
while(str_l!=''):
    try:
        nums = [int(n) for n in str_l.split()]
        print(Computer(nums))
        str_l = input("请输入一组数据：")
    except:
        print('输入为非数字')
        str_l = input("请输入一组数据：")


