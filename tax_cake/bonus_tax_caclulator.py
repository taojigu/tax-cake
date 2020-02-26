# -*- coding: UTF-8 -*-
from tax_rules import yearSalaryTextInput

class BonusTaxCalculator:
    
    def bonusSuitTax(sefl,monthCount,monthSalary,totalPackage,bonusPart):
        return 1000



def printIntrocution():
    intro = ("如果您的年终奖和当月工资一起发放（例如 20 万）,如何分配二者的额度才能缴纳最少的个税"
    "就成了摆在您面前的一个问题"
    "本工具可以帮您计算各种分配方案的结果，供您参考"
    )
    print(intro)
    print ("--------------------------------")
    return
def bonusTaxMain():
    # 打印本工具介绍
    printIntrocution()
    # 规则介绍：默认起征点5000，采用年度个税计算方式
    text = yearSalaryTextInput()
    monthSalary = int(input(text))
    # 输入年终奖和月薪总包
    package = int(input("请输入总包数额 ："))
    salaryPart = int(input("请输入工资部分数额: "))
    
    calculator = BonusTaxCalculator()
    tax = calculator.bonusSuitTax(11,monthSalary,package,salaryPart)
    print ("分配方案:月薪 %i 元，年终奖 %i 元 ==> 缴纳个税 %i 元" %(salaryPart,package-salaryPart,tax))
    return

bonusTaxMain()

