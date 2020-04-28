'''我们在刚开始上课的时候介绍过一个小学四则运算自动生成程序的例子，请实现它，要求：
能够自动生成四则运算练习题
可以定制题目数量
用户可以选择运算符
用户设置最大数（如十以内、百以内等）
用户选择是否有括号、是否有小数
用户选择输出方式（如输出到文件、打印机等）
最好能提供图形用户界面（根据自己能力选做，以完成上述功能为主）'''
import random
#四则运算式参数列表生成（不带括号）
def getList(Operator,max_num,decimal_status,decimal_digit):
    operator = []
    calculate_num = []
    operate_num = random.randint(2, 3)#操作数数量
    operator_num = operate_num - 1#操作符数量
    for i in range(operate_num):
        if decimal_status == 1:
            calculate_num.append(random.randint(0, max_num))
        elif decimal_status ==0:
            if random.randint(0,1) == 1:
                calculate_num.append(random.randint(0, max_num))
            else:
                calculate_num.append(round(random.uniform(0, max_num),decimal_digit))
    for i in range(operator_num):
        operator.append(Operator[random.randint(0, len(Operator) - 1)])
        if operator[i] == '/':
            while calculate_num[i+1] == 0:
                if decimal_status == 1:
                    calculate_num[i + 1] = random.randint(0, max_num)
                elif decimal_status == 0:
                    if random.randint(0,1) == 1:
                        calculate_num[i+1] = random.randint(0, max_num)
                    else:
                        calculate_num[i + 1] = round(random.uniform(0, max_num),decimal_digit)
    if decimal_status == 1:
        for i in range(len(operator)):
            if i == 0:
                if operator[i] == '*':
                    temp = calculate_num[i] * calculate_num[i + 1]
                elif operator[i] == '/':
                    while calculate_num[i] % calculate_num[i + 1] != 0:
                        calculate_num[i] = random.randint(0, max_num)
                        calculate_num[i + 1] = random.randint(0, max_num)
                        while calculate_num[i + 1] == 0:
                            calculate_num[i + 1] = random.randint(0, max_num)
                    temp = calculate_num[i] // calculate_num[i + 1]
            else:
                if operator[i] == '*':
                    if operator[i - 1] == '*' or operator[i - 1] == '/':
                        temp = temp * calculate_num[i + 1]
                    else:
                        temp = calculate_num[i] * calculate_num[i + 1]
                elif operator[i] == '/':
                    if operator[i - 1] == '*' or operator[i - 1] == '/':
                        while temp % calculate_num[i + 1] != 0:
                            calculate_num[i + 1] = random.randint(0, max_num)
                            while calculate_num[i + 1] == 0:
                                calculate_num[i + 1] = random.randint(0, max_num)
                        temp = temp // calculate_num[i + 1]
                    else:
                        while calculate_num[i] % calculate_num[i + 1] != 0:
                            calculate_num[i] = random.randint(0, max_num)
                            calculate_num[i + 1] = random.randint(0, max_num)
                            while calculate_num[i + 1] == 0:
                                calculate_num[i + 1] = random.randint(0, max_num)
                        temp = calculate_num[i] // calculate_num[i + 1]
    return operator,calculate_num


