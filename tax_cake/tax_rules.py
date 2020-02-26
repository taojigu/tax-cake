# -*- coding: UTF-8 -*-
def pinYearTaxDict(money):
    if money <= 36000:
        return taxDict(0.03,0)
    elif money <= 144000:
        return taxDict(0.1,2520)
    elif money <= 300000:
        return taxDict(0.2,16920)
    elif money <= 420000:
        return taxDict(0.25,31920)
    elif money <= 660000:
        return taxDict(0.3,52920)
    elif money <= 960000:
        return taxDict(0.35,85920)

    return taxDict(0.45,181920)

def pinBonusTaxDict(realBonus):
    monthBouns = realBonus / 12
    if monthBouns <= 3000:
        return taxDict(0.03,0)
    elif monthBouns <= 12000:
        return taxDict(0.1,210)
    elif monthBouns <= 25000:
        return taxDict(0.2,1410)
    elif monthBouns <= 35000:
        return taxDict(0.25,2660)
    elif monthBouns <= 55000:
        return taxDict(0.3,4410)
    elif monthBouns <= 80000:
        return taxDict(0.35,7160)
    return taxDict(0.45,15160)

def taxDict(rate,deduction):
    return { 'rate' : rate, 'deduction' : deduction}

def yearSalaryTextInput ():
    text = ("请输入您扣除五险一金和个税低折扣后的月薪: "
    "(例如您税前月薪30000元，五险一金扣除5000元，"
    "赡养两位老人抵扣2000元，"
    "第一套房贷利息抵扣1000元，"
    "您在此应该输入的的金额应该是30000-5000-2000-1000=22000) ")
    return text

