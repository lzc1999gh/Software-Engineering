import tkinter
from tkinter import messagebox
from tkinter import ttk
import Part_Edition
class Main:
    def __init__(self):
        self.op = []  #操作符
        self.root = tkinter.Tk()
        self.root.title("This is a window")
        self.root.geometry("580x640")
        self.digit_status = 1  #小数 0-有 1-无
        self.bracket_status = 1  #括号 0-有 1-无
        self.decimal_digit = 0  # 小数位数
        self.max_num = 50
        self.program_num = 10
        self.programlist = []
        self.programanswerlist = []

        self.opframe = tkinter.Frame(self.root)
        Lable1 = tkinter.Label(self.opframe,text="选择算符：",width=20,font=("微软雅黑",14))
        Lable1.pack(side='left')
        self.operate=[("加法",1,tkinter.IntVar()),("减法",2,tkinter.IntVar()),("乘法",3,tkinter.IntVar()),("除法",4,tkinter.IntVar())]
        #count = 1
        for title,decides,status in self.operate:
            CheckButton = tkinter.Checkbutton(self.opframe, text=title, onvalue=1, offvalue=0, variable=status,font=("微软雅黑",14))
            CheckButton.pack(side='left')
            #count += 1
        self.opframe.grid(row=0,column=0,columnspan=2)

        Lable2 = tkinter.Label(self.root,text="请输入最大操作数：",font=("微软雅黑",14))
        Lable2.grid(row = 1,column=0)
        self.Entry1 = tkinter.Entry(self.root)
        self.Entry1.grid(row=1,column=1)
        self.Entry1.insert(0,50)
        Lable3 = tkinter.Label(self.root,text="请输入题目数量：",font=("微软雅黑",14))
        Lable3.grid(row=2, column=0)
        self.Entry2 = tkinter.Entry(self.root)
        self.Entry2.grid(row=2, column=1)
        self.Entry2.insert(0,10)

        self.bframe = tkinter.Frame(self.root)
        Lable4 = tkinter.Label(self.bframe, text="是否包括括号：", font=("微软雅黑", 14))
        Lable4.pack(side='left')
        self.status2 = tkinter.IntVar()
        self.status2.set(1)  # 设置默认选项
        self.choose2 = [("是", 0), ("否", 1)]
        for decision, value in self.choose2:
            RadioButton = tkinter.Radiobutton(self.bframe, text=decision, value=value, variable=self.status2,
                                              font=("微软雅黑", 14))
            RadioButton.pack(side='right')

        self.dframe1 = tkinter.Frame(self.root)
        Lable5 = tkinter.Label(self.dframe1, text="是否包括小数：", font=("微软雅黑", 14))
        Lable5.pack(side='left')
        self.choose1 = [("是", 0), ("否", 1)]
        self.status1 = tkinter.IntVar()
        self.status1.set(1)
        for decision, value in self.choose1:
            RadioButton = tkinter.Radiobutton(self.dframe1, text=decision, value=value, variable=self.status1,
                                              font=("微软雅黑", 14))
            RadioButton.pack(side='right')

        self.dframe2 = tkinter.Frame(self.root)
        Lable6 = tkinter.Label(self.dframe2, text="请选择小数位数:", font=("微软雅黑", 14))
        Lable6.pack(side='left')
        decimal_digit_tuple = (0,1,2,3)
        self.decimal_combobox = tkinter.ttk.Combobox(self.dframe2,values=decimal_digit_tuple)
        self.decimal_combobox.set(0)
        self.decimal_combobox.pack(side='right')


        self.bframe.grid(row=3,column=0,columnspan=2)
        self.dframe1.grid(row=4, column=0,columnspan=2)
        self.dframe2.grid(row=5, column=0, columnspan=2)


        Lable7 = tkinter.Label(self.root, text="题目：", font=("微软雅黑", 14))
        Lable7.grid(row=9,column=0)
        Lable8 = tkinter.Label(self.root, text="答案：", font=("微软雅黑", 14))
        Lable8.grid(row=10,column=0)
        self.frame1 = tkinter.Frame(self.root)
        self.frame2 = tkinter.Frame(self.root)
        self.listbox1 = tkinter.Listbox(self.frame1, height=5, font=("微软雅黑", 14))
        self.listbox2 = tkinter.Listbox(self.frame2, height=5, font=("微软雅黑", 14))
        self.scrollbar1 = tkinter.Scrollbar(self.frame1)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.scrollbar1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scrollbar2 = tkinter.Scrollbar(self.frame2)
        self.scrollbar2.config(command=self.listbox2.yview)
        self.scrollbar2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox1.pack()
        self.listbox2.pack()
        self.frame1.grid(row=9,column=1)
        self.frame2.grid(row=10, column=1)

        self.frame3 = tkinter.Frame(self.root)
        self.frame4 = tkinter.Frame(self.root)
        button = tkinter.Button(self.frame3, text="生成", command=self.makesure, font=("微软雅黑", 14))
        button.pack(side= 'top')
        programbutton = tkinter.Button(self.frame3, text="显示题目", command=self.print_program_view,
                                       font=("微软雅黑", 14))
        programbutton.pack(side= 'left',fill='x')
        answerbutton = tkinter.Button(self.frame3, text="显示答案", command=self.print_answer_view, font=("微软雅黑", 14))
        answerbutton.pack(side='right',fill='x')
        writefile = tkinter.Button(self.frame4, text="写入文件", command=self.write_file, font=("微软雅黑", 14))
        writefile.pack()
        self.frame3.grid(row=6,column=0,columnspan=2)
        self.frame4.grid(row=7, column=0, columnspan=2)
        self.root.mainloop()


    def makesure(self):
        self.getMaxNum()
        self.getProgramNum()
        self.operator_choose_handle()
        if len(self.op) == 0:
            tkinter.messagebox.showwarning("", "请至少选择一个算符！")
        self.digit_decide()
        self.bracket_decide()
        self.getDecimalDigit()
        if len(self.op) > 0:
            self.getList()
            tkinter.messagebox.showinfo("","已生成")

    def write_file(self):
        count1 = count2 = 1
        with open('Program.txt', 'w', encoding='UTF-8') as f:
            f.write("题目如下：\n")
            for i in range(self.program_num):
                f.write(str(count1) + '、' + str(self.programlist[i]) + '=' + '\n')
                count1 += 1
        with open('Answer.txt', 'w', encoding='UTF-8') as f:
            f.write("答案如下：\n")
            for i in range(self.program_num):
                f.write(str(count2) + '、' + str(self.programanswerlist[i]) + '\n')
                count2 += 1
        tkinter.messagebox.showinfo("","写入完成")

    def print_program_view(self):
        self.create_program_view(self.programlist)

    def print_answer_view(self):
        self.create_answer_view(self.programanswerlist)


    def getList(self):
        self.programlist = Part_Edition.getProgramList(self.program_num, self.op, self.max_num, self.digit_status, self.decimal_digit,
                                    self.bracket_status)
        self.programanswerlist = Part_Edition.Compute_Answer(self.program_num,self.digit_status,self.decimal_digit,self.programlist)


    def create_answer_view(self,list):
        self.listbox2.delete(0,tkinter.END)
        count = 1
        for item in list:
            self.listbox2.insert(tkinter.END,str(count) + '、' + str(item))
            count += 1


    def create_program_view(self,list):
        self.listbox2.delete(0, tkinter.END)
        count = 1
        for item in list:
            self.listbox1.insert(tkinter.END,str(count) + '、' + item)
            count += 1


    def getDecimalDigit(self):
        if self.digit_status == 0:
            self.decimal_digit = self.decimal_combobox.get()
            self.decimal_digit = int(self.decimal_digit)

    def bracket_decide(self):
        for decision,value in self.choose1:
            if self.status2.get()==value:
                if decision == '是':
                    self.bracket_status = value

    def digit_decide(self):
        for decision,value in self.choose1:
            if self.status1.get()==value:
                if decision == '是':
                    self.digit_status = value

    def getProgramNum(self):
        programnum = self.Entry2.get()
        programnum = int(programnum)
        if programnum <= 0 :
            tkinter.messagebox.showwarning("输入错误","请输入正整数！")
        self.program_num = programnum

    def getMaxNum(self):
        maxnum = self.Entry1.get()
        maxnum = int(maxnum)
        if maxnum <= 0 :
            tkinter.messagebox.showwarning("输入错误","请输入正整数！")
        self.max_num = maxnum

    def operator_choose_handle(self):
        for title,decision,status in self.operate:
            if status.get() == 1:
                if decision == 1:
                    self.op.append('+')
                elif decision == 2:
                    self.op.append('-')
                elif decision == 3:
                    self.op.append('*')
                elif decision == 4:
                    self.op.append('/')
            self.op = list(set(self.op))


def main():
    Main()

if __name__ == '__main__':
    main()