#四则运算式参数列表生成（带括号）
def getList2(Operator,max_num,decimal_status,decimal_digit):
    operator = []
    calculate_num = []
    operate_num = random.randint(3,4)#操作数的数量
    operator_num = operate_num - 1#操作符数量
    for i in range(operate_num):
        if decimal_status == 1:
            calculate_num.append(random.randint(0, max_num))
        elif decimal_status == 0:
            if random.randint(0,1) == 1:
                calculate_num.append(random.randint(0, max_num))
            else:
                calculate_num.append(round(random.uniform(0, max_num),decimal_digit))
    for i in range(operator_num):
        operator.append(Operator[random.randint(0, len(Operator) - 1)])
        if operator[i] == '/':
            while calculate_num[i+1] == 0:
                if decimal_status == 1:
                    calculate_num[i+1] = random.randint(0,max_num)
                elif decimal_status == 0:
                    if random.randint(0,1) == 1:
                        calculate_num[i+1] = random.randint(0, max_num)
                    else:
                        calculate_num[i+1] = round(random.uniform(0, max_num),decimal_digit)
    if decimal_status == 1:
        for i in range(len(operator)):
            if i == 0:
                if operator[i] == '*':
                    temp = calculate_num[i] * calculate_num[i + 1]
                elif operator[i] == '/':
                    while calculate_num[i] % calculate_num[i + 1] != 0:
                        calculate_num[i] = random.randint(0, max_num)
                        calculate_num[i + 1] = random.randint(0, max_num)
                        while calculate_num[i + 1] == 0:
                            calculate_num[i + 1] = random.randint(0, max_num)
                    temp = calculate_num[i] // calculate_num[i + 1]
                elif operator[i] == '+':
                    temp = calculate_num[i] + calculate_num[i + 1]
                elif operator[i] == '-':
                    temp = calculate_num[i] - calculate_num[i + 1]
            elif i == 1:
                if operator[i] == '*':
                    temp = temp * calculate_num[i + 1]
                elif operator[i] == '/':
                    while temp % calculate_num[i + 1] != 0:
                        calculate_num[i + 1] = random.randint(0, max_num)
                        while calculate_num[i + 1] == 0:
                            calculate_num[i + 1] = random.randint(0, max_num)
                    temp = temp // calculate_num[i + 1]
            else:
                if operator[i] == '*':
                    if operator[i - 1] == '*' or operator[i - 1] == '/':
                        temp = temp * calculate_num[i + 1]
                    else:
                        temp = calculate_num[i] * calculate_num[i + 1]
                elif operator[i] == '/':
                    if operator[i - 1] == '*' or operator[i - 1] == '/':
                        while temp % calculate_num[i + 1] != 0:
                            calculate_num[i + 1] = random.randint(0, max_num)
                            while calculate_num[i + 1] == 0:
                                calculate_num[i + 1] = random.randint(0, max_num)
                        temp = temp // calculate_num[i + 1]
                    else:
                        while calculate_num[i] % calculate_num[i + 1] != 0:
                            calculate_num[i] = random.randint(0, max_num)
                            calculate_num[i + 1] = random.randint(0, max_num)
                            while calculate_num[i + 1] == 0:
                                calculate_num[i + 1] = random.randint(0, max_num)
                        temp = calculate_num[i] // calculate_num[i + 1]

    return operator,calculate_num
#四则运算式组合
def getFormula(operator,calculate_num,brackets=0):
    formula = ''
    if brackets == 0 or brackets == 1:
        formula = str(calculate_num[0])
        for i in range(len(operator)):
            formula = formula + operator[i] + str(calculate_num[i + 1])
    elif brackets == 2:
        formula = '(' + str(calculate_num[0])
        for i in range(len(operator)):
            if i == 0:
                formula = formula + operator[i] + str(calculate_num[i + 1]) + ')'
            else:
                formula = formula + operator[i] + str(calculate_num[i + 1])
    return formula


    #四则式列表生成模块，传入参数需：program_num,Operator,max_num,decimal_status,decimal_digit，返回值为ProgramList
def getProgramList(program_num,Operator,max_num,decimal_status,decimal_digit,blackets):
    ProgramList = []
    while len(ProgramList) != program_num:  #利用集合元素的唯一性获得无重复四则式列表
        if blackets == 0:
            brackets_probability = random.randint(0, 2)     #2/3概率为不带括号，1/3概率为带括号
            if brackets_probability==0 or brackets_probability == 1:
                operator,calculate_num = getList(Operator,max_num,decimal_status,decimal_digit)
                ProgramList.append(getFormula(operator,calculate_num,brackets_probability))
            elif brackets_probability==2:
                operator,calculate_num = getList2(Operator,max_num,decimal_status,decimal_digit)
                ProgramList.append(getFormula(operator,calculate_num,brackets_probability))
        elif blackets == 1:
            operator, calculate_num = getList(Operator, max_num, decimal_status, decimal_digit)
            ProgramList.append(getFormula(operator, calculate_num))
        ProgramList = set(ProgramList)      #列表转集合
        ProgramList = list(ProgramList)     #集合转列表
    return ProgramList


    #计算模块，传入参数需：decimal_status,decimal_digit,ProgramList,Program_Answer，返回值为Program_Answer
def Compute_Answer(program_num, decimal_status, decimal_digit, ProgramList):
    ProgramList_Temp = []
    Program_Answer = []
    if decimal_status == 1:#如果不包括小数
        for i in ProgramList:
            ProgramList_Temp.append(i.replace('/', '//'))
        for i in range(program_num):
            Program_Answer.append(eval(ProgramList_Temp[i]))
    elif decimal_status == 0:
        for i in range(len(ProgramList)):
            Program_Answer.append(round(eval(ProgramList[i]),decimal_digit))
    return Program_Answer


    #输出模块，传入参数：Output_Mode,ProgramList,Program_Answer
