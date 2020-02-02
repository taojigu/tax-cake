
from tax_rules import pinYearTaxDict
class YearSalaryTaxCalculator:

    _monthThreshold = 5000

    def __init__(self):
        return
     #计算单月的个税
    def taxOfMonth(self,monthIndex,monthSalary,taxSum,yearSum):
        assert(monthIndex >= 0 and monthIndex < 12 )
        assert(monthSalary > self._monthThreshold)
        inputSum = (monthSalary - self._monthThreshold) * (monthIndex +1)     
        taxDict = pinYearTaxDict(inputSum)
        rate = taxDict['rate']
        deduction = taxDict['deduction']
        tax = inputSum * rate - deduction - taxSum
        return tax

    #按照月薪，预估全年的累计数个税
    def yearSalaryTax(self,monthSalary):
        
        if monthSalary <= self._monthThreshold:
            raise '十分遗憾，您作为纳税人的荣誉被剥夺了'
            return 0

        monthIndex = 0
        salarySum = 0
        taxSum =0
        while (monthIndex < 12):
            salarySum += monthSalary
            taxSum += self.taxOfMonth(monthIndex,monthSalary,taxSum,salarySum)
            monthIndex += 1
        return taxSum
    
    def yearSalayMain:
        
        return
   

cal = YearSalaryTaxCalculator()
ys = cal.yearSalaryTax(25500)
print('year tax is %.2f' %ys)