def Output_Module(program_num,ProgramList,Program_Answer):
    print(str(program_num) + "道题目已生成，请选择操作方式：\n"
                        "1-输出至屏幕同时存为文件 2-仅输出至屏幕")
    while True:
        try:
            Output_Mode = int(input())
            while Output_Mode not in [1,2]:
                Output_Mode = int(input("无该选项，请重新选择：1-输出至屏幕同时存为文件 2-仅输出至屏幕\n"))
        except ValueError:
            print("请输入正确选项！！！")
        else:
            break
    if Output_Mode == 1:
        print_screen(program_num,ProgramList,Program_Answer)
        count1 = count2 = 1
        with open('Program.txt','w',encoding='UTF-8') as f:
            f.write("题目如下：\n")
            for i in range(program_num):
                f.write(str(count1) + '、' + str(ProgramList[i]) + '='+'\n')
                count1 += 1
        with open('Answer.txt', 'w', encoding='UTF-8') as f:
            f.write("答案如下：\n")
            for i in range(program_num):
                f.write(str(count2) + '、' + str(Program_Answer[i])+'\n')
                count2 += 1
    else:
        print_screen(program_num,ProgramList,Program_Answer)


def print_screen(program_num,ProgramList,Program_Answer):
        count1 = count2 = 1
        print("题目如下：")
        for i in range(program_num):
            print(str(count1)+'、'+ str(ProgramList[i]) + '=')
            count1+=1
        while True:
            try:
                Answer_Print = int(input("是否输出答案：0-是 1-否"))
                while Answer_Print not in [0,1]:
                    Answer_Print = int(input("无该选项，请重新选择：0-是 1-否"))
            except ValueError:
                print("请输入正确选项！")
            else:
                break
        if Answer_Print == 0:
            print("答案如下：")
            for i in range(program_num):
                print(str(count2) + '、' + str(Program_Answer[i]))
                count2+=1

def main():
    while True:
        try:
            program_num = int(input("请输入题目数量："))
            while program_num <= 0:
                program_num = int(input("输入为非正整数！！！\n请输入有效题目数量："))
        except ValueError:
            print("请输入整数！！！")
        else:
            break
    while True:
        try:
            max_num = int(input("请输入最大操作数："))
            while max_num < 0:
                max_num = int(input("输入为负数！！！\n请输入有效最大操作数："))
        except ValueError:
            print("请输入非负整数！")
        else:
            break

    while True:
        try:
            blackets = int(input("是否包含括号：0-是 1-否\n"))
            while blackets not in [0,1]:
                blackets = int(input("无该选项，请重新选择：0-是 1-否\n"))
        except ValueError:
            print("请输入正确选项！")
        else:
            break
    while True:
        try:
            decimal_status = int(input("是否包括小数：0-是 1-否\n"))
            while decimal_status not in [0,1]:
                decimal_status = int(input("无该选项，请重新选择：0-是 1-否\n"))
        except ValueError:
            print("请输入正确选项！")
        else:
            break
    decimal_digit = 0
    if decimal_status == 0:
        while True:
            try:
                decimal_digit = int(input("请输入小数位数:"))
                while decimal_digit < 0:
                    decimal_digit = int(input("输入为非正整数！！！\n请输入有效小数位数："))
            except ValueError:
                print("请输入非负整数！")
            else:
                break

    Operator_str_temp = input("请输入操作符，以空格隔开：")
    Operator_str = Operator_str_temp.strip(' ')
    Operator = Operator_str.split(' ')
    while True:
        count = 0
        for i in Operator:
            if i not in ['+','-','*','/']:
                Operator_str_temp = input("输入含非运算符！！！\n请输入正确的操作符：")
                Operator_str = Operator_str_temp.strip(' ')
                Operator = Operator_str.split(' ')
                break
            else:
                count += 1
        if count == len(Operator):
            break

    ProgramList = getProgramList(program_num,Operator,max_num,decimal_status,decimal_digit,blackets)
    Program_Answer = Compute_Answer(program_num, decimal_status, decimal_digit, ProgramList)
    Output_Module(program_num, ProgramList, Program_Answer)

if __name__ == '__main__':
    main()